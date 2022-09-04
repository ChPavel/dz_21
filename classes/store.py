from classes.base_storage import BaseStorage


class Store(BaseStorage):
    """
    Класс склада, наследуется от базового класса.
    """
    def __init__(self, items: dict, capacity: int = 100):
        super().__init__(items, capacity)
