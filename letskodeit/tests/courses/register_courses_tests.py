from selenium import webdriver
from pages.courses.register_courses_page import RegisterCoursePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import pytest
import unittest
import time 

@pytest.mark.usefixtures("OneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def classSetup(self, OneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.courses = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)
    
    
    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.lp.login("test@email.com", "abcabc")
        self.courses.enrollCourse(num="4200 0000 0000 0000", exp="12/24", cvv="546", code="11005")
        result1 = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result1, "Test case for the invalid Enrollment")
    
    
    
