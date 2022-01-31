from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from modules.author.domain.aggregate.model import Author
from modules.author.infrastructure.persistence.uow import AuthorPersistenceUnitOfWork

from .command import AddBookToAuthorCommand


class AddBookToAuthorUseCase(BaseUseCase[AuthorPersistenceUnitOfWork]):
    def __init__(self, uow: AuthorPersistenceUnitOfWork) -> None:
        self._uow = uow

    @async_transactional()
    async def invoke(self, command: AddBookToAuthorCommand) -> Author:
        author = await self.uow.repository.find_by_pk(command.author_id)
        author.add_book(command)

        return author
