from dataclasses import dataclass, field
from typing import List

from modules.book.domain.value_objects import Title, Isbn, Page, KoreanMoney, Year, BookAuthor
from modules.book.usecase.addAuthor.command import AddAuthorCommand
from modules.book.usecase.newBook.command import NewBookCommand

from .id import BookId


@dataclass
class Book:
    id: BookId
    title: Title
    isbn: Isbn
    pages: Page
    price: KoreanMoney
    publication_year: Year
    authors: List[BookAuthor] = field(default_factory=list)

    @staticmethod
    def new_book(command: NewBookCommand) -> 'Book':
        return Book(id=BookId.next_id(), **command.dict())

    def add_author(self, command: AddAuthorCommand):
        self.authors.append(BookAuthor(book_id=self.id, author_id=command.author_id))
