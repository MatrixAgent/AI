# Задание 7

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return Complex(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)

    def __str__(self):
        return f'({self.r}, {self.i})'

a = Complex(1, 1)
b = Complex(2, 0)

print(a + b)
print(a * b)
