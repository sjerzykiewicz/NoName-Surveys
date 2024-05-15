from sqlmodel import Session, SQLModel, create_engine

from config import settings

# this is to be changed later on in the development
engine = create_engine(
    "sqlite://",
    echo=(settings.environment_type == "dev"),
    connect_args={"check_same_thread": False},
)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
