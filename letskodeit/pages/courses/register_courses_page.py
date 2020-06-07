from base.basepage import BasePage
import time
import utilities.custom_logger as Cl
import logging


class RegisterCoursePage(BasePage):
    
    log = Cl.customLogger(logging.INFO)
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    #locators
    _search_box = "search-courses"   #id
    _search_button = "search-course-button" #id
    _course = "//div[@title='{0}']"  #xpath
    _enroll_button = "enroll-button-top"  #id
    _cc_num = "cardnumber" #name
    _cc_exp = "exp-date"  #name
    _cc_cvv = "cvc" #name
    _check_box = "agreed_to_terms_checkbox"  #id
    _postal_code = "postal" #name 
    _sbmit_enroll = "confirm-purchase" #id
    _enroll_error_message = "//div[@class='payment-error-box only-on-mobile']//span[contains(text(),'The card was declined.')]" #xpath
    _iframe_1 = "//div[@id='credit_card_number']//iframe"
    _iframe_2 = "//div[@id='expiration']//iframe"
    _iframe_3 = "//div[@id='cvc']//iframe"
    _iframe_4 = "//div[@id='postal']//iframe"
    
    
    
    #Actions
    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box)
    
    def clickSearchButton(self):
        self.elementClick(self._search_button)
    
    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(self._course.format(fullCourseName), locatorType="xpath")
    
    def clickOnEnrollButton(self):
        self.elementClick(self._enroll_button)
    
    def enterCardNum(self, num):
        self.driver.switch_to.frame(self.getElement(self._iframe_1, locatorType="xpath"))
        self.sendKeys(num, self._cc_num, locatorType="name")
        self.driver.switch_to.default_content()
        
    def enterCardExp(self, exp):
        self.driver.switch_to.frame(self.getElement(self._iframe_2, locatorType="xpath"))
        self.sendKeys(exp, self._cc_exp, locatorType="name")
        self.driver.switch_to.default_content()
    
    def enterCardCVV(self, cvv):
        self.driver.switch_to.frame(self.getElement(self._iframe_3, locatorType="xpath"))
        self.sendKeys(cvv, self._cc_cvv, locatorType="name")
        self.driver.switch_to.default_content()
    
    def enterPostalCode(self, code):
        self.driver.switch_to.frame(self.getElement(self._iframe_4, locatorType="xpath"))
        self.sendKeys(code, self._postal_code, locatorType="name")
        self.driver.switch_to.default_content()
        
    def clickCheckBox(self):
        self.elementClick(self._check_box)
    
    def clickEnrollSubmitButton(self):
        self.elementClick(self._sbmit_enroll)
    
    def enterCreditCardInformation(self, num, exp, cvv, code):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterPostalCode(code)
        
        
    def enrollCourse(self, num="", exp="", cvv="", code=""):
        self.enterCourseName("JavaScript")
        self.clickSearchButton()
        self.selectCourseToEnroll("JavaScript for beginners")
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        
        self.enterCreditCardInformation(num, exp, cvv, code)
        self.clickCheckBox()
        self.clickEnrollSubmitButton()
    
    def verifyEnrollFailed(self):
        errorMsgElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=errorMsgElement)
        return result 
    
    
        
    
        