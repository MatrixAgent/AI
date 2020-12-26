# Задание 2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, a, b):
        return self._length * self._width * a * b / 1000

road = Road(20, 5000)
print(road.mass(25, 5))