from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..schemas.birthday import BirthdayCreate, BirthdayResponse
from ..services import birthday_service
from ..core.database import get_db
from uuid import UUID
from typing import List

router = APIRouter(prefix="/birthdays", tags=["Birthdays"])

@router.post("/", response_model=BirthdayResponse)
def create_birthday(birthday: BirthdayCreate, db: Session = Depends(get_db)):
    return birthday_service.create_birthday(db, birthday)

@router.get("/user/{user_id}", response_model=List[BirthdayResponse])
def get_birthdays_by_user(user_id: UUID, db: Session = Depends(get_db)):
    return birthday_service.get_birthdays_by_user(db, user_id)

@router.get("/{birthday_id}", response_model=BirthdayResponse)
def get_birthday(birthday_id: UUID, db: Session = Depends(get_db)):
    return birthday_service.get_birthday_by_id(db, birthday_id)

@router.put("/{birthday_id}", response_model=BirthdayResponse)
def update_birthday_api(birthday_id: UUID, birthday_update: BirthdayCreate, db: Session = Depends(get_db)):
    return birthday_service.update_birthday(db, birthday_id, birthday_update)

@router.delete("/{birthday_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_birthday_api(birthday_id: UUID, db: Session = Depends(get_db)):
    birthday_service.delete_birthday(db, birthday_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)