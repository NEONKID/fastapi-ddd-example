from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from modules.book.infrastructure.query.dto import BookDTO
from modules.book.infrastructure.query.uow import BookQueryUnitOfWork


class FindBookByTitleUseCase(BaseUseCase[BookQueryUnitOfWork]):
    def __init__(self, uow: BookQueryUnitOfWork) -> None:
        self._uow = uow

    @async_transactional(read_only=True)
    async def invoke(self, title: str) -> BookDTO:
        return await self.uow.repository.fetch_by_title(title)
