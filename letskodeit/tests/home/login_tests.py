import sys
sys.path.append("C:\\Users\\Manish Rawat\\git\\repository\\letskodeit")

from selenium import webdriver
from selenium.webdriver.common.by import By 
from pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):
    
    def test_validLogin(self):
        baseURL = "https://learn.letskodeit.com/"
        driver = webdriver.Ie()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)
        
        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")
        
        userIcon = driver.find_element(By.XPATH, "//div[@id='navbar']//span[text()='Test']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login failed")



        