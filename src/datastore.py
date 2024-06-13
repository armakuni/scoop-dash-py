import os

from sqlalchemy import create_engine

DATABASE_URL = os.environ.get(
    "DATABASE_URL", "postgresql://postgres:scoopdash@localhost:5433/postgres"
)

engine = create_engine(DATABASE_URL, echo=True, future=True)
