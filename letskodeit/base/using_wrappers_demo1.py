from selenium import webdriver
from base.HandyWrappers import HandyWrappers
import time

class UsingWrappers1():
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Ie()
        driver.maximize_window()
        driver.implicitly_wait(5)
        
        hw = HandyWrappers(driver)
        driver.get(baseURL)
        
        textField = hw.getElement("name", locatorType='id')
        textField.send_keys("manish")

ie = UsingWrappers1()
ie.test()