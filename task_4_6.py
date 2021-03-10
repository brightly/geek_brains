from itertools import count, cycle

def counter(num):
    for el in count(num):
        print(el)
        if el == 25:
            break
counter(3)

def looped(list_number):
    for el in cycle(list_number):
        print(el)
        if el == 19:
            break

looped([el for el in range(1,20)])