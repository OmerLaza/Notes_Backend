from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    salt = "FAKESALT"

    # TODO: make this semi sucure
    fake_hashed_password = user.password + salt + "notreallyhashed"
    db_user = models.User(email=user.email,
                          hashed_password=fake_hashed_password,
                          password_salt=salt)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()


def create_user_note(db: Session, note: schemas.NoteCreate, user_id: int):
    db_note = models.Note(**note.dict(), owner_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def get_user_notes(db: Session, owner_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Note).filter(models.Note.owner_id == owner_id).offset(skip).limit(limit).all()
