from sys import argv
print(argv)

name, money_hours, stavka, premia = argv
print(f'Выроботка в часах {money_hours}')
print(f'Ставка в час {stavka}')
print(f'Премия {premia}')
print(f'Заработная плата сотрудника {(int(money_hours) * int(stavka)) + int(premia)}')