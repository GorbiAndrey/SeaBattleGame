# SeaBattleGame

Игра «Морской бой».

Интерфейс приложения представляет из себя консольное окно с двумя полями вида 6х6.

Программа поделена на следующие модули:
- main:
    модуль запуска игры.  
- gameObjectLibrary:
    модуль содержит классы Dot, Ship, Board. В нем реализована внутренняя логика игры.
- gameLogicLibrary:
    модуль содержит основной класс Game, который отвечает за внешнюю логику игры (пользовательский интерфейс, игровой контроллер, который считает побитые корабли). 
    В данном классе происходит сборка основных объектов игры.
- playersLibrary:
    модуль содержит классы Player, AI, User и отвечает за поведение игрока и искуственного интеллекта, так же относится к внешней логике игры.
- exceptionLibrary:
    модуль содержит в себе классы ошибок, которые могут возникнуть в процессе игры.

