from datetime import UTC, datetime

from sqlmodel import Field, SQLModel


class GreetingIncident(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC), nullable=False
    )
