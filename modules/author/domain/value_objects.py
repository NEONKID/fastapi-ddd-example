from pydantic import PositiveInt, constr
from pydantic.dataclasses import dataclass

from core.pydantic import ConStr
from modules.author.domain.aggregate.id import AuthorId
from modules.book.domain.aggregate.id import BookId


class Age(PositiveInt):
    gt = 1


class Biography(ConStr):
    min_length: 1
    max_length: 3000


@dataclass
class Name:
    first_name: constr(min_length=1, max_length=100)
    last_name: constr(min_length=1, max_length=100)

    # Sqlalchemy composite callback func
    def __composite_values__(self):
        return self.first_name, self.last_name


@dataclass
class AuthorBook:
    author_id: AuthorId
    book_id: BookId
