out_f = open("out_file.txt", "a")
temp = 1
while temp != '':
    temp = input('Введите данные окончание ввода пустая строка ')
    out_f.write(temp)
    out_f.write('\n')

out_f.close()