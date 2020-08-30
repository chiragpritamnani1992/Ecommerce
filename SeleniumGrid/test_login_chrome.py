import pytest
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime
from pageObjects.LoginPage import LoginPage
import selenium.webdriver.chrome
from datetime import datetime
from Utilities.readproperties import ReadConfig
from Utilities.customLogger import LogGen

driver = None


def setup_module(module):
    global driver

    driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.CHROME.copy(),
                              command_executor='http://192.168.1.103:4545/wd/hub')
    driver.implicitly_wait(4)
    driver.get("https://admin-demo.nopcommerce.com/login")


def test_01():
    title = driver.title
    print(driver.title)


def teardown_module(module):
    driver.quit()
