"""
Event ingestion routes - receive agent execution logs
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Any, Dict
import sqlite3
from datetime import datetime
import json

router = APIRouter(prefix="/events", tags=["Events"])

class EventIngest(BaseModel):
    session_id: int
    event_type: str  # request, response, error, tool_call, etc.
    input: Optional[Any] = None
    output: Optional[Any] = None
    tokens_input: Optional[int] = None
    tokens_output: Optional[int] = None
    latency_ms: Optional[int] = None
    cost_usd: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = None

def get_db():
    conn = sqlite3.connect("./agentguard.db")
    conn.row_factory = sqlite3.Row
    return conn

@router.post("/ingest", status_code=201)
async def ingest_event(event: EventIngest):
    """
    Ingest an agent event. This is the main data point for monitoring.

    Example usage:
    POST /events/ingest
    {
        "session_id": 1,
        "event_type": "request",
        "input": "Hello, how are you?",
        "tokens_input": 5,
        "latency_ms": 200,
        "cost_usd": 0.001
    }
    """
    conn = get_db()
    try:
        cur = conn.cursor()
        # Verify session exists
        cur.execute("SELECT id FROM sessions WHERE id = ?", (event.session_id,))
        if not cur.fetchone():
            raise HTTPException(status_code=404, detail=f"Session {event.session_id} not found")

        cur.execute("""
            INSERT INTO events (
                session_id, event_type, input, output,
                tokens_input, tokens_output, latency_ms, cost_usd, metadata
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            event.session_id,
            event.event_type,
            json.dumps(event.input) if event.input else None,
            json.dumps(event.output) if event.output else None,
            event.tokens_input,
            event.tokens_output,
            event.latency_ms,
            event.cost_usd,
            json.dumps(event.metadata) if event.metadata else None
        ))
        conn.commit()
        return {"success": True, "event_id": cur.lastrowid}
    finally:
        conn.close()

@router.get("/stats/{session_id}")
async def get_session_stats(session_id: int):
    """Get aggregated stats for a session"""
    conn = get_db()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT
                COUNT(*) as total_events,
                SUM(COALESCE(cost_usd, 0)) as total_cost,
                AVG(COALESCE(latency_ms, 0)) as avg_latency,
                SUM(COALESCE(tokens_input, 0)) as total_tokens_in,
                SUM(COALESCE(tokens_output, 0)) as total_tokens_out
            FROM events
            WHERE session_id = ?
        """, (session_id,))
        row = cur.fetchone()

        if not row or row['total_events'] == 0:
            raise HTTPException(status_code=404, detail="No events found for session")

        return {
            "session_id": session_id,
            "total_events": row['total_events'],
            "total_cost_usd": round(row['total_cost'], 6),
            "avg_latency_ms": round(row['avg_latency'], 2),
            "total_tokens_input": row['total_tokens_in'],
            "total_tokens_output": row['total_tokens_out']
        }
    finally:
        conn.close()
