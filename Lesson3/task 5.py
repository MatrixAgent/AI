# Задание 5

terminator = '#'

s = 0
end = False
while not end:
    l = input().split(' ')
    for e in l:
        if e == terminator:
            end = True
            break
        s += float(e)

print(f"Sum is {s}")