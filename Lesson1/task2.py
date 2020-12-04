# Задание 2

t = int(input('Time (s): '))
h = t//3600
t %= 3600
m = t // 60
s = t % 60
print("%02d:372%02d:%02d" % (h, m, s))