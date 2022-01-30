from pydantic import PositiveInt
from pydantic.dataclasses import dataclass

from core.pydantic import ConStr
from modules.author.domain.aggregate.id import AuthorId
from modules.book.domain.aggregate.id import BookId


class Title(ConStr):
    min_length = 1
    max_length = 100


class KoreanMoney(PositiveInt):
    gt = 1  # Min Number


class Isbn(ConStr):
    min_length = 10
    max_length = 10


class Page(PositiveInt):
    gt = 1


class Year(PositiveInt):
    gt = 1


@dataclass
class BookAuthor:
    book_id: BookId
    author_id: AuthorId
