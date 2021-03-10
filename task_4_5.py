from functools import reduce

list_number = [el for el in range(100, 1001) if el % 2 == 0]


def pr(a, b):
    return a * b


print(reduce(pr, list_number))
