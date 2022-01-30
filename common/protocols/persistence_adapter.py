from abc import abstractmethod
from typing import Protocol

from . import D, I


class PersistenceAdapter(Protocol[D, I]):
    @abstractmethod
    def find_by_id(self, _id: I) -> D:
        ...

    @abstractmethod
    def insert(self, domain: D) -> D:
        ...

    @abstractmethod
    def delete_by_id(self, _id: I):
        ...
