from abc import ABC, abstractmethod


class Storage(ABC):
    """
    Абстрактный класс.
    """
    @abstractmethod
    def add(self, item: str, quantity: int) -> int:
        pass

    @abstractmethod
    def remove(self, item: str, quantity: int) -> int:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self) -> dict:
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass
