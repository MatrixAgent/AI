# Задание 4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} goes!')

    def stop(self):
        print('Stopped.')

    def turn(self, dir):
        print(f'Turned to {dir}')

    def show_speed(self):
        print(f"Speed of {self.name} = {self.speed}")

class TownCar(Car):
    limit = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
    def show_speed(self):
        super().show_speed()
        if self.speed > self.limit:
            print(f"Speed is above limit by {self.speed - self.limit}!")

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

class WorkCar(Car):
    limit = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > self.limit:
            print(f"Speed is above limit by {self.speed - self.limit}!")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

cars = [TownCar(70, 'Green', 'Best car'), SportCar('100', 'Red', 'Super car'), WorkCar(50, 'Yellow', 'Usefull car'), PoliceCar(90, 'Blue', 'Strict car')]
for e in cars:
    print(f'{e.name}, speed: {e.speed}, color: {e.color}, police: {e.is_police}')
    e.go()
    e.show_speed()
    e.turn('left')
    e.stop()

