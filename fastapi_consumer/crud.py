from typing import List

from sqlalchemy.orm import Session

import models
import schemas
from db import SessionLocal




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_request_by_id(db: Session, request_id: int) -> models.Request:
    return db.query(models.Request).filter(models.Request.id == request_id).first()


def get_requests_by_phone(db: Session, phone: str) -> List[models.Request]:
    return db.query(models.Request).filter(models.Request.phone == phone).all()


def get_requests(db: Session, skip: int = 0, limit: int = 100) -> List[models.Request]:
    return db.query(models.Request).offset(skip).limit(limit).all()


def create_request(item: schemas.Request, db: Session = SessionLocal()):
    db_item = models.Request(**item)
    print("Proccessing: ", item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
