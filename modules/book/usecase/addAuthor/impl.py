from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from modules.book.domain.aggregate.model import Book
from modules.book.infrastructure.persistence.uow import BookPersistenceUnitOfWork

from .command import AddAuthorCommand


class AddAuthorUseCase(BaseUseCase[BookPersistenceUnitOfWork]):
    def __init__(self, uow: BookPersistenceUnitOfWork) -> None:
        self._uow = uow

    @async_transactional()
    async def invoke(self, command: AddAuthorCommand) -> Book:
        book: Book = await self.uow.repository.find_by_pk(command.book_id)
        book.add_author(command)

        # Publish Event

        return book
