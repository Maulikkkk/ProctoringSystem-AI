# AI Proctoring System

This repository contains a full-stack AI proctoring system with separated `backend` and `frontend` applications.

## Structure

- `backend/`
  - `app/`
    - `main.py` - FastAPI application entrypoint
    - `routes/` - API routes for proctoring and report generation
    - `services/` - AI detection and reporting service placeholders
    - `models/` - Pydantic data models
    - `utils/` - helper utilities
    - `database/` - MongoDB connection stub
  - `requirements.txt` - backend Python dependencies
  - `yolov8n.pt` - model file placeholder

- `frontend/`
  - `src/` - React source files
  - `package.json` - frontend dependencies and scripts

## Setup

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm start
```
