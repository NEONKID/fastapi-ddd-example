from pymfdata.rdb.connection import AsyncEngine
from pymfdata.rdb.usecase import AsyncSQLAlchemyUnitOfWork

from modules.author.infrastructure.query.repository.impl import AuthorAlchemyRepository, AuthorQueryRepository


class AuthorQueryUnitOfWork(AsyncSQLAlchemyUnitOfWork):
    def __init__(self, engine: AsyncEngine) -> None:
        super().__init__(engine)

    async def __aenter__(self):
        await super().__aenter__()

        self.repository: AuthorQueryRepository = AuthorAlchemyRepository(self.session)
