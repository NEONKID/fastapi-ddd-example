from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Path
from starlette import status

from container import Container
from modules.book.domain.aggregate.id import BookId
from modules.book.usecase import router
from modules.book.usecase.deleteBook.impl import DeleteBookUseCase, DeleteBookCommand


@router.delete(path="/{id}", name="Delete Book", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_book(id: BookId = Path(..., title="Book ID"),
                      uc: DeleteBookUseCase = Depends(Provide[Container.delete_book_use_case])):
    await uc.invoke(DeleteBookCommand(book_id=id))
