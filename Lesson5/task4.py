# Задание 4

d = { "Zero": "Ноль", "One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять",
      "Six": "Шесть", "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять" }

with open("task4out.txt", "w", encoding="utf-8") as of:
    with open("task4.txt", "r") as f:
        l = f.readline().split('-')
        while l != ['']:
            of.write(f"{d[l[0]]}-{l[1]}")
            l = f.readline().split('-')
