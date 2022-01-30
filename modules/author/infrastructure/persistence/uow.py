from pymfdata.rdb.connection import AsyncEngine
from pymfdata.rdb.usecase import AsyncSQLAlchemyUnitOfWork

from persistence.author.repository import AuthorRepository


class AuthorPersistenceUnitOfWork(AsyncSQLAlchemyUnitOfWork):
    def __init__(self, engine: AsyncEngine) -> None:
        super().__init__(engine)

    async def __aenter__(self) -> None:
        await super().__aenter__()

        self.repository = AuthorRepository(self.session)
