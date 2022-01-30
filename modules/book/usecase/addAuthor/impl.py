from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from modules.book.domain.aggregate.model import Book
from modules.book.infrastructure.persistence.adapter import BookPersistenceAdapter
from modules.book.infrastructure.query.dto import BookDTO
from modules.book.infrastructure.query.uow import BookQueryUnitOfWork

from .command import AddAuthorCommand


class AddAuthorUseCase(BaseUseCase[BookQueryUnitOfWork]):
    def __init__(self, bpa: BookPersistenceAdapter, uow: BookQueryUnitOfWork) -> None:
        self._uow = uow
        self.book_persistence_adapter = bpa

    @async_transactional(read_only=True)
    async def invoke(self, command: AddAuthorCommand) -> BookDTO:
        async with self.book_persistence_adapter.uow:
            book: Book = await self.book_persistence_adapter.uow.repository.find_by_pk(command.book_id)
            book.add_author(command)

            # Boilerplate
            await self.book_persistence_adapter.uow.commit()
            await self.book_persistence_adapter.uow.refresh(book)

        # Publish Event

        return await self.uow.repository.fetch_by_id(book.id)
