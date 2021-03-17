class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income

class Position(Worker):
    def get_full_name(self):
        print(f'ФИ - {self.surname} {self.name}')
    def get_total_income(self):
        print(f'Полный доход {sum(list(self.income.values()))}')

position1 = Position('Ваня','Петров','инженер',{'wage' : 200000, 'bonus': 30000})
position2 = Position('Дима','Свиридов','программист',{'wage' : 100000, 'bonus': 50000})
position1.get_full_name()
position1.get_total_income()
position2.get_full_name()
position2.get_total_income()