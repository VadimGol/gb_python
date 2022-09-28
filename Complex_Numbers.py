class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return f'{self.re} + {self.im}i'

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber((self.re * other.re) - (self.im * other.im), (self.re * other.im) + (self.im * other.re))


a = ComplexNumber(2, 3)
b = ComplexNumber(5, 4)
print(a * b)
print(a + b)

