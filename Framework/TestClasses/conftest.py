
import pytest
from selenium import webdriver

from Utility.readProperties import ReadConfig

#step3: modify fixture for multiple browser
@pytest.fixture
def openbrowser(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()

        driver.get(ReadConfig.getAppUrl())
        driver.implicitly_wait(5)
        return driver

#Step2: use to get browser name from command - line & pass value browser to openbrowser fixture
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#step1: set default value of browser
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",
                     help="provide browser name - chrome, firefox, edge, etc")