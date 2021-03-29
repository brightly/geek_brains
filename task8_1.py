class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = day_month_year.split('.')
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day_month_year):
        day, month, year = Data.extract(day_month_year)
        if day < 1 or day > 31:
            return f'Не бывает {day} дня в месяце'
        elif year < 0 or year > 2021 :
            return f'{year} Неверный год'
        elif month < 1 or month > 12:
            return f'Не бывает {month} месяца в году'
        else:
            return f'{day_month_year} корректа'

    def __str__(self):
        temp = [str(i) for i in Data.extract(self.day_month_year)]
        return f'Текущая дата {".".join(temp)}'


today = Data('31.12.2001')
print(today)
print(Data.valid('19.11.2021'))
print(today.valid('19.10.2078'))
print(Data.extract('15.14.2011'))
