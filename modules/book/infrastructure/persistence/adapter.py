from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from common.protocols.persistence_adapter import PersistenceAdapter
from modules.book.domain.aggregate.model import Book, BookId

from .uow import BookPersistenceUnitOfWork


class BookPersistenceAdapter(BaseUseCase[BookPersistenceUnitOfWork], PersistenceAdapter[Book, BookId]):
    def __init__(self, uow: BookPersistenceUnitOfWork) -> None:
        self._uow = uow

    @async_transactional(read_only=True)
    async def find_by_id(self, _id: BookId) -> Book:
        return await self.uow.repository.find_by_pk(_id)

    @async_transactional()
    async def insert(self, domain: Book) -> Book:
        self.uow.repository.create(domain)
        return domain

    @async_transactional()
    async def delete_by_id(self, _id: BookId):
        entity = await self.uow.repository.find_by_pk(_id)
        if entity:
            await self.uow.repository.delete(entity)
