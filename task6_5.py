class Stationery:
    def __init__(self,title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Вы взяли ручку, запуск отрисовка {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Вы взяли карандаш, запуск отрисовка {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Вы взяли маркер, запуск отрисовка {self.title}')

zero = Stationery('Ручка')
one = Pen('ручка1')
two = Pencil('Карандаш1')
three = Handle('Маркер1')

zero.draw()
one.draw()
two.draw()
three.draw()
