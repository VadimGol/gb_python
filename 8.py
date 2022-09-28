from abc import ABC, abstractmethod


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def validation(day, month, year):
        if day > 31 or day < 1:
            print('Day is out of range')
            return False
        if month > 12 or month < 1:
            print('Month is out of range')
            return False
        if year < 0:
            print('Year is out of range')
            return False
        return True

    @classmethod
    def set_d_m_y(cls, obj):
        day = int(obj.split('-')[0])
        month = int(obj.split('-')[1])
        year = int(obj.split('-')[2])
        if Date.validation(day, month, year):
            return cls(day, month, year)


anniversary = Date.set_d_m_y('25-07-2012')
print(anniversary.year)

birthday = Date.set_d_m_y('26-08-2003')
print(birthday.year)
print(birthday.day)

date = Date.set_d_m_y('33-02-24')


class Zero(Exception):
    def __init__(self, txt):
        self.txt = txt


a = input('Введите a: ')
b = input('Введите b: ')
try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise Zero('Division on 0 is not permitted')
    summary = a / b
except (ValueError, Zero) as err:
    print(err)
else:
    print(summary)
finally:
    print('end of operation')


class DigitList(Exception):
    def __init__(self, txt):
        self.txt = txt


def only_numbers(list_numbers=[]):
    try:
        while True:
            arg = input('Введите число для списка: ')
            if arg == 'stop':
                break
            if not arg.isdigit():
                raise DigitList('List must contain only numbers')
            list_numbers.append(arg)
    except DigitList as error:
        print(error)
        only_numbers(list_numbers)
    else:
        print(list_numbers)


# only_numbers()
####################################################################################
class StorageOfOfficeEquipment:
    def __init__(self, size):
        self.size = size
        self.stor_unit = {}
        self.stor = []

    def add_equip(self, name, year, department, amount):
        if self.size > 0:
            self.size -= 1
        self.stor_unit['name'] = name
        self.stor_unit['year'] = year
        self.stor_unit['department'] = department
        for i in range(1, amount):
            self.stor.append(self.stor_unit)

    def remove_from_storage(self, name):
        for i in self.stor:
            if i['name'] == name:
                self.stor.remove(i)
                self.size += 1


class Equipment(ABC):
    @abstractmethod
    def add_to_storage(self, amount):
        pass

    @abstractmethod
    def send_to_department(self, department):
        pass


class OfficeEquipment(Equipment):
    @staticmethod
    def validation(amount):
        if amount is not int:
            print('Amount must be integer')
            return False
        return True

    def __init__(self, year, department, name):
        self._year = year
        self._department = department
        self._name = name

    def add_to_storage(self, amount):
        if OfficeEquipment.validation(amount):
            StorageOfOfficeEquipment.add_equip(self._name, self._year, self._department, amount)

    def send_to_department(self, department):
        self._department = department


class Printer(OfficeEquipment):
    __amount_of_ink = 0
    __brightness = 0

    def printer_print(self):
        print('Printing!..')
        self.__amount_of_ink -= 1

    @property
    def bright(self):
        return self.__brightness

    @bright.setter
    def bright(self, brightness):
        self.__brightness = brightness

    def ink(self):
        return self.__brightness

    def refill(self, ink):
        self.__amount_of_ink += ink


class Scanner(OfficeEquipment):
    def scanning(self):
        print('Scanning!..')

    @property
    def naming(self):
        return self._name

    @naming.setter
    def naming(self, name):
        self._name = name


class Copier(OfficeEquipment):
    __amount_of_ink = 0
    __brightness = 0

    def copy(self):
        print('Copying!..')
        self.__amount_of_ink -= 1

    @property
    def bright(self):
        return self.__brightness

    @bright.setter
    def bright(self, brightness):
        self.__brightness = brightness

    def ink(self):
        return self.__brightness

    def refill(self, ink):
        self.__amount_of_ink += ink


stor1 = StorageOfOfficeEquipment(5)
a1 = Copier(2002, 'Buhg', 'Samsung')
