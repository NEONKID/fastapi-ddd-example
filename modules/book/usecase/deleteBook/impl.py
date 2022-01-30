from pymfdata.common.usecase import BaseUseCase

from modules.book.infrastructure.persistence.adapter import BookPersistenceAdapter

from .command import DeleteBookCommand


class DeleteBookUseCase(BaseUseCase):
    def __init__(self, bpa: BookPersistenceAdapter) -> None:
        self.book_persistence_adapter = bpa

    async def invoke(self, command: DeleteBookCommand):
        await self.book_persistence_adapter.delete_by_id(command.book_id)
