from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from pydantic import BaseModel, constr, Field, PositiveInt
from starlette import status
from typing import Optional

from container import Container
from modules.author.domain.value_objects import Name
from modules.author.usecase import router
from .impl import NewAuthorCommand, NewAuthorUseCase


# application/json request schema
class NewAuthorRequest(BaseModel):
    first_name: constr(min_length=1, max_length=100) = Field(title="Author First Name")
    last_name: constr(min_length=1, max_length=100) = Field(title="Author Last Name")
    age: PositiveInt = Field(title="Author Age")
    biography: Optional[constr(min_length=1, max_length=3000)] = Field(title="Author Biography")


@router.post(path='', name="New Author", status_code=status.HTTP_201_CREATED)
@inject
async def new_author(command: NewAuthorRequest,
                     uc: NewAuthorUseCase = Depends(Provide[Container.new_author_use_case])):
    author = await uc.invoke(
        NewAuthorCommand(
            name=Name(first_name=command.first_name, last_name=command.last_name),
            age=command.age,
            biography=command.biography
        )
    )
    return author.id
