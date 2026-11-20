"""
Agent management routes
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import sqlite3
from datetime import datetime

router = APIRouter(prefix="/agents", tags=["Agents"])

class AgentCreate(BaseModel):
    id: str
    name: str
    model: Optional[str] = None
    provider: Optional[str] = None

class AgentResponse(BaseModel):
    id: str
    name: str
    model: Optional[str]
    provider: Optional[str]
    created_at: str

def get_db():
    conn = sqlite3.connect("./agentguard.db")
    conn.row_factory = sqlite3.Row
    return conn

@router.post("/", response_model=AgentResponse)
async def create_agent(agent: AgentCreate):
    """Register a new AI agent"""
    conn = get_db()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT OR REPLACE INTO agents (id, name, model, provider, created_at) VALUES (?, ?, ?, ?, ?)",
            (agent.id, agent.name, agent.model, agent.provider, datetime.utcnow().isoformat())
        )
        conn.commit()
        return AgentResponse(
            id=agent.id,
            name=agent.name,
            model=agent.model,
            provider=agent.provider,
            created_at=datetime.utcnow().isoformat()
        )
    finally:
        conn.close()

@router.get("/", response_model=List[AgentResponse])
async def list_agents():
    """List all registered agents"""
    conn = get_db()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM agents ORDER BY created_at DESC")
        rows = cur.fetchall()
        return [AgentResponse(**dict(row)) for row in rows]
    finally:
        conn.close()

@router.get("/{agent_id}", response_model=AgentResponse)
async def get_agent(agent_id: str):
    """Get single agent details"""
    conn = get_db()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM agents WHERE id = ?", (agent_id,))
        row = cur.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Agent not found")
        return AgentResponse(**dict(row))
    finally:
        conn.close()
