<div align="center">

# 🎯 AI Proctoring System

### Intelligent Interview Monitoring with Real-Time Computer Vision & AI Evaluation

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-FF6B35?style=for-the-badge)](https://ultralytics.com)
[![Mistral AI](https://img.shields.io/badge/Mistral-AI-7C3AED?style=for-the-badge)](https://mistral.ai)
[![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)](LICENSE)

<br/>

> An AI-powered interview proctoring system that uses lightweight computer vision models and an **event-driven architecture** to detect suspicious behavior and delivering intelligent evaluation reports at a fraction of the cost of traditional LLM-heavy approaches.

<br/>

[Features](#-features) · [Architecture](#-architecture) · [Tech Stack](#-tech-stack) · [Setup](#-setup) · [API Reference](#-api-reference) · [Roadmap](#-roadmap)

</div>

---

## 🧠 The Problem with Traditional AI Proctoring

Most existing proctoring systems are expensive and inefficient:

| Traditional Approach | This System |
|---|---|
| ❌ Continuously streams frames to LLMs | ✅ Uses lightweight CV models per frame |
| ❌ High per-inference API cost | ✅ Single final LLM call for evaluation |
| ❌ Latency from repeated LLM round-trips | ✅ Real-time local CV processing |
| ❌ Poor scalability | ✅ Event-driven, aggregated analysis |

---

## ✨ Features

### 🔍 Real-Time Detection
- **Phone Detection** — YOLOv8-powered object detection identifies phone usage
- **Face Visibility** — MediaPipe tracks whether the candidate is present
- **Eye Gaze / Looking Away** — Detects off-screen gaze direction
- **Multiple People** — Alerts when more than one person is detected
- **Bounding Box Overlays** — Live visual annotations on webcam feed

### ⚙️ Smart Event Engine
- Stateful, debounced detection to reduce noise
- Deduplication of repeated events within short windows
- Session-level event aggregation for clean reporting

### 🤖 AI Risk Evaluation
- Rule-based risk scoring for transparent, auditable assessments
- Single final LLM call to Mistral AI — low cost, high value
- AI-generated narrative evaluation report at session end

### 🖥️ Frontend Dashboard
- Live webcam feed with detection overlays
- Real-time warning panel
- Session statistics display
- Rendered AI evaluation report

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Browser Client                   │
│         React Dashboard + Webcam Capture            │
└───────────────────────┬─────────────────────────────┘
                        │  Frame (Base64) / Events
                        ▼
┌─────────────────────────────────────────────────────┐
│                  FastAPI Backend                    │
│                                                     │
│  ┌──────────────────────────────────────────────┐   │
│  │        Computer Vision Detection Layer       │   │
│  │   YOLOv8 (Phone)  +  MediaPipe (Face/Gaze)  │   │
│  └──────────────────────┬───────────────────────┘   │
│                         │                           │
│  ┌──────────────────────▼───────────────────────┐   │
│  │          Smart Event Aggregation Engine      │   │
│  │    Debouncing · Deduplication · Counting     │   │
│  └──────────────────────┬───────────────────────┘   │
│                         │                           │
│  ┌──────────────────────▼───────────────────────┐   │
│  │           Rule-Based Risk Scorer             │   │
│  └──────────────────────┬───────────────────────┘   │
│                         │  (End of session only)    │
│  ┌──────────────────────▼───────────────────────┐   │
│  │         Mistral AI — Single LLM Call         │   │
│  │        Generates Final Evaluation Report     │   │
│  └──────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React 18, Vite, Axios |
| **Backend** | FastAPI, Python 3.10+ |
| **Object Detection** | YOLOv8 (Ultralytics) |
| **Face & Gaze Tracking** | MediaPipe, OpenCV |
| **AI Evaluation** | Mistral AI |

---

## 📁 Folder Structure

```
ai-proctoring-system/
│
├── backend/
│   ├── app/
│   │   ├── routes/           # API route handlers
│   │   ├── services/         # Detection & evaluation logic
│   │   ├── models/           # Pydantic data models
│   │   ├── utils/            # Helper utilities
│   │   └── database/         # Session storage layer
│   │
│   ├── requirements.txt
│   └── main.py               # FastAPI entry point
│
├── frontend/
│   ├── src/
│   │   ├── components/       # React UI components
│   │   ├── services/         # API communication layer
│   │   └── assets/           # Static assets
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## 🚀 Setup

### Prerequisites
- Python 3.10+
- Node.js 18+
- A [Mistral AI API key](https://console.mistral.ai/)

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-proctoring-system.git
cd ai-proctoring-system
```

---

### 2. Backend Setup

```bash
cd backend

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app.main:app --reload
```

Backend runs at: **`http://127.0.0.1:8000`**

---

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start the dev server
npm run dev
```

Frontend runs at: **`http://localhost:5173`**

---

### 4. Environment Variables

Create a `.env` file inside the `backend/` directory:

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## 📡 API Reference

### `POST /analyze-frame`
Analyzes a single webcam frame for suspicious behavior.

**Detects:**
- Phone usage
- Face visibility
- Gaze direction (looking away)
- Multiple people in frame

---

### `GET /generate-report`
Triggers the final AI evaluation at session end.

**Returns:**
- Session-level event statistics
- Rule-based risk score
- Mistral AI-generated evaluation narrative

---

### `GET /session-stats`
Returns aggregated detection counts for the current session.

**Example Response:**
```json
{
  "phone_count": 1,
  "looking_away_count": 2,
  "multiple_people_count": 0,
  "tab_switch_count": 1
}
```

---

### `POST /tab-switch`
Logs a browser tab-switch event from the frontend.

---

## 🗺️ Roadmap

- [ ] MongoDB integration for persistent session storage
- [ ] Authentication system (JWT-based)
- [ ] Admin dashboard for reviewers
- [ ] WebSocket streaming for lower latency
- [ ] Browser-side inference (TensorFlow.js)
- [ ] Docker deployment support
- [ ] Cloud deployment guides (AWS / GCP / Azure)
- [ ] Advanced behavioral analytics & trend reports

---


## 👤 Author

**Maulik Gupta**
B.Tech CSE (AI) — Bennett University
AI/ML Specialization — IIT Indore

<div align="left">

[![GitHub](https://github.com/Maulikkkk)
[![LinkedIn](https://www.linkedin.com/in/maulikg29/)

</div>

---

<div align="center">

*Built with ❤️ using open-source AI tools*

</div>
