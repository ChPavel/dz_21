from classes.courier import Courier
from classes.request import Request
from classes.shop import Shop
from classes.store import Store
from exceptions import BaseError

store = Store(items={
    "печенька": 25,
    "собачка": 25,
    "ёлка": 25,
    "пончик": 12,
    "торт": 10,
    "питон": 1
})

shop = Shop(items={
    "печенька": 4,
    "собачка": 4,
    "ёлка": 2,
    "торт": 2,
    "питон": 2
})

storages = {
    'магазин': shop,
    'склад': store
}


def main():
    print('\nПривет!\n')

    while True:
        for name in storages:
            print(f'Сейчас в {name}:\n {storages[name].get_items()}')

        user_input = input(
            'Введите запрос, соблюдая единственное число, в формате "Доставить 3 печенька из склад в магазин"\n'
            'Введите "стоп" или "stop", если хотите выйти из программы:\n'
        )
        if user_input in ("стоп", "stop"):
            break

        try:
            request = Request(request=user_input, storages=storages)
        except BaseError as e:
            print(e.message)
            continue

        courier = Courier(request, storages)

        try:
            courier.move()
        except BaseError as e:
            if e.message == 'В пункте назначения не приняли товар, так как превышен ассортимент.':
                print(e.message)
                courier.again_the_authorities_messed_up()
                continue
            print(e.message)
            continue


if __name__ == '__main__':
    main()
