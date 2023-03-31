

import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from utils import extract_digits
   
class CalculatorSeleniumGateway:
    def __init__(self) -> None:

                
        self.driver =  webdriver.Firefox()
        self.driver.get("http://localhost:8001/")
        sleep(2)
        self.__map_buttons()
    def __map_buttons(self):
        '''Esta funcion crea un diccionario con todos los botones de la calculadora'''
        self.display = self.driver.find_element(By.CLASS_NAME,"DisplayText")
        self.delete_b = self.driver.find_element(By.XPATH,'//input[@class="Button"]')
        buttons = self.driver.find_elements(By.XPATH,'//button[@class="Button"]')
        sleep(0.5)
        self.map_buttons = {}
        print("Mapeando botones de la calculadora: ....")
        for b in buttons:
            b.click()
            sleep(0.1)
            b_value = self.display.get_attribute("value")
            self.map_buttons[str(b_value)] = b
            self.delete_b.click()
            print(f"boton {b_value} mapeado...")

        print("Boton * mapeado: ....")
        self.map_buttons["*"] = self.driver.find_element(By.CLASS_NAME,"Multiply")
        print("Boton enviar mapeado: ....")
        self.send_button = self.driver.find_element(By.NAME,"equal")
    def press_button(self,key):
        key = str(key)
        if key in self.map_buttons:
            self.map_buttons[key].click()
    def input_number(self,number):
        for digit in extract_digits(number):
            self.press_button(digit)
    def delete(self,times=1):
        for _ in range(times):
            self.delete_b.click()
    def operate(self):
        self.send_button.click()
    def get_display(self):
        return self.display.get_attribute("value")
