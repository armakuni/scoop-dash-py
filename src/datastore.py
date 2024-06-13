import os

from sqlalchemy import create_engine

DATABASE_URL = (
    os.environ["DATABASE_URL"]
    if "DATABASE_URL" in os.environ
    else "postgresql://postgres:scoopdash@localhost:5433/postgres"
)

engine = create_engine(DATABASE_URL, echo=True, future=True)
