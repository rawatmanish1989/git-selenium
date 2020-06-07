"""
Webdriver Factory class implementation
It crates a webdriver instance based on browser configurations

"""

from selenium import webdriver
import traceback

class WebDriverFactory():
    
    def __init__(self, browser):
        self.browser = browser
        
    
    def getWebDriverInstance(self):
        """
        This method returns the webdriver instance based on browser configurations
    
        """
        baseURL = "https://letskodeit.teachable.com"
        if self.browser == "ie":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(baseURL)
        return driver 
         
    
        