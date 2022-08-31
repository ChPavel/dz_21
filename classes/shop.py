from classes.base_storage import BaseStorage


class Shop(BaseStorage):
    """
    Класс магазина, наследуется от базового класса.
    """
    def __init__(self, items: dict, capacity: int = 20, commodity_shelves: int = 5):
        super().__init__(items, capacity, commodity_shelves)


