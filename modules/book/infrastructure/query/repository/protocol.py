from abc import abstractmethod
from typing import Protocol

from modules.book.infrastructure.query.dto import BookDTO


class BookQueryRepository(Protocol):
    @abstractmethod
    async def fetch_by_title(self, title: str) -> BookDTO:
        ...

    @abstractmethod
    async def fetch_by_id(self, _id: int) -> BookDTO:
        ...
