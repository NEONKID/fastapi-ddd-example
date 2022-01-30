from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from modules.book.domain.aggregate.model import Book
from modules.book.usecase.newBook.command import NewBookCommand
from modules.book.infrastructure.persistence.adapter import BookPersistenceAdapter
from modules.book.infrastructure.query.dto import BookDTO
from modules.book.infrastructure.query.uow import BookQueryUnitOfWork


class NewBookUseCase(BaseUseCase[BookQueryUnitOfWork]):
    def __init__(self, bpa: BookPersistenceAdapter, uow: BookQueryUnitOfWork) -> None:
        self._uow = uow
        self.book_persistence_adapter = bpa

    @async_transactional(read_only=True)
    async def invoke(self, command: NewBookCommand) -> BookDTO:
        save_book = await self.book_persistence_adapter.insert(Book.new_book(command))
        return await self.uow.repository.fetch_by_id(save_book.id)
