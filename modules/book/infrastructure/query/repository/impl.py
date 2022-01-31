from pymfdata.rdb.repository import AsyncSession, BaseAsyncRepository
from sqlalchemy import select

from modules.book.infrastructure.query.dto import BookDTO
from modules.book.infrastructure.query.repository.protocol import BookQueryRepository


class BookAlchemyRepository(BaseAsyncRepository, BookQueryRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def fetch_by_title(self, title: str) -> BookDTO:
        stmt = select(BookDTO).where(BookDTO.title == title)

        result = await self.session.execute(stmt)
        return result.unique().scalars().fetchall()

    async def fetch_by_id(self, _id: int) -> BookDTO:
        stmt = select(BookDTO).where(BookDTO.id == _id)

        result = await self.session.execute(stmt)
        return result.unique().scalars().one_or_none()
