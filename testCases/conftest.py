import pytest
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pageObjects.LoginPage import LoginPage
import selenium.webdriver.chrome
from Configurations import configuration as cf

driver = None


@pytest.fixture()
def setup(browser):
    if browser == "chrome" and cf.Grid_Browser == "Jenkins":
        driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.CHROME.copy(),
                                  command_executor='http://localhost:4444/wd/hub')
        print("Launching Chrome Browser........")

    elif browser == "ff" and cf.Grid_Browser == "Jenkins":
        driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX.copy(),
                                  command_executor='http://localhost:4444/wd/hub')
        print("Launching FF  Browser........")
    elif browser == "IE" and cf.Grid_Browser == "Jenkins":
        driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.INTERNETEXPLORER.copy(),
                                  command_executor='http://localhost:4444/wd/hub')
        print("Launching IE  Browser........")
    elif browser == "FF":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Launching FF  Browser........")
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

For Grouping  : to run grouping test

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
