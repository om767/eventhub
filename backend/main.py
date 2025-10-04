from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

# Import your routers and database models/session
from .database import engine, Base
from .routers import AuthenticationRouter, organizer, shared, gemini

# Tables already exist in the database, so we don't need to create them
# Base.metadata.create_all(bind=engine)

# --- FastAPI Application Setup ---

app = FastAPI(
    title="EventHub API",
    description="Backend API for the EventHub application.",
    version="0.1.0",
)

# --- CORS (Cross-Origin Resource Sharing) ---
# Allows your frontend to communicate with the backend API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Include API Routers ---
# This integrates all your API endpoints from the /routers directory
app.include_router(AuthenticationRouter.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(organizer.router, prefix="/api/organizer", tags=["Organizer"])
app.include_router(shared.router, prefix="/api/shared", tags=["Shared"])
app.include_router(gemini.router, prefix="/api/ai", tags=["AI"])

# --- Serve Frontend ---
frontend_dir = os.path.join(os.path.dirname(__file__), '..', 'front end')

# This mounts your entire 'front end' directory. FastAPI will automatically
# look for files like 'style.css' or 'about.html' here.
app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="static")

# The `html=True` argument tells StaticFiles to serve 'landing.html' for the
# root path ('/'). It also handles a neat trick: if a request comes in for a
# path that doesn't match a file (like '/login'), it will serve 'landing.html',
# which is perfect for single-page applications that use client-side routing.
@app.exception_handler(404)
async def custom_404_handler(_, __):
    return FileResponse(os.path.join(frontend_dir, 'index.html'))
