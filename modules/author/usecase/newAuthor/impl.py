from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from modules.author.domain.aggregate.model import Author
from modules.author.infrastructure.persistence.uow import AuthorPersistenceUnitOfWork

from .command import NewAuthorCommand


class NewAuthorUseCase(BaseUseCase[AuthorPersistenceUnitOfWork]):
    def __init__(self, uow: AuthorPersistenceUnitOfWork) -> None:
        self._uow = uow

    @async_transactional()
    async def invoke(self, command: NewAuthorCommand) -> Author:
        author = Author.new_author(command)
        self.uow.repository.create(author)
        return author
