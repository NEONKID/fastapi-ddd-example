from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Path

from container import Container
from modules.author.domain.aggregate.id import AuthorId
from modules.book.domain.aggregate.id import BookId
from modules.book.usecase import router
from modules.book.usecase.addAuthor.impl import AddAuthorUseCase

from .command import AddAuthorCommand


@router.post(path="/{id}/authors/{author_id}", name="Add Author for Book")
@inject
async def add_author(id: BookId = Path(..., title="Book ID"), author_id: AuthorId = Path(..., title="Author ID"),
                     uc: AddAuthorUseCase = Depends(Provide[Container.add_author_use_case])):
    await uc.invoke(AddAuthorCommand(book_id=id, author_id=author_id))
    return "OK"
