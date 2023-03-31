import requests


base_url="http://localhost:5000/"
#case 8
class CalculatorApiGateway:

    def divide(self,number1,number2):
        url = f"{base_url}Calculator/Divide"
        body = {
            "firstDecimal": number1,
            "secondDecimal": number2
            }
        headers=   {"Accept": "application/json",
            "Content-Type": "application/json",}
        response = requests.post(url,json=body,headers=headers)
        return response
# response = CalculatorApiGateway().divide(1,0)
# print(response.text)
