from pymfdata.common.usecase import BaseUseCase

from modules.author.infrastructure.persistence.adapter import AuthorPersistenceAdapter

from .command import AddBookToAuthorCommand


class AddBookToAuthorUseCase(BaseUseCase):
    def __init__(self, apa: AuthorPersistenceAdapter) -> None:
        self.author_persistence_adapter = apa

    async def invoke(self, command: AddBookToAuthorCommand):
        author = await self.author_persistence_adapter.find_by_id(command.author_id)
        author.add_book(command)

        await self.author_persistence_adapter.update(author)
