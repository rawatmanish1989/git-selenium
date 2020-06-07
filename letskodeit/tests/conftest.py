import pytest
from selenium import webdriver
from pages.home.login_page import LoginPage
from base.webdriverfactory import WebDriverFactory

@pytest.fixture()
def setUp():
    print("Running method level setup")
    yield 
    print("Running method level tearDown")
    
@pytest.fixture(scope="class")
def OneTimeSetUp(request, browser):
    print("Running one time setup")
    
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    
   
    print("**********Running the test cases in " + browser + "**********")
    
    
    if request.cls is not None:
        request.cls.driver = driver
        
    yield driver
    print("***************Running one time tearDown****************************")
    driver.quit()
    print("***************Quitting the browser*******************************")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
    