from typing import Optional

from common.protocols.event import BaseEvent
from modules.author.domain.aggregate.id import AuthorId
from modules.book.domain.aggregate.id import BookId
from modules.book.domain.event import AuthorAddedToBookDomainEvent

from .command import AddBookToAuthorCommand
from .impl import AddBookToAuthorUseCase


class AddBookToAuthorEventHandler(BaseEvent):
    def __init__(self, uc: AddBookToAuthorUseCase) -> None:
        self.uc = uc

    async def handle(self, param: AuthorAddedToBookDomainEvent = None) -> None:
        command = AddBookToAuthorCommand(book_id=BookId(param.book_id), author_id=AuthorId(param.author_id))
        await self.uc.invoke(command)
