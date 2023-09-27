"""
FastAPI router for handling User operations.

This module contains endpoints for creating, retrieving, updating, and deleting users.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db import SessionLocal
from models import User

router = APIRouter(prefix="/users")


class UserUpdate(BaseModel):
    username: str
    email: str


@router.post("/")
async def create_user(user: User):
    """
    Create a new user.

    Parameters:
        user (User): The user to create.

    Returns:
        dict: Confirmation message and user_id of the created user.
    """

    session = SessionLocal()

    db_user = User(**user.dict())
    session.add(db_user)

    session.commit()
    user_id = db_user.id

    session.close()

    return {"message": "User created successfully", "user_id": user_id}


@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    """
    Retrieve a specific user by its ID.

    Parameters:
        user_id (int): The ID of the user to retrieve.

    Returns:
        User: The user object if found.
    """
    session = SessionLocal()
    db_user = session.query(User).filter(User.id == user_id).first()
    session.close()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@router.put("/{user_id}")
async def update_user_by_id(user_id: int, user: UserUpdate):
    """
    Update a specific user by its ID.

    Parameters:
        user_id (int): The ID of the user to update.
        user (User): The updated user data.

    Returns:
        dict: Confirmation message.
    """
    session = SessionLocal()
    db_user = session.query(User).filter(User.id == user_id).first()

    if db_user is None:
        session.close()
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user.dict().items():
        setattr(db_user, key, value)

    session.commit()
    session.close()

    return {"message": "User updated successfully"}


@router.delete("/{user_id}")
async def delete_user_by_id(user_id: int):
    """
    Delete a specific user by its ID.

    Parameters:
        user_id (int): The ID of the user to delete.

    Returns:
        dict: Confirmation message.
    """
    session = SessionLocal()
    db_user = session.query(User).filter(User.id == user_id).first()

    if db_user is None:
        session.close()
        raise HTTPException(status_code=404, detail="User not found")

    session.delete(db_user)
    session.commit()
    session.close()

    return {"message": "User deleted"}
