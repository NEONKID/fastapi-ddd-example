from pydantic import BaseModel


class AuthorAddedToBookDomainEvent(BaseModel):
    book_id: int
    author_id: int
