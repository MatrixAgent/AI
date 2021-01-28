# Задание 1
# Метод test так и не понял почему не работает. У кого-то глюк: или у меня или у системы.

class Date:
    def __init__(self, d):
        self.date = d

    @classmethod
    def conv(cls, date : 'Date'):
        return [int(e) for e in date.date.split('-')]

    @staticmethod
    def test(date : 'Date'):
        t = Date.conv(date)
        if t[1] == 2:
            n = t[2] % 4 == 0 if 29 else 28
        elif t[1] <= 7:
            n = t[1] % 2 == 1 if 31 else 30
        else:
            n = t[1] % 2 == 0 if 31 else 30

        return t[0] >= 1 and t[0] <= n

d = Date('01-02-2021')
t = Date.conv(d)
for i in t:
    print(i)

print(Date.test(d))
