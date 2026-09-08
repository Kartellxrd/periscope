from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings

# Create SQLAlchemy 2.x engine
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # Automatically check for dead connections
    pool_size=10,
    max_overflow=20,
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """
    Dependency function to inject DB sessions into FastAPI route handlers.
    Ensures connection is always closed after request completion.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()