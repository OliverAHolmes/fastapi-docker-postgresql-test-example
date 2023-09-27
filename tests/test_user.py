from fastapi import status
from fastapi.testclient import TestClient
from main import app
from db import SessionLocal
from models import User

client = TestClient(app)


def test_create_user():
    # Creating a new user
    response = client.post(
        "/users/",
        json={
            "username": "testuser",
            "email": "test@email.com",
            "full_name": "Test User",
            "hashed_password": "hashedpassword123",  # In a real-world scenario, this should be hashed
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "User created successfully"
    user_id = response.json()["user_id"]

    # Validate database
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    assert db_user is not None
    db.close()


def test_get_user_by_id():
    db = SessionLocal()
    db_user = db.query(User).first()
    user_id = db_user.id
    db.close()

    response = client.get(f"/users/{user_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == user_id


def test_get_user_by_id_not_found():
    response = client.get("/users/9999")  # Assuming ID 9999 does not exist in the DB
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_update_user_by_id():
    db = SessionLocal()
    db_user = db.query(User).first()
    user_id = db_user.id
    db.close()

    response = client.put(
        f"/users/{user_id}",
        json={"username": "updateduser", "email": "updated@email.com"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "User updated successfully"


def test_delete_user_by_id():
    db = SessionLocal()
    db_user = db.query(User).first()
    user_id = db_user.id
    db.close()

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "User deleted"}

    # Validate the user is deleted
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    db.close()
    assert db_user is None


def test_delete_user_by_id_not_found():
    response = client.delete("/users/9999")  # Assuming ID 9999 does not exist in the DB
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User not found"}
