# Задание 5

class Склад:
    def __init__(self):
        self.l = { 'dep1': {}, 'dep2': {} }
    def add(self, d, t, n):
        if self.l[d].get(t) == None:
            self.l[d][t] = n
        else:
            self.l[d][t] += n
    def show(self):
        for i in self.l:
            print(i + ':')
            for j in self.l[i]:
                print(f'{j.name} - {self.l[i][j]}')

class Оргтехника:
    def __init__(self, n, m, p):
        self.name = n
        self.model = m
        self.price = p

class Принтер(Оргтехника):
    def __init__(self, n, m, p, type):
        super().__init__(n, m, p)
        self.type = type

class Сканер(Оргтехника):
    pass

p = Принтер('принтер', 'canon', 10000, 'laser')
s = Сканер('сканер', 'canon', 10000)
store = Склад()
store.add('dep1', p, 2)
store.add('dep2', s, 1)
store.show()