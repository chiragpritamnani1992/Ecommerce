import pytest
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pageObjects.LoginPage import LoginPage
import selenium.webdriver.chrome


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome Browser........")
    elif browser == "ff":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Launching FireFox Browser........")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome Browser........")
    return driver


"""

for command line argument 
pytest testCases\Login_TestCase.py -s -v --browser chrome

If u want to run test in parallel mode
pytest testCases\Login_TestCase.py -s -v --browser chrome -n 2 
n means of no of workers 

"""


def pytest_addoption(parser):  # this will get the value from cli or hooks
    parser.addoption("--browser")


@pytest.fixture()  # this will return the browser
def browser(request):
    return request.config.getoption("--browser")


########## pytest html report ##############

# hooks to be added in Enviroment info to HTMl Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Chirag'


# Hooks to delete/modify env info in the HTML Report

@pytest.mark.optionalhook
def pytest_metatdata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
