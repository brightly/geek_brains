import random

out_f = open("out_file1.txt", "w")
for _ in range(100):
    temp = str(random.randint(1, 1000))
    out_f.write(temp)
    out_f.write(' ')
out_f.close()
out_f = open("out_file1.txt", "r")
a = out_f.read()
list_st = a.split(' ')
print(list_st)
list_st = [int(x) for x in list_st if x != '']
print(f'Сумма чисел {sum(list_st)}')
out_f.close()
