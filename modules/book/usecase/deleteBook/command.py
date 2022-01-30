from pydantic import BaseModel, Field

from modules.book.domain.aggregate.model import BookId


class DeleteBookCommand(BaseModel):
    book_id: BookId = Field(title="Book ID")
