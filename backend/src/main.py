import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlmodel import SQLModel

from config import settings
from src.api.router import api_router
from src.db.base import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # before startup logic
    init_db()
    yield
    # we can implement post-shutdown logic here in the future


app = FastAPI(lifespan=lifespan)

origins = ["http://localhost:5173", "localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()


@app.middleware("http")
async def validate_token(request: Request, call_next):
    if request.url.path == "/docs" or request.url.path == "/openapi.json":
        return await call_next(request)

    if os.getenv("TESTING", False):  # Skip validation in tests
        return await call_next(request)

    if "Authorization" not in request.headers:
        raise HTTPException(status_code=403, detail="Authorization header missing")

    auth: HTTPAuthorizationCredentials = await security(request)
    token = auth.credentials

    if token != settings.bearer_token:
        raise HTTPException(status_code=403, detail="Invalid token")

    return await call_next(request)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="NoName Anonymous Surveys API",
        version="1.0.0",
        description="This is the API for the NoName Anonymous Surveys project.",
        routes=app.routes,
    )
    security_scheme = {
        "HTTPBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    openapi_schema["components"]["securitySchemes"] = security_scheme
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"HTTPBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


app.include_router(api_router)


def init_db():
    SQLModel.metadata.create_all(engine)
