# Задание 2
from abc import ABC, abstractmethod

class Одежда(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def Расход(self):
        pass

class Пальто(Одежда):
    def __init__(self, V):
        self.V = V
    @property
    def Расход(self):
        return self.V / 6.5 + 0.5

class Костюм(Одежда):
    def __init__(self, H):
        self.H = H
    @property
    def Расход(self):
        return self.H * 2 + 0.3

a = Пальто(10)
print(a.Расход)

b = Костюм(10)
print(b.Расход)

