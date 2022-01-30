from pydantic import BaseModel

from modules.book.domain.aggregate.id import BookId
from modules.author.domain.aggregate.id import AuthorId


class AddAuthorCommand(BaseModel):
    author_id: AuthorId
    book_id: BookId
