from classes.abstract_storage import Storage
from exceptions import NotEnoughProduct, TooManyDifferentProducts, NotEnoughSpase


class BaseStorage(Storage):
    """
    Базовый класс, реализующий основную логику движения товара на объекте.
    Наследуется от абстрактного класса.
    """

    def __init__(self, items: dict[str: int], capacity: int, commodity_shelves: int = 100):
        self.__items = items
        self.__capacity = capacity - sum([item for item in self.__items.values()])
        self.__commodity_shelves = commodity_shelves

    def add(self, item: str, quantity: int) -> int:
        """
        Метод добавления товаров в объекте с учётом соотнесения запроса и наличия,
        а также наличия свободных полок и места на объекте.
        :param item: название товара,
        :param quantity: количество товара,
        :return: остаток не вместившегося товара -> int.
        """
        if self.get_unique_items_count() >= self.__commodity_shelves and item not in self.__items.keys():
            raise TooManyDifferentProducts
        elif self.__capacity <= 0:
            raise NotEnoughSpase

        if self.get_free_space() >= quantity:
            return self.__add_all_items(item, quantity)
        else:
            return self.__add_part_items(item, quantity)

    def __add_all_items(self, item: str, quantity: int) -> int:
        """
        Вспомогательный метод для метода "add", принимает и возвращает те же параметры и данные.
        Добавляет все поставленные товары с учётом ассортимента, уменьшая место на объекте.
        """
        if item in self.__items:
            self.__items[item] += quantity
            self.__capacity -= quantity
            return 0
        else:
            self.__items[item] = quantity
            self.__capacity -= quantity
            return 0

    def __add_part_items(self, item: str, quantity: int) -> int:
        """
        Вспомогательный метод для метода "add", принимает и возвращает те же параметры и данные.
        Добавляет часть поставленных товаров с учётом ассортимента, уменьшая место на объекте.
        """
        if item in self.__items:
            self.__items[item] += self.__capacity
            remains = self.__remains(quantity)
            self.__capacity = 0
            return remains
        else:
            self.__items[item] = self.__capacity
            remains = self.__remains(quantity)
            self.__capacity = 0
            return remains

    def remove(self, item: str, quantity: int) -> int:
        """
        Метод уменьшения товаров в объекте с учётом соотнесения запроса и наличия.
        :param item: название товара,
        :param quantity: количество товара,
        :return: сколько товара не хватило для удовлетворения запроса -> int.
        """
        if item not in self.__items:
            raise NotEnoughProduct

        if self.__items[item] >= quantity:
            return self.__remove_all_items(item, quantity)
        else:
            return self.__remove_part_items(item, quantity)

    def __remove_all_items(self, item: str, quantity: int) -> int:
        """
        Вспомогательный метод для метода "remove", принимает и возвращает те же параметры и данные.
        Уменьшает количество товара в соответствии с запросом, добавляя место на объекте и если
        израсходован весь товарный остаток - удаляет позицию ассортимента.
        """
        self.__items[item] -= quantity
        if self.__items[item] == 0:
            self.__items.pop(item)
        self.__capacity += quantity
        return 0

    def __remove_part_items(self, item: str, quantity: int) -> int:
        """
        Вспомогательный метод для метода "remove", принимает и возвращает те же параметры и данные.
        Уменьшает количество товара до нуля, удаляя позицию ассортимента, добавляя место на объекте
        и фиксируя не удовлетворённую часть запрошенного товара.
        """
        self.__capacity += self.__items[item]
        shortage = self.__shortage(quantity, item)
        self.shortage = shortage
        self.__items.pop(item)
        return shortage

    def get_free_space(self) -> int:
        """
        Метод проверки свободного места на объекте.
        :return: число свободных мест -> int.
        """
        return self.__capacity

    def get_items(self) -> dict[str: int]:
        """
        Метод получения ассортимента товаров на объекте.
        :return: товары -> dict.
        """
        return self.__items

    def get_unique_items_count(self) -> int:
        """
        Метод получения числа уникальных товаров на объекте.
        :return: видовое разнообразие товаров -> int.
        """
        return len(set(self.__items.keys()))

    def __remains(self, quantity):
        """
        Метод получения остатка поставленного товара, не вошедшего в объект в связи с отсутствием свободных мест.
        Используется методом self.add.
        :param quantity: число поставленного товара.
        :return: остаток не вместившегося товара -> int
        """
        return quantity - self.get_free_space()

    def __shortage(self, quantity, item):
        """
        Метод получения не удовлетворённого спроса при условии частичного наличия товара на объекте.
        Используется методом self.remove.
        :param quantity: число запрошенного товара.
        :return: сколько товара не хватило для удовлетворения спроса -> int
        """
        return quantity - self.__items[item]
