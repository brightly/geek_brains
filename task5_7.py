import json

profit = {}
pr = {}
prof = []
prof_over = 0
global_list = []
with open('task7.txt', 'r') as file:
    for line in file:
        name, sobst, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
    prof = list(profit.values())
    prof = [int(x) for x in prof if x > 0]
    prof_over = sum(prof)/len(prof)
    pr['average_profit'] = prof_over
    global_list.append(profit)
    global_list.append(pr)



with open('file_7.json', 'w') as write_f:
    json.dump(global_list, write_f)


