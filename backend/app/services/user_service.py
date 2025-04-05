from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.user import User
from ..schemas.user import UserCreate
from passlib.context import CryptContext
import uuid

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user: UserCreate):
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or Email already exists",
        )

    hashed_password = pwd_context.hash(user.password)

    new_user = User(
        name=user.name,
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
        phone_number=user.phone_number,
        profile_pic_url=user.profile_pic_url,
        timezone=user.timezone,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(db: Session, user_id: uuid.UUID):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_all_users(db: Session):
    return db.query(User).all()

def delete_user(db: Session, user_id: uuid.UUID):
    user = get_user_by_id(db, user_id)
    db.delete(user)
    db.commit()

def get_user_by_username(username: str, db: Session):
    return db.query(User).filter(User.username == username).first()