from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from common.protocols.persistence_adapter import PersistenceAdapter
from modules.author.domain.aggregate.model import Author, AuthorId

from .uow import AuthorPersistenceUnitOfWork


class AuthorPersistenceAdapter(BaseUseCase[AuthorPersistenceUnitOfWork], PersistenceAdapter[Author, AuthorId]):
    def __init__(self, uow: AuthorPersistenceUnitOfWork) -> None:
        self._uow = uow

    @async_transactional(read_only=True)
    async def find_by_id(self, _id: AuthorId) -> Author:
        return await self.uow.repository.find_by_pk(_id)

    @async_transactional()
    async def insert(self, domain: Author) -> Author:
        self.uow.repository.create(domain)
        return domain

    @async_transactional()
    async def delete_by_id(self, _id: AuthorId):
        author = self.uow.repository.find_by_pk(_id)
        if author:
            await self.uow.repository.delete(author)
