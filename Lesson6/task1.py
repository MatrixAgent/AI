from time import sleep

# Задание 1

class TrafficLight:
    def __init__(self):
        self.__light = [(7, "red"), (2, "yellow"), (5, "green")]

    def running(self):
        for e in self.__light:
            self.__color = e[1]
            print(self.__color)
            sleep(e[0])

tl = TrafficLight()
for i in range(3):
    tl.running()
