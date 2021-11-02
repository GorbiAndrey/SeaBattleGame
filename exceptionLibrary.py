class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    """Ошибка при попытке выстрелить за пределы доски"""

    def __str__(self):
        return "Вы пытаетесь выстрелить за доску"


class BoardUsedException(BoardException):
    """Ошибка при попытке выстрелить повторно в клетку"""

    def __str__(self):
        return "Вы уже стреляли в эту клетку"


class BoardWrongShipException(BoardException):
    pass
