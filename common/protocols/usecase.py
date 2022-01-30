from abc import abstractmethod
from pymfdata.common.usecase import BaseUseCase as PyMfUseCase


class BaseUseCase(PyMfUseCase):
    @abstractmethod
    def invoke(self):
        ...
