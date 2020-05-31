import sys
sys.path.append("C:\\Users\\Manish Rawat\\git\\repository\\letskodeit")

from selenium import webdriver
from selenium.webdriver.common.by import By 
from pages.home.login_page import LoginPage
import unittest
import pytest
import time


class LoginTests(unittest.TestCase):
    
    baseURL = "https://learn.letskodeit.com/"
    driver = webdriver.Ie()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(baseURL)
    lp = LoginPage(driver)
    
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginSuccessful()
        assert result == True 
        time.sleep(2)
        self.driver.quit()
    
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcd")
        result = self.lp.verifyLoginFailed()
        assert result == True 
        
        



        