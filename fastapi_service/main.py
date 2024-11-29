import threading
from contextlib import asynccontextmanager

import uvicorn
from api import traffic
from core.settings import settings
from db import sqlite
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from grpc_server.grpc_server import serve


@asynccontextmanager
async def lifespan(app: FastAPI):
    sqlite.db = sqlite.SessionLocal()
    yield sqlite.db.close()


app = FastAPI(
    title=settings.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)


grpc_thread = threading.Thread(target=serve, daemon=True)
grpc_thread.start()


app.include_router(traffic.router, prefix="/traffic", tags=["traffic"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
