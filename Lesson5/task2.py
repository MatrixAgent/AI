# Задание 2

def wordcount(s):
    return len(s.split())

with open("task2.txt", "r") as f:
    l = f.readlines()

    for i, e in enumerate(l):
        print(f"Line {i + 1} has {wordcount(e)} words.")

print(f"Total lines: {len(l)}")