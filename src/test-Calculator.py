import unittest

from src.Calculator import Calculator
from src.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader("math-operator-csvdata/Subtraction1.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_addition(self):
        test_data = CsvReader("math-operator-csvdata/Addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        test_data = CsvReader("math-operator-csvdata/Multiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiplication(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square(self):
        test_data = CsvReader("math-operator-csvdata/Square.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.squares(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_squarerts(self):
        test_data = CsvReader("math-operator-csvdata/SquareRoot.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.squaresrt(row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)