# Задание 2

l = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([l[i] for i in range(1, len(l)) if l[i-1] < l[i]])
