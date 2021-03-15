out_f = open("task6.txt", "r")
a = out_f.read()
list_st = a.split('\n')
list_data = []
out_f.close()
print('Исходные данные:', list_st)
dict_lab = dict()
for i in list_st:
    if i != '':
        temp = i.split(':')[0]
        temp1 = i.split()[1:]
        temp2 = []
        for j in temp1:
            if j[0].isdigit():
                temp2.append(int(j.split('(')[0]))
        dict_lab[temp] = sum(temp2)
print('Получившийся словарь:', dict_lab)
