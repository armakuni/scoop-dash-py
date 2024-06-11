from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class InterestedVisitor(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr = Field(unique=True)
