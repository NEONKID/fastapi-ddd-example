from pymfdata.rdb.connection import AsyncEngine
from pymfdata.rdb.usecase import AsyncSQLAlchemyUnitOfWork

from modules.book.infrastructure.query.repository.impl import BookAlchemyRepository, BookQueryRepository


class BookQueryUnitOfWork(AsyncSQLAlchemyUnitOfWork):
    def __init__(self, engine: AsyncEngine) -> None:
        super().__init__(engine)

    async def __aenter__(self):
        await super().__aenter__()

        self.repository: BookQueryRepository = BookAlchemyRepository(self.session)
