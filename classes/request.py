from classes.abstract_storage import Storage
from exceptions import InvalidRequest, InvalidStorageName


class Request:
    """
    Класс запроса пользователя.
    """
    def __init__(self, request: str, storages: dict[str: Storage]):

        s_request = request.lower().split(' ')
        if len(s_request) != 7:
            raise InvalidRequest

        self.amount = int(s_request[1])
        self.product = s_request[2]
        self.start_point = s_request[4]
        self.end_point = s_request[6]

        if self.start_point not in storages or self.end_point not in storages:
            raise InvalidStorageName
