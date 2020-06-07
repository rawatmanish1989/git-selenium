import sys
sys.path.append("C:\\Users\\Manish Rawat\\git\\repository\\letskodeit")

from selenium import webdriver
from selenium.webdriver.common.by import By 
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time

@pytest.mark.usefixtures("OneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def ClassSetup(self):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
    
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Verification for Page Title")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Test Case for the valid Login") 
        
        
    
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcd")
        result1 = self.lp.verifyLoginFailed()
        self.ts.mark(result1, "Verfication for invalid login")
        self.ts.markFinal("test_invalidLogin", result1, "Test Case for Invalid Login") 
        
        



        