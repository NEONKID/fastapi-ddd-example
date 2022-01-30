from pydantic import BaseModel

from modules.author.domain.aggregate.id import AuthorId
from modules.book.domain.aggregate.id import BookId


class AddBookToAuthorCommand(BaseModel):
    book_id: BookId
    author_id: AuthorId
