# Задание 4

def my_func1(x, y):
    return x ** y

def my_func2(x, y):
    r = 1
    for i in range(abs(y)):
        if y > 0:
            r *= x
        else:
            r /= x
    return r

x = float(input("x = "))
y = int(input("y = "))

print(my_func1(x, y))
print(my_func2(x, y))
