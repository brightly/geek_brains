list_word = input('Введите текст ').split()
for num, i in enumerate(list_word, 1):
    if len(i)>10:
        print(num, i[:10])
    else:
        print(num,i)
