from dataclasses import asdict
from pymfdata.rdb.mapper import mapper_registry
from sqlalchemy.orm import backref, relationship

from common.protocols.model_mapper import ModelMapper
from modules.book.domain.aggregate.model import Book, BookId, BookAuthor
from persistence.book.entity import BookEntity, BookAuthorEntity


class BookMapper(ModelMapper[Book, BookEntity]):
    @staticmethod
    def map_to_domain_entity(model: BookEntity) -> Book:
        return Book(
            id=BookId(model.id),
            title=model.title,
            isbn=model.isbn,
            pages=model.pages,
            price=model.price,
            publication_year=model.publication_year,
            authors=list(map(lambda entity: entity.id, model.authors))
        )

    @staticmethod
    def map_to_persistence_entity(model: Book) -> BookEntity:
        return BookEntity(**asdict(model))


def start_mapper():
    t = BookEntity.__table__
    rt = BookAuthorEntity.__table__

    mapper_registry.map_imperatively(Book, t, properties={
        'authors': relationship(BookAuthor, backref=backref("book"), lazy='joined')
    })
    mapper_registry.map_imperatively(BookAuthor, rt, properties={
        'books': relationship(Book, backref=backref("author", cascade="all, delete-orphan"), lazy='joined')
    })
