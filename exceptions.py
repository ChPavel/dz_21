# Классы исключений.
class BaseError(Exception):
    message = 'Неожиданная ошибка'


class NotEnoughProduct(BaseError):
    message = 'Товар отсутствует на складе'


class TooManyDifferentProducts(BaseError):
    message = 'В пункте назначения не приняли товар, так как превышен ассортимент.'


class InvalidRequest(BaseError):
    message = 'Ошибка в запросе. Проверьте и попробуйте снова.'


class InvalidStorageName(BaseError):
    message = 'Выбранного склада нет.'


class NotEnoughSpase(BaseError):
    message = 'Недостаточно места на складе'
