def my_func(x, y):
    pr = 1
    for i in range(1, (-1) * y + 1):
        pr *= x
    print(pr)
    return 1 / pr


print(my_func(5, -3))
