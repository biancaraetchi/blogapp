from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine

from models import Post  # noqa

# Initialize SQLite database
DATABASE_URL = "sqlite:///./blog.db"
ENGINE = create_engine(
    DATABASE_URL, echo=True
)

# Session to work with
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)


def create_tables():
    """Create tables."""
    SQLModel.metadata.create_all(ENGINE)


def get_db():
    """Get database connection."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        2
    session.close()


if __name__ == "__main__":
    create_tables()
