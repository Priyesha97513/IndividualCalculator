from src.Subtraction import subtraction
from src.Addition import addition
from src.Multiplication import multipy
from src.Squares import square
from src.SquareRoot import squarert
from src.Exponent import exponent
from src.Division import division


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiplication(self,a,b):
        self.result = multipy(a,b)
        return self.result

    def squares(self,a):
        self.result = square(a)
        return self.result

    def squaresrt(self,a):
        self.result = squarert(a)
        return self.result

    def exponents(self,a,b):
        self.result = exponent(a,b)
        return self.result

    def divisions(self,a,b):
        self.result = division(a,b)
        return self.result