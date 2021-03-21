class Clothes:
    def __init__(self, name):
        pass


class Coat(Clothes):
    def __init__(self,V):
        self.v = V

    @property
    def set_V(self):
        return self.v

    def calc(self,set_V):
        return round(self.v / 6.5 + 0.5, 2)

    def __str__(self):
        return f"Для пальто {self.v} размера " \
               f"требуется {self.calc(self.set_V)} кв м ткани"


class Suit(Clothes):
    def __init__(self,H):
        self.h = H

    @property
    def set_H(self):
        return self.h

    def calc(self,set_H):
        return round(self.h * 2 + 0.3, 2)

    def __str__(self):
        return f"Для костюма {self.h} роста " \
               f"требуется {self.calc(self.set_H)} кв м ткани"


a = Coat(36)
print(a)
b = Suit(1.83)
print(b)