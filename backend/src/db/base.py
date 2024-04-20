from sqlmodel import Session, SQLModel, create_engine

# this is to be changed later on in the development
engine = create_engine(
    "sqlite://", echo=True, connect_args={"check_same_thread": False}
)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
