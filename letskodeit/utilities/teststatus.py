import utilities.custom_logger as Cl
import logging
from base.selenium_driver import SeleniumDriver

class TestStatus(SeleniumDriver):
    
    log = Cl.customLogger(logging.INFO)
    
    def __init__(self, driver):
        super().__init__(driver) #Instantiating the parent class __init__
        self.resultList = []     #Creating a empty list for storing the results
    
    def setResult(self, result, resultMessage):
        try:
            
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.info("### VERIFICATION FAILED :: + " + resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.info("### VERIFICATION FAILED :: + " + resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.info("### Exception Occured !!!")
            
    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)
    
    def markFinal(self, testName, result, resultMessage):
        self.setResult(result, resultMessage)
        self.screenShot(testName)
        if "FAIL" in self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            self.resultList.clear()
            assert True == False 
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True 
            
    
