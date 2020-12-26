# Задание 3

class Cell:
    def __init__(self, n):
        self.n = n
    def __add__(self, other):
        return Cell(self.n + other.n)
    def __sub__(self, other):
        if self.n > other.n:
            return Cell(self.n - other.n)
        else:
            print("Illegal action!")
            return None
    def __mul__(self, other):
        return Cell(self.n * other.n)
    def __truediv__(self, other):
        return Cell(self.n // other.n)

    def make_order(self, k):
        i = self.n // k
        j = self.n % k
        return ("*" * k + '\n') * i + "*" * j
    def __str__(self):
        return str(self.n)

c1 = Cell(7)
c2 = Cell(2)
print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c1 * c2)
print(c1 / c2)

print(c1.make_order(2))s