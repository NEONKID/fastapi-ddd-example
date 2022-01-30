from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from modules.author.domain.aggregate.model import Author
from modules.author.infrastructure.persistence.adapter import AuthorPersistenceAdapter
from modules.author.infrastructure.query.dto import AuthorDTO
from modules.author.infrastructure.query.uow import AuthorQueryUnitOfWork

from .command import NewAuthorCommand


class NewAuthorUseCase(BaseUseCase[AuthorQueryUnitOfWork]):
    def __init__(self, apa: AuthorPersistenceAdapter, uow: AuthorQueryUnitOfWork) -> None:
        self._uow = uow
        self.author_persistence_adapter = apa

    @async_transactional(read_only=True)
    async def invoke(self, command: NewAuthorCommand) -> AuthorDTO:
        domain = Author.new_author(command)
        save_author = await self.author_persistence_adapter.insert(domain)
        return await self.uow.repository.fetch_by_id(save_author.id)
