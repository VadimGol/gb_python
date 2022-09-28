from abc import ABC, abstractmethod


class Matrix:
    def __init__(self, ls):
        self.matrix = ls

    def __str__(self):
        st = ''
        for i in self.matrix:
            for j in i:
                st += str(j) + '\t'
            st += '\n'
        st = st.strip('\n')
        return st

    def __add__(self, other):
        new_ls = []
        for i in range(len(self.matrix)):
            sum_ls = []
            for j in range(len(self.matrix[i])):
                sum_ls.append(self.matrix[i][j] + other.matrix[i][j])
            new_ls.append(sum_ls)
        return Matrix(new_ls)


# a = Matrix([[1, 2, 3], [2, 3, 4]])
# b = Matrix([[1, 2, 3], [2, 3, 4]])
# c = Matrix([[1, 2, 3], [2, 3, 4]])
# print(a + b + c)
# print()


# class ClothesAbstract(ABC):
#    @abstractmethod
#    def get_size(self):
#        pass
#
#   @abstractmethod
#   def set_size(self):
#       pass
#
#   @abstractmethod
#   def cloth_amount(self, size):
#        pass

class Clothes(ABC):
    @abstractmethod
    def cloth_amount(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def cloth_amount(self):
        return (self.__size / 6.5) + 0.5

    # s = property()
    # s = s.setter(set_size)
    # s = s.getter(get_size)


class Costume(Clothes):
    def __init__(self, size):
        self.__height = size

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def cloth_amount(self):
        return (self.__height * 2) + 0.3

    # h = property()
    # h = h.setter(set_height)
    # h = h.getter(get_height)


class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return f'Has {self.cells} cells'

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else:
            return 'Невозможно отнять большее кол-во клеток'

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(int(self.cells / other.cells))

    def make_order(self, amount_row):
        sum_str = ''
        cells = self.cells
        while cells != 0:
            if cells >= amount_row:
                sum_str += ('*' * amount_row) + '\n'
                cells -= amount_row
            else:
                sum_str += '*' * cells
                cells = 0
        return sum_str


a = Cell(55)
print(a.make_order(10))
b = Cell(2)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a)
