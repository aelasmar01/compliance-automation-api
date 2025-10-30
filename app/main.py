from fastapi import FastAPI
from app.db import Base, engine
import app.models  # register models with metadata

app = FastAPI(title="Compliance API")

@app.get("/health")
def health():
    return {"status": "ok"}
