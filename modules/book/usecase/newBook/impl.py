from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from modules.book.domain.aggregate.model import Book
from modules.book.usecase.newBook.command import NewBookCommand
from modules.book.infrastructure.persistence.uow import BookPersistenceUnitOfWork


class NewBookUseCase(BaseUseCase[BookPersistenceUnitOfWork]):
    def __init__(self, uow: BookPersistenceUnitOfWork) -> None:
        self._uow = uow

    @async_transactional()
    async def invoke(self, command: NewBookCommand) -> Book:
        book = Book.new_book(command)
        self.uow.repository.create(book)
        return book
