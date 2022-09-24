import time


class TrafficLight:
    __color = ''

    def running(self):
        while True:
            self.__color = 'Red'
            print(self.__color)
            time.sleep(7)
            self.__color = 'Yellow'
            print(self.__color)
            time.sleep(2)
            self.__color = 'Green'
            print(self.__color)
            time.sleep(7)


# first = TrafficLight()
# first.running()


class Road:
    _length = 0
    _width = 0
    m_for_1_meter = 25
    height = 1

    def __init__(self):
        self._length = int(input('Введите длину дороги (м): '))
        self._width = int(input('Введите ширину дороги (м): '))

    def measure(self):
        self.m_for_1_meter = int(input(
            'Введите массу асфальта для покрытия одного квадратного метра дороги c толщиной 1 см в (кг): '))
        self.height = int(input('Введите толщину асфальта в (см): '))
        return f'{(self._width * self._length * self.m_for_1_meter * self.height) / 1000} (т)'


# route = Road()
# print(route.measure())

class Worker:
    name = ''
    surname = ''
    position = ''
    wage = 0
    bonus = 0
    income = {'wage': wage, 'bonus': bonus}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = int(input('Введите оклад работника: '))
        self.bonus = int(input('Введите премию сотрудника: '))
        self.income = {'wage': self.wage, 'bonus': self.bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        print(self.income['bonus'] + self.income['wage'])


# director = Position('Ivan', 'Ivanov', 'director')
# director.get_total_income()
# director.get_full_name()
# print(director.name)
# print()


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Поехали!')

    def stop(self):
        print('Стоп!')

    def turn(self, direction):
        print(f'Поворачиваем {direction}')

    def show_speed(self):
        print(f'Скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость {self.speed}')
        if self.speed > 60:
            print('Превышение!')


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость {self.speed}')
        if self.speed > 40:
            print('Превышение!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self):
        super().__init__()
        self.is_police = True


class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        self.title = 'Pen'

    def draw(self):
        print(f'Запуск отрисовки ручкой')


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Pencil'

    def draw(self):
        print(f'Запуск отрисовки карандашом')


class Handle(Stationery):
    def __init__(self):
        self.title = 'Handle'

    def draw(self):
        print(f'Запуск отрисовки маркером')
