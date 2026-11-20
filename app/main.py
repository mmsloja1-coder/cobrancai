"""
AgentGuard Brasil - AI Agent Observability Platform
Monitors AI agent costs, detects anomalies, ensures LGPD compliance
"""
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
import sqlite3
import os
from datetime import datetime
from dotenv import load_dotenv
from .routers.agents import router as agents_router
from .routers.events import router as events_router

# Port configuration
PORT = int(os.getenv("PORT", "8000"))

load_dotenv()

# Database setup
DB_PATH = os.getenv("DATABASE_URL", "sqlite:///./agentguard.db").replace("sqlite:///", "")

# Ensure database directory exists
os.makedirs(os.path.dirname(DB_PATH) if os.path.dirname(DB_PATH) else ".", exist_ok=True)

def init_db():
    """Initialize SQLite database with required tables"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS agents (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            model TEXT,
            provider TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agent_id TEXT NOT NULL,
            started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            ended_at TIMESTAMP,
            FOREIGN KEY (agent_id) REFERENCES agents(id)
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            event_type TEXT NOT NULL,
            input TEXT,
            output TEXT,
            tokens_input INTEGER,
            tokens_output INTEGER,
            latency_ms INTEGER,
            cost_usd REAL,
            metadata TEXT,
            FOREIGN KEY (session_id) REFERENCES sessions(id)
        )
    """)
    conn.commit()
    conn.close()

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="AgentGuard Brasil",
    description="AI Agent Observability & Compliance Platform",
    version="0.1.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend - define path early for use in routes
frontend_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend')

# Include routers
app.include_router(agents_router)
app.include_router(events_router)

@app.get("/")
async def root():
    """Serve frontend index.html"""
    if os.path.exists(frontend_dir):
        return FileResponse(os.path.join(frontend_dir, "index.html"))
    return {"service": "AgentGuard Brasil", "status": "error", "message": "Frontend not found"}

@app.get("/health")
async def health():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}

# Serve frontend at /frontend path
frontend_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend')
if os.path.exists(frontend_dir):
    app.mount("/frontend", StaticFiles(directory=frontend_dir), name="static")

    @app.get("/dashboard")
    async def dashboard():
        from fastapi.responses import RedirectResponse
        return RedirectResponse(url="/frontend/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT, log_level="debug")
