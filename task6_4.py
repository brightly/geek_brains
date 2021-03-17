class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name}  остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.name} повернула {self.direction}')

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')
        if self.speed > 60:
            print('Привышение, в городе нельзя ехать больше 60')


class SportCar(Car):
    def get_highly_speed(self, speed):
        print(f'Ваш SportCar разогнался до {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')
        if self.speed > 40:
            print('Привышение, на рабочей машине нельзя ехать больше 40')


class PoliceCar(Car):
    def polis_is(self):
        self.is_police = True
        print(f" {self.name} полицейская машина")


tiguan = Car(50, 'Black', "Тигик", False)
tiguan.go()
tiguan.stop()
tiguan.turn('направо')
tiguan.show_speed()
nissan = TownCar(70, 'White', "Ниссан", False)
nissan.show_speed()
ford = PoliceCar(40, 'Blue', "Форд", True)
ford.polis_is()
bmw = WorkCar(70, 'Black', "Бэха", False)
bmw.show_speed()
