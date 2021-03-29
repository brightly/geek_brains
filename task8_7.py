class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма t1 и t2')
        return f't = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение t1  и t2')
        return f't = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f't = {self.a} + {self.b} * i'


t1 = ComplexNumber(4, -5)
t2 = ComplexNumber(8, 2)
print(t1)
print(t2)
print(t1 * t2)
print(t1 + t2)
