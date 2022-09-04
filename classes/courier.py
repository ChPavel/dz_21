from classes.abstract_storage import Storage
from classes.request import Request


class Courier:
    """
    Класс курьер, реализует логику перемещения товара и выводимых сообщений.
    """

    def __init__(self, request: Request, storages: dict[str, Storage]):
        self.__request = request
        self.result_remove = 0
        self.result_add = 0

        if self.__request.start_point in storages:
            self.__from = storages[self.__request.start_point]

        if self.__request.end_point in storages:
            self.__to = storages[self.__request.end_point]

    def __courier_says(self, key):
        """
        Метод вывода сообщений курьера по ключу из словаря.
        """
        list_of_phrases = {
            'took everything': f'Курьер забрал {self.__request.amount} {self.__request.product} '
                               f'из {self.__request.start_point}.',
            'took the part': f'Курьер забрал только {self.__request.amount - self.result_remove} {self.__request.product} '
                             f'из {self.__request.start_point}, так как там больше не было!',
            'delivered everything': f'Курьер доставил {self.__request.amount - self.result_remove} {self.__request.product} '
                                    f'в {self.__request.end_point}.',
            'delivered part': f'Курьер доставил только {self.__request.amount - self.result_add} {self.__request.product} '
                              f'в {self.__request.end_point}, так как для большего нет места!',
            'returned': f'Курьер вернул обратно в {self.__request.start_point} {self.result_add} {self.__request.product}!',
            'swore': f'Курьер вернулся в {self.__request.start_point}, вернул товар и минус в карму!!!'
        }
        print(list_of_phrases[key])

    def __working_at_the_startpoint(self):
        """
        Вспомогательный метод для метода "move". Реализует логику в начальной точке маршрута курьера с учётом
        возможной разницы между наличием и запрашиваемым количеством с её фиксацией в self.result_remove.
        """
        self.result_remove = self.__from.remove(
            item=self.__request.product,
            quantity=self.__request.amount
        )
        if self.result_remove != 0:
            self.__courier_says('took the part')
        else:
            self.__courier_says('took everything')

    def __working_at_the_endpoint(self):
        """
        Вспомогательный метод для метода "move". Реализует логику в конечной точке маршрута курьера с учётом
        возможного возврата остатка товара с его фиксацией в self.result_add.
        """
        self.result_add = self.__to.add(
            item=self.__request.product,
            quantity=self.__request.amount - self.result_remove
        )
        if self.result_add != 0:
            self.__courier_says('delivered part')
            self.__from.add(
                item=self.__request.product,
                quantity=self.result_add
            )
            self.__courier_says('returned')
        else:
            self.__courier_says('delivered everything')

    def move(self) -> None:
        """
        Метод изменения количества товара на складе и в магазине.
        """
        self.__working_at_the_startpoint()
        self.__working_at_the_endpoint()

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
        self.__courier_says('swore')
