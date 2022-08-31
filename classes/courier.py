from classes.abstract_storage import Storage
from classes.request import Request


class Courier:
    """
    Класс курьер, реализует логику перемещения товара.
    """
    def __init__(self, request: Request, storages: dict[str, Storage]):
        self.__request = request
        self.result_remove = 0
        self.result_add = 0

        if self.__request.start_point in storages:
            self.__from = storages[self.__request.start_point]

        if self.__request.end_point in storages:
            self.__to = storages[self.__request.end_point]

    def move(self) -> None:
        """
        Метод изменения количества товара на складе и в магазине с учётом возможных не стыковок между наличием и
        запрашиваемым количеством с их фиксацией в self.result_remove и self.result_add (последнее ещё не использовано).
        """
        self.result_remove = self.__from.remove(
            item=self.__request.product,
            quantity=self.__request.amount
        )
        if self.result_remove != 0:
            print(f'Курьер забрал только {self.__request.amount - self.result_remove} {self.__request.product} '
                  f'из {self.__request.start_point}, так как там больше не было!')
        else:
            print(f'Курьер забрал {self.__request.amount} {self.__request.product} из {self.__request.start_point}.')

        self.result_add = self.__to.add(
            item=self.__request.product,
            quantity=self.__request.amount - self.result_remove
        )
        if self.result_add != 0:
            print(f'Курьер доставил только {self.__request.amount - self.result_add} {self.__request.product} '
                  f'в {self.__request.end_point}, так как для большего нет места!')
            self.__from.add(
                item=self.__request.product,
                quantity=self.result_add
            )
            print(f'Курьер вернул обратно в {self.__request.start_point} {self.result_add} {self.__request.product}!')
        else:
            print(f'Курьер доставил {self.__request.amount - self.result_remove} {self.__request.product} '
                  f'в {self.__request.end_point}.')

    def again_the_authorities_messed_up(self) -> None:
        """
        Метод определяющий поведение курьера при исключениях.
        """
        items = self.__from.get_items().get(self.__request.product)
        if items is not None and self.result_remove == 0:
            self.__from.add(
                item=self.__request.product,
                quantity=self.__request.amount
            )
        else:
            self.__from.add(
                item=self.__request.product,
                quantity=self.__request.amount - self.result_remove
            )
        print(f'Курьер вернулся в {self.__request.start_point} и всех обматерил!!!')
