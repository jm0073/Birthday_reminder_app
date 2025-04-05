from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..schemas.user import UserCreate, UserResponse
from ..services import user_service
from ..core.database import get_db
from typing import List
from uuid import UUID

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: UUID, db: Session = Depends(get_db)):
    return user_service.get_user_by_id(db, user_id)

@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: UUID, db: Session = Depends(get_db)):
    user_service.delete_user(db, user_id)