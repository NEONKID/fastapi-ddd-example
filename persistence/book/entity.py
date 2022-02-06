from pymfdata.rdb.mapper import Base
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from typing import List, Union


class BookAuthorEntity(Base):
    __tablename__ = 'book_author'

    book_id = Column(ForeignKey("book.id", ondelete="RESTRICT"), primary_key=True)
    author_id = Column(BigInteger, primary_key=True)


class BookEntity(Base):
    __tablename__ = 'book'

    id: Union[int, Column] = Column(BigInteger, primary_key=True)
    title: Union[str, Column] = Column(String(100), nullable=False)
    isbn: Union[str, Column] = Column(String(10), nullable=False, unique=True)
    pages: Union[int, Column] = Column(Integer, nullable=False)
    price: Union[int, Column] = Column(BigInteger, nullable=False)
    publication_year: Union[int, Column] = Column(Integer, nullable=False)

    # If viewonly set false, comment start_mapper for BookEntity, because two object conflict
    r_authors = relationship(BookAuthorEntity, viewonly=True, lazy='joined')

    @property
    def authors(self) -> List[BookAuthorEntity]:
        return self.r_authors

    @authors.setter
    def authors(self, authors: List[int]):
        self.r_authors = list(map(lambda _id: BookAuthorEntity(book_id=self.id, author_id=_id), authors))
