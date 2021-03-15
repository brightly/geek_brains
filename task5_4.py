out_f = open("task4.txt", "r")
a = out_f.read()
list_st = a.split('\n')
list_data = []
out_f.close()
for i in list_st:
    if i != '':
        list_data.append(i.split())
spisok = {'One': 'Один', 'Two': 'Два', 'Three': 'Три',
             'Four': 'Четыре', 'Five': 'Пять', 'Six': 'Шесть',
             'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять',
             'Ten': 'Десять'}
out_f = open("out_file.txt", "w")
for i in list_data:
    temp = spisok[i[0]]+i[1]+i[2]
    out_f.write(temp)
    out_f.write('\n')

out_f.close()