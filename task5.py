
summ = 0
last = 't'
while last.lower() != 'q':
    temp = input("Введите числа через пробел Q - выход ").split()
    last = temp[-1]
    if last.lower() == 'q':
        temp = [int(x) for x in temp[:-1]]
        summ += sum(temp)
        print(f'Окончательная сумма {summ}')
        break
    else:
        temp = [int(x) for x in temp]
        summ += sum(temp)
        print(f'Сумма чисел {summ}')
