n = int(input('Введите количество элементов в списке '))
list_number = []
print(f'Введите {n} чисел')
for _ in range(n):
    temp = input()
    list_number.append(temp)
print('Ваш список ', *list_number)
for i in range(0, n - 1, 2):
    list_number[i], list_number[i + 1] = list_number[i + 1], list_number[i]
print('Измененный список', *list_number)
