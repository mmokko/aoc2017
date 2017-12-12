from unittest import TestCase
from day8 import RegisterCalculator


INPUT = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''

class TestRegisterCalculator(TestCase):
    def test_register_calculator(self):
        sut = RegisterCalculator(INPUT)
        sut.execute_commands()
        registers = sorted(sut.registers, key=lambda x:x.value, reverse=True)
        self.assertEqual(1, registers[0].value)
