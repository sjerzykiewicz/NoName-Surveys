from sqlmodel import Session, SQLModel, create_engine

from config import settings


def db_connection_is_provided():
    return (
        hasattr(settings, "db_type")
        and settings.db_type
        and hasattr(settings, "db_user")
        and settings.db_user
        and hasattr(settings, "db_password")
        and settings.db_password
        and hasattr(settings, "db_host")
        and settings.db_host
        and hasattr(settings, "db_name")
        and settings.db_name
    )


def create_url():
    db_type = settings.db_type
    db_dialect = "+" + settings.db_dialect if settings.db_dialect else ""
    db_user = settings.db_user
    db_password = settings.db_password
    db_host = settings.db_host
    db_port = ":" + str(settings.db_port) if settings.db_port else ""
    db_name = settings.db_name

    return (
        f"{db_type}{db_dialect}://{db_user}:{db_password}@{db_host}{db_port}/{db_name}"
    )


def create_db_engine():
    return (
        create_engine(create_url())
        if db_connection_is_provided()
        else create_engine(
            "sqlite://",
            connect_args={"check_same_thread": False},
        )
    )


engine = create_db_engine()


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
