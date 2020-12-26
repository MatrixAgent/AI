# Задание 6
#
def int_func(word):
    return word.capitalize()

s = input()
l = s.split(" ")
for i in range(len(l)):
    l[i] = int_func(l[i])

print(" ".join(l))
