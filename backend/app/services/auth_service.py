from sqlalchemy.orm import Session

from backend.app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from backend.app.models.user import User
from backend.app.schemas.user import UserRegister


def register_user(db: Session, user: UserRegister) -> User:
    existing_user = (
        db.query(User)
        .filter(
            (User.email == user.email)
            | (User.username == user.username)
        )
        .first()
    )

    if existing_user:
        raise ValueError("User already exists")

    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise ValueError("Invalid email or password")

    if not verify_password(password, user.hashed_password):
        raise ValueError("Invalid email or password")

    token = create_access_token(
        {
            "sub": user.email,
            "user_id": user.id,
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }