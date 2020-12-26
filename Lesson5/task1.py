# Задание 1

with open("task3.txt", "w") as f:
    s = input()
    while s != "":
        f.write(s + "\n")
        s = input()
