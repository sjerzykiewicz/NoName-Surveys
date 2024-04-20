from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

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


app.include_router(api_router)


def init_db():
    SQLModel.metadata.create_all(engine)
