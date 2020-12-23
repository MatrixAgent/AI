# Задание 3

class Worker:
    def __init__(self, name, surname, pos, income):
        self.name = name
        self.surname = surname
        self.position = pos
        self._income = income

class Position(Worker):
    def __init__(self, name, surname, pos, income):
        super().__init__(name, surname, pos, income)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

w = Position("John", "Doe", "Boss", { "wage": 3000, "bonus": 300 })
print(w.name, w.surname, w.position, w._income)
print(w.get_full_name())
print(w.get_total_income())
