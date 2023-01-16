import pytest

from app.calculator import Calculator


class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 2) == 3

    def test_subtraction_success(self):
        assert self.calc.subtraction(5, 3) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(2, 4) == 8

    def test_division_success(self):
        assert self.calc.division(9, 3) == 3

    def teardown_method(self):
        print('Выполнение метода Teardown')
