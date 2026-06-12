from contextlib import asynccontextmanager
from fastapi import FastAPI
from entity_store import init_db
from models import ObfuscateRequest, ObfuscateResponse
from obfuscator import obfuscate_dataset


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Obfuscation Microservice", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/obfuscate", response_model=ObfuscateResponse)
def obfuscate(request: ObfuscateRequest) -> ObfuscateResponse:
    obfuscated_rows = obfuscate_dataset(request.columns, request.rows)
    return ObfuscateResponse(columns=request.columns, rows=obfuscated_rows)
