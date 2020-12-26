# Задание 1

class Matrix:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        s = ""
        for i in self.a:
            for j in i:
                s = f"{s} {j}"
            s += "\n"
        return s

    def __add__(self, other):
        c = []
        for i in range(len(other.a)):
            c.append([])
            for j in range(len(other.a[0])):
                c[i].append(self.a[i][j] + other.a[i][j])
        return Matrix(c)

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

print(A + B)
