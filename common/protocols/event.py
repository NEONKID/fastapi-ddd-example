from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Type, Union


class BaseEvent(ABC):
    @abstractmethod
    async def handle(self, param: Union[Type[BaseModel], None] = None) -> None:
        ...
