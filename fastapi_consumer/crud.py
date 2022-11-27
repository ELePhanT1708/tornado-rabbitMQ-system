from typing import List

from sqlalchemy.orm import Session

import models
import schemas


def get_request_by_id(db: Session, request_id: int) -> models.Request:
    return db.query(models.Request).filter(models.Request.id == request_id).first()


def get_requests_by_phone(db: Session, phone: str) -> List[models.Request]:
    return db.query(models.Request).filter(models.Request.email == phone).all()


def get_requests(db: Session, skip: int = 0, limit: int = 100) -> List[models.Request]:
    return db.query(models.Request).offset(skip).limit(limit).all()


def create_request(db: Session, item: schemas.Request):
    db_item = models.Request(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
