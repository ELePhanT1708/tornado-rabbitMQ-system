from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    surname = Column(String)
    name = Column(String)
    parent_name = Column(String, default=True)
    phone = Column(Integer)
    request_body = Column(String)

    def __str__(self):
        return f'Обращение №{self.id} from {self.surname} {self.name} по поводу :' \
               f'{self.request_body[:20]} '

