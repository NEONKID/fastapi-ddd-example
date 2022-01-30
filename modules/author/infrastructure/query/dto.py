from dataclasses import dataclass
from sqlalchemy.ext.associationproxy import association_proxy
from typing import FrozenSet


@dataclass
class AuthorDTO:
    id: int
    first_name: str
    last_name: str
    age: int
    biography: str
    books: FrozenSet[int] = association_proxy("author_books", "book_id")
