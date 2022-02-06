from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from core.fastapi.event.dispatcher import EventDispatcher
from core.fastapi.event.handler import event_handler
from modules.author.usecase.addBookToAuthor.event_handler import AddBookToAuthorEventHandler
from modules.book.domain.aggregate.model import Book
from modules.book.domain.event import AuthorAddedToBookDomainEvent
from modules.book.infrastructure.persistence.uow import BookPersistenceUnitOfWork

from .command import AddAuthorCommand


class AddAuthorUseCase(BaseUseCase[BookPersistenceUnitOfWork]):
    def __init__(self, uow: BookPersistenceUnitOfWork, event: AddBookToAuthorEventHandler) -> None:
        self._event = event
        self._uow = uow

    # Transaction order
    @async_transactional()
    @EventDispatcher()
    async def invoke(self, command: AddAuthorCommand) -> Book:
        book: Book = await self.uow.repository.find_by_pk(command.book_id)
        book.add_author(command)

        # Publish Event
        await event_handler.store(event=self._event,
                                  param=AuthorAddedToBookDomainEvent(book_id=command.book_id,
                                                                     author_id=command.author_id))
        return book
