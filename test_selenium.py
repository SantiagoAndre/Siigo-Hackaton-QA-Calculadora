from gateways.selenium import CalculatorSeleniumGateway
import unittest

global_calculator = CalculatorSeleniumGateway()
from time import sleep
class TestSelenium(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        
        self.calculator = global_calculator
    def test_case_0(self):
        '''Este test valida que al oprimir un valor aparece en la interfaz'''
        # print("hola")
        self.calculator.input_number(3)
        display = self.calculator.get_display()
        self.assertEqual("3",display)
        self.calculator.delete(4)

    def test_case_1_add(self):
        '''Usuario requiere él resultado de una operación aritmética: caso suma'''
        self.calculator.input_number(3)
        self.calculator.press_button("+")
        self.calculator.input_number(3)
        self.calculator.operate()
        display = self.calculator.get_display()
        print(display)
        self.calculator.delete(4)
        self.assertEqual("6",display)
    def test_case_1_multiply(self):
        '''Usuario requiere él resultado de una operación aritmética: caso multiplicacion'''
        self.calculator.input_number(3)
        self.calculator.press_button("*")
        self.calculator.input_number(3)
        self.calculator.operate()
        display = self.calculator.get_display()
        print(display)
        self.calculator.delete(4)
        self.assertEqual("9",display)
    def test_case_1_resta(self):
        '''Usuario requiere él resultado de una operación aritmética: caso resta'''
        self.calculator.input_number(3)
        self.calculator.press_button("-")
        self.calculator.input_number(3)
        self.calculator.operate()
        display = self.calculator.get_display()
        self.calculator.delete(4)
        self.assertEqual("0",display)
    def test_case_1_div(self):
        '''Usuario requiere él resultado de una operación aritmética: caso divicion'''
        self.calculator.input_number(6)
        self.calculator.press_button("/")
        self.calculator.input_number(3)
        self.calculator.operate()
        display = self.calculator.get_display()
        print(display)
        self.calculator.delete(4)
        self.assertEqual("2",display)
    def test_case_5(self):
        '''Usuario inenta hacer una operacion aritmetrica solo con un numero'''
        self.calculator.input_number(6)
        self.calculator.press_button("/")
        self.calculator.operate()
        display = self.calculator.get_display()
        print(display)
        self.calculator.delete(4)
        self.assertEqual("6/",display)
    def test_case_8(self):
        '''El usuario intenta hacer una divicion por 0'''
        #case 8
        self.calculator.input_number(99)
        self.calculator.press_button("/")
        self.calculator.press_button("0")
        self.calculator.operate()
        display = self.calculator.get_display()
        self.calculator.delete(5)
        self.assertEqual(display,"0")    
   
    def test_large_number(self):
        #case 3 test with multiply Value was either too large or too small for a Decimal
        self.calculator.input_number(1000000000000000000000)
        self.calculator.press_button("/")
        self.calculator.input_number(1000000000000000000000)
        self.calculator.operate()
        display = self.calculator.get_display()
        self.calculator.delete(45)
        self.assertEqual(display,"1")

    
# if __name__ == '__main__':
unittest.main()