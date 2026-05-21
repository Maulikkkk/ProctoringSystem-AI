from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.proctor import router as proctor_router
from app.routes.report import router as report_router
from app.routes.session import router as session_router
from app.routes.tab import router as tab_router


app = FastAPI()
app.include_router(tab_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(proctor_router)
app.include_router(report_router)
app.include_router(session_router)
@app.get("/")
def home():
    return {
        "message": "AI Proctoring Backend Running"
    }