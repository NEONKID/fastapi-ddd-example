from pymfdata.rdb.repository import AsyncRepository, AsyncSession

from modules.author.domain.aggregate.model import Author


class AuthorRepository(AsyncRepository[Author, int]):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
