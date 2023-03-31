from gateways.api import CalculatorApiGateway
import unittest

class TestApi(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        
        self.calculator = CalculatorApiGateway()
    def test_divide_success_case(self):
        # print("hola")
        response = CalculatorApiGateway().divide(1,4)
        data = response.json()
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['value'],0.25)
    def test_divide_by_zero(self):
        #case 8
        # print("hola2")

        response = CalculatorApiGateway().divide(1,0)
        data = response.json()
        # print(data)

        self.assertEqual(response.status_code,200)
        self.assertEqual(data['error'],"Attempted to divide by zero.")
    
    def test_send_caracteres(self):
          #case 3

        response = CalculatorApiGateway().divide("1s","2")


        self.assertEqual(response.status_code,400)
        # self.assertEqual(data['error'],"Attempted to divide by zero.")
        # TODO use regex to validate de message

    def test_large_number(self):
        #case 3 test with multiply Value was either too large or too small for a Decimal

        response = CalculatorApiGateway().divide(1000000000000000000000,1000000000000000000000)


        self.assertEqual(response.status_code,400)
        # self.assertEqual(data['error'],"Attempted to divide by zero.")
        # TODO use regex to validate de message

    

print("testapi")
unittest.main()
