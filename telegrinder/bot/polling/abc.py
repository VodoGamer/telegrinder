import typing
from abc import ABC, abstractmethod

from telegrinder.model import Raw
from telegrinder.types import Update


class ABCPolling(ABC):
    offset: int

    @abstractmethod
    async def get_updates(self) -> list[Raw]:
        pass

    @abstractmethod
    async def listen(self) -> typing.AsyncGenerator[list[Update], None]:
        yield []

    @abstractmethod
    def stop(self) -> None:
        pass
