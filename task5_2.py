out_f = open("task2.txt", "r")
a = out_f.read()
list_st = a.split('\n')
print(f'В файле {len(list_st)} строк')
for num, i in enumerate(list_st, 1):
    print(f'В строке {num} символов {len(i)} ')
out_f.close()
