from prettytable import PrettyTable

class OfficeEquipment:
    def __init__(self):
        self.equipment = {
            'name' : [],
            'price' : [],
            'quantity' : []
        }

    def table_print(self):
        x = PrettyTable()
        x.field_names = ["Наминование", "Цена", "Количество"]
        for i in range(len(self.equipment['name'])):
            x.add_row([self.equipment['name'][i], self.equipment['price'][i], self.equipment['quantity'][i]])
        print(x)


    def reception(self):
        try:
            name = input(f'Введите наименование ')
            price = int(input(f'Введите цену за ед '))
            quantity = int(input(f'Введите количество '))
            print(f'Добавлено на склад {name} Цена {price} Количество {quantity}')
            self.equipment['name'].append(name)
            self.equipment['price'].append(price)
            self.equipment['quantity'].append(quantity)
        except:
            return f'неверно ввели данные'


t = OfficeEquipment()
t.reception()
t.reception()
t.table_print()

