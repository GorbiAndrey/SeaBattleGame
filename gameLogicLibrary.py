from random import randint

from exceptionLibrary import *
from gameObjectLibrary import Dot, Ship, Board
from playersLibrary import AI, User


class Game:
    """класс игры и генерации доски"""

    def __init__(self, size=6):
        """создаем конструктор"""

        self.lens = [3, 2, 2, 1, 1, 1, 1]
        self.size = size
        player = self.random_board()
        comp = self.random_board()
        comp.hid = True

        self.ai = AI(comp, player)
        self.us = User(player, comp)

    def try_board(self):
        board = Board(size=self.size)
        attempts = 0
        for board_len in self.lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), board_len, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):
        """функция приветствия"""

        print("__________________")
        print(" Приветствуем вас ")
        print("      в игре      ")
        print("    морской бой   ")
        print("__________________")
        print("формат ввода: х у ")
        print(" x - номер строки ")
        print(" у - номер столбца")

    def print_boards(self):
        """функция отображения доски"""

        print("-" * 20)
        print(" Доска пользователя: ")
        print(self.us.board)
        print("-" * 20)
        print(" Доска компьютера: ")
        print(self.ai.board)
        print("-" * 20)

    def loop(self):
        """функция для игрового цикла"""

        num = 0
        while True:
            self.print_boards()
            if num % 2 == 0:
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("Ходит компьютер! ")
                repeat = self.ai.move()

            if repeat:
                num -= 1

            if self.ai.board.defeat():
                self.print_boards()
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.us.board.defeat():
                self.print_boards()
                print("-" * 20)
                print("Компьютер выиграл")
                break

            num += 1

    def start(self):
        """функция запуска"""

        self.greet()
        self.loop()
