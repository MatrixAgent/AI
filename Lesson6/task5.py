# Задание 5

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print(f'Рисует ручка {self.title}.')

class Pencil(Stationery):
    def draw(self):
        print(f'Рисует карандаш {self.title}.')


class Handle(Stationery):
    def draw(self):
        print(f'Рисует маркер {self.title}.')

Pen('синяя').draw()
Pencil('химический').draw()
Handle('оранжевый').draw()
