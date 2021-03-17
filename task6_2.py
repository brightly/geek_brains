class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def massa(self, ves, square):
        self.ves = ves
        self.square = square
        print(f'Масса асфальта для покрытий {self.square} см')
        print((self.__length * self.__width * self.ves * self.square)//1000,'т')

road1 = Road(20, 5000)
road1.massa(25, 5)
