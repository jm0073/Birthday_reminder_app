from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.birthday import Birthday
from ..schemas.birthday import BirthdayCreate
import uuid

def create_birthday(db: Session, birthday: BirthdayCreate):
    new_birthday = Birthday(**birthday.dict())
    db.add(new_birthday)
    db.commit()
    db.refresh(new_birthday)
    return new_birthday

def get_birthdays_by_user(db: Session, user_id: uuid.UUID):
    return db.query(Birthday).filter(Birthday.user_id == user_id).all()

def get_birthday_by_id(db: Session, birthday_id: uuid.UUID):
    birthday = db.query(Birthday).filter(Birthday.id == birthday_id).first()
    if not birthday:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Birthday not found")
    return birthday

def update_birthday(db: Session, birthday_id: uuid.UUID, birthday_update: BirthdayCreate):
    birthday = db.query(Birthday).filter(Birthday.id == birthday_id).first()
    if not birthday:
        raise HTTPException(status_code=404, detail="Birthday not found")

    for key, value in birthday_update.dict().items():
        setattr(birthday, key, value)

    db.commit()
    db.refresh(birthday)
    return birthday

def delete_birthday(db: Session, birthday_id: uuid.UUID):
    birthday = db.query(Birthday).filter(Birthday.id == birthday_id).first()
    if not birthday:
        raise HTTPException(status_code=404, detail="Birthday not found")

    db.delete(birthday)
    db.commit()
    return {"detail": "Birthday deleted successfully"}