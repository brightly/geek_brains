time_year = {'зима': [12, 1, 2],
             'весна': [3, 4, 5],
             'лето': [6, 7, 8],
             'осень': [9, 10, 11],
             }
number = 15
while number < 1 or number > 12:
    number = int(input('Введите номер месяца '))
for key, val in time_year.items():
    if number in val:
        print(key)
