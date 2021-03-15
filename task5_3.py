out_f = open("task3.txt", "r")
a = out_f.read()
list_st = a.split('\n')
list_data = []

for i in list_st:
    if i != '':
        list_data.append(i.split())
print('Сотрудники с зарплатой меньше 20 тысяч')
for i in list_data:
    if int(i[1]) < 20:
        print(i[0])
zp = [int(x[1]) for x in list_data]
print(zp)
print('Средняя величина дохода', (sum(zp)) // len(zp), 'тысяч')
out_f.close()
