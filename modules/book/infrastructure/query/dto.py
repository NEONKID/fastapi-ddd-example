from dataclasses import dataclass
from sqlalchemy.ext.associationproxy import association_proxy
from typing import FrozenSet


@dataclass
class BookDTO:
    id: int
    title: str
    isbn: str
    pages: int
    authors: FrozenSet[int] = association_proxy("book_authors", "author_id")
