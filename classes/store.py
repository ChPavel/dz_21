from classes.base_storage import BaseStorage


class Store(BaseStorage):
    """
    Класс склада, наследуется от базового класса.
    """
    def __init__(self, items: dict, capacity: int = 100):
        super().__init__(items, capacity)
    # Вариант:
    # def add(self, item: str, quantity: int):
    #     if self.get_unique_items_count() >= 100:
    #         raise TooManyDifferentProducts
    #
    #     return super().add(item, quantity)

