from fastapi import APIRouter

from schemas import MessageSchema

router = APIRouter(
    tags=['items'],
    responses={404: {"description": "Page not found"}}
)


