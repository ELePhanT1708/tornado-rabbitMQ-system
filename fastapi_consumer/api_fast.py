import asyncio

from fastapi import Depends, FastAPI
from fastapi.logger import logger
from sqlalchemy.orm import Session

import schemas
import crud
import models
from db import engine
from pika_client import PikaClient

models.Request.metadata.create_all(bind=engine)


class FooApp(FastAPI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pika_client = PikaClient()  # self.log_incoming_message

    @classmethod
    def log_incoming_message(cls, message: dict):
        """Method to do something meaningful with the incoming message"""
        logger.info('Here we got incoming message %s', message)


foo_app = FooApp()


@foo_app.on_event('startup')
async def startup():
    loop = asyncio.get_running_loop()
    task = loop.create_task(foo_app.pika_client.consume(loop))
    await task


# @foo_app.post("/save-request/", response_model=schemas.Request)
# async def create_request(request, db: Session = Depends(get_db)):
#     db_request = crud.create_request(db, request)
#     return db_request


@foo_app.get("/get-requests/", response_model=list[schemas.Request])
def get_requests(skip: int = 0, limit: int = 100, db: Session = Depends(crud.get_db)):
    users = crud.get_requests(db, skip=skip, limit=limit)
    return users


@foo_app.get("/")
async def root():
    return {"message": "Hello World"}
