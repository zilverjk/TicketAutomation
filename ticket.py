import os
import sys
from selenium import webdriver


path = "C:\PythonScripts\TicketAutomation"
browser = webdriver.Chrome(
    "C:\PythonScripts\TicketAutomation\chromedriver.exe")
browser.get("http://www.ofisis.com.pe/solicitud-soporte")
codAcceso = "0433"


def generateTicket():
    pyButton = browser.find_elements_by_xpath(
        "//*[@id='txtCodigoAcceso_I']")[0]
    pyButton.click()
    pyButton.send_keys(codAcceso)


if __name__ == "__main__":
    generateTicket()
