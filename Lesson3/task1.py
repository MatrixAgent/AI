# Задание 1

def div(a, b):
    try:
        return a / b;
    except ZeroDivisionError:
        print("Division by zero!")

a = int(input("a = "))
b = int(input("b = "))

print(f"a / b = {div(a, b)}")
