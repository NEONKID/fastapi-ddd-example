from pymfdata.rdb.mapper import Base
from sqlalchemy import BigInteger, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, composite
from typing import List, Union

from modules.author.domain.value_objects import Name


class AuthorBookEntity(Base):
    __tablename__ = 'author_book'

    author_id: Union[int, Column] = Column(ForeignKey('author.id', ondelete="RESTRICT"), primary_key=True)
    book_id: Union[int, Column] = Column(BigInteger, primary_key=True)


class AuthorEntity(Base):
    __tablename__ = 'author'

    id: Union[int, Column] = Column(BigInteger, primary_key=True)
    first_name: Union[str, Column] = Column(String(100), nullable=False)
    last_name: Union[str, Column] = Column(String(100), nullable=False)
    age: Union[int, Column] = Column(Integer, nullable=False)
    biography: Union[str, Column] = Column(String(3000), nullable=True)

    # If viewonly set false, comment start_mapper for AuthorEntity, because two object conflict
    r_book_ids = relationship(AuthorBookEntity, viewonly=True, lazy='joined')

    # If use orm_mode for Pydantic BaseModel
    name = composite(Name, first_name, last_name)

    @property
    def book_ids(self) -> List[AuthorBookEntity]:
        return self.r_book_ids

    @book_ids.setter
    def book_ids(self, books: List[int]):
        self.r_book_ids = list(map(lambda _id: AuthorBookEntity(author_id=self.id, book_id=_id), books))
