from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from traceback import print_stack
import utilities.custom_logger as cl
import utilities.custom_datetime as cdt
import logging
import time
import os 



class SeleniumDriver():
    
    
    log = cl.customLogger(logging.DEBUG)
    
    
    def __init__(self, driver):
        self.driver = driver
        
    
    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("locator Type " + locatorType + "not supported/correct")
    
    
    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and locatorType: " + locatorType)
        return element
    
    def getElementList(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator + " and locatorType: " + locatorType)
        return element
    
    def elementClick(self, locator, locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Can't Click on element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()
    
    def sendKeys(self, data, locator, locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Can't send data : " + data + " on element with locator: " + locator + " locatorType: " + locatorType)
    
    def getText(self, locator, locatorType="id", element=None, info=""):
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text()
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text
    
    
    def isElementPresent(self, locator, locatorType = "id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True 
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not Found")
            return True 
    
    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator + "locatorType: " + locatorType)
            else:
                self.log.info("Element is not displayed with locator: " + locator + "locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False
        
    
    def elmentPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0 :
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False
        
    def getTitle(self):
            return self.driver.title
        
    def screenShot(self, resultMessage):
        self.current_datetime = cdt.customDateTime()
        
        fileName = resultMessage + "_" + self.current_datetime + ".png"
        currentDirectory = os.getcwd()
        Directory1 = os.path.dirname(currentDirectory)
        screenshotsDirectory = os.path.dirname(Directory1) + "\\screenshots"
        destinationFileName = screenshotsDirectory + "\\" + fileName
        
        try:
            if not os.path.exists(screenshotsDirectory):
                os.makedirs(screenshotsDirectory)
            self.driver.save_screenshot(destinationFileName)
            self.log.info("Screenshot save to directory: " + screenshotsDirectory)
        except:
            self.log.error("### Exception occurred while taking screenshots")
            print_stack()    
                
        
    
    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element
    
    def webScroll(self, direction=""):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")   
        
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 750);") 
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    