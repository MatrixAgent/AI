# Задание 4

class Склад:
    pass

class Оргтехника:
    def __init__(self, n, m, p):
        self.name = n
        self.model = m
        self.price = p

class Принтер(Оргтехника):
    def __init__(self, n, m, p, type):
        super(m, p)
        self.type = type

class Сканер(Оргтехника):
    pass
