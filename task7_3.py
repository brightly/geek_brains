class Cell:
    def __init__(self, quantity):
        self.q = int(quantity)

    def __str__(self):
        return f'Получилась клетка \n{self.make_order()}'

    def make_order(self):
        answer = ''
        for i in range(self.q // 5):
            answer += 5 * '*' + '\n'
        answer += self.q % 5 * '*'
        return answer

    def __add__(self, other):
        return Cell(self.q + other.q)

    def __sub__(self, other):
        if self.q - other.q < 0:
            print(f'Оперция невозможна')
        else:
            return Cell(self.q - other.q)
    def __mul__(self, other):
       return Cell(self.q * other.q)

    def __truediv__(self, other):
        return Cell(self.q // other.q)

cells1 = Cell(33)
cells2 = Cell(8)
print(cells1+cells2)
print(cells1-cells2)
print(cells2-cells1)
cells3 = Cell(3)
cells4 = Cell(2)
print(cells3*cells4)
print(cells1/cells2)
