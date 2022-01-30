from pymfdata.rdb.mapper import mapper_registry
from sqlalchemy.orm import relationship

from persistence.book.entity import BookEntity, BookAuthorEntity
from .dto import BookDTO


def start_mapper():
    t = BookEntity.__table__

    mapper_registry.map_imperatively(BookDTO, t, properties={
        'book_authors': relationship(BookAuthorEntity, viewonly=True, lazy='joined')
    })
