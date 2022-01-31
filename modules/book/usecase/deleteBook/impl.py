from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from modules.book.infrastructure.persistence.uow import BookPersistenceUnitOfWork

from .command import DeleteBookCommand


class DeleteBookUseCase(BaseUseCase[BookPersistenceUnitOfWork]):
    def __init__(self, uow: BookPersistenceUnitOfWork) -> None:
        self._uow = uow

    @async_transactional()
    async def invoke(self, command: DeleteBookCommand):
        book = await self.uow.repository.find_by_pk(command.book_id)
        if book:
            await self.uow.repository.delete(book)
