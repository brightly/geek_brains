my_list = [7, 5, 3, 3, 2]
temp = 0
while temp != -1:
    temp = int(input('Введите число, для окончания ввода введите -1 '))
    for num, i in enumerate(my_list):
        if temp > i:
            my_list.insert(num,temp)
            break
    print('Рейтинг с участием вашей оценки ',my_list)