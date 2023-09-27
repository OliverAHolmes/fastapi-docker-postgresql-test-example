from typing import Optional
from datetime import datetime as dt
from sqlmodel import Field, SQLModel, Column, String


class User(SQLModel, table=True):
    """Represents a user stored in the database."""

    __tablename__ = "user"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    username: str = Field(
        description="Username for the user.",
    )
    email: str = Field(
        sa_column=Column(String, unique=True, index=True),
        description="Email address of the user.",
    )
    full_name: Optional[str] = Field(
        description="Full name of the user.",
    )
    hashed_password: str = Field(
        description="Hashed password for the user.",
    )
    created_at: dt = Field(
        default_factory=dt.utcnow,
        description="Timestamp of when the user was registered.",
    )
