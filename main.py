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


def in_storages_now():
    for name in storages:
        print(f'Сейчас в {name}:\n {storages[name].get_items()}')


def user_says():
    return input(
        'Введите запрос, соблюдая единственное число, в формате "Доставить 3 печенька из склад в магазин"\n'
        'Введите "стоп" или "stop", если хотите выйти из программы:\n'
    )


def courier_in_business(request):
    courier = Courier(request, storages)

    try:
        courier.move()
    except BaseError as e:
        if e.message == 'В пункте назначения не приняли товар, так как превышен ассортимент.':
            print(e.message)
            courier.again_the_authorities_messed_up()
            return 'continue'
        print(e.message)
        return 'continue'


def main():
    print('\nПривет!\n')

    while True:
        in_storages_now()

        user_input = user_says()
        if user_input in ("стоп", "stop"):
            break

        try:
            request = Request(request=user_input, storages=storages)
        except BaseError as e:
            print(e.message)
            continue

        if courier_in_business(request) == 'continue':
            continue


if __name__ == '__main__':
    main()
