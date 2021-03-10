from math import factorial


def fact(n):
    for i in range(0, n + 1):
        yield factorial(i)

n = int(input('Введите число n до которого будем считать факториалы '))
for i, el in enumerate(fact(n)):
    print(f'Факториал {i}! равен {el}')

