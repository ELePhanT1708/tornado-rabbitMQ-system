from pydantic import BaseModel


class Request(BaseModel):
    surname: str
    name: str
    parent_name: str | None = None
    phone: str
    request_body: str

    class Config:
        orm_mode = True



