from pymfdata.rdb.mapper import mapper_registry
from sqlalchemy.orm import composite

from common.protocols.model_mapper import ModelMapper
from modules.author.domain.aggregate.model import Author
from modules.author.domain.value_objects import Name, AuthorBook
from persistence.author.entity import AuthorEntity, AuthorBookEntity, relationship


# Classical Mapper (Traditional)
class AuthorMapper(ModelMapper[Author, AuthorEntity]):
    @staticmethod
    def map_to_domain_entity(model: AuthorEntity) -> Author:
        return Author(
            id=model.id,
            name=Name(first_name=model.first_name, last_name=model.last_name),
            age=model.age,
            biography=model.biography,
            book_ids=list(map(lambda entity: entity.id, model.book_ids))
        )

    @staticmethod
    def map_to_persistence_entity(model: Author) -> AuthorEntity:
        return AuthorEntity(
            id=model.id,
            first_name=model.name.first_name,
            last_name=model.name.last_name,
            age=model.age,
            biography=model.biography,
            book_ids=model.book_ids
        )


# SQLAlchemy Mapper (only sqlalchemy)
def start_mapper():
    t = AuthorEntity.__table__
    rt = AuthorBookEntity.__table__

    mapper_registry.map_imperatively(Author, t, properties={
        'name': composite(Name, t.c.first_name, t.c.last_name),
        'book_ids': relationship(AuthorBook, lazy='joined')
    })
    mapper_registry.map_imperatively(AuthorBook, rt)
