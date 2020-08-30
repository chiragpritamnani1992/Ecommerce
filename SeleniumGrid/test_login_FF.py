import pytest
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = None


def setup_module(module):
    global driver

    driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.INTERNETEXPLORER.copy(),
                              command_executor='http://192.168.1.103:4646/wd/hub')
    driver.implicitly_wait(4)
    driver.get("https://admin-demo.nopcommerce.com/login")


def test_01():
    title = driver.title
    print(driver.title)


def teardown_module(module):
    driver.quit()
