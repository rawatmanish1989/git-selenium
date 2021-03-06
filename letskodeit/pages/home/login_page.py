from selenium.webdriver.common.by import By
from base.basepage import BasePage
import logging
import utilities.custom_logger as Cl



class LoginPage(BasePage):
    
    log = Cl.customLogger(logging.DEBUG)
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    
    def clickLoginLink(self):
        self.elementClick(self._login_link, "linktext")
        
    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)
        
    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)
        
    def clickLoginButton(self):
        self.elementClick(self._login_button, "name")
    
    def clearFields(self):
        emailField = self.getElement(self._email_field)
        emailField.clear()
        passwordField = self.getElement(self._password_field)
        passwordField.clear()
        
    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
    
    
    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//div[@id='navbar']//span[text()='Test']", locatorType="xpath")
        return result
    
    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(), 'Invalid email or password')]", locatorType="xpath")
        return result
    
    def verifyTitle(self):
        print(self.getTitle())
        if "Let's Kode It" in self.getTitle():
            return True
        else:
            return False 
        