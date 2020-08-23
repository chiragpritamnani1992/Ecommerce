import pytest
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime
from pageObjects.LoginPage import LoginPage
import selenium.webdriver.chrome
from datetime import datetime
from Utilities.readproperties import ReadConfig
from Utilities.customLogger import LogGen
"""
self.driver coz it is belongs to class
"""


# web_driver = None


# @pytest.fixture(params=["chrome"], scope='class')
# def init_WebDriver(request):
#     global web_driver
#     if request == "chrome":
#         web_driver = webdriver.Chrome(ChromeDriverManager().install())
#     else:
#         web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()


class Test_001_Login():
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_HomePageTitle(self, setup):
        self.logger.info("===========Test_001_Login===========")
        self.logger.info("===========Verifying Home Page Title===========")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        Act_Title = self.driver.title
        if Act_Title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("===========Home Page Title Test is Passed===========")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("===========Home Page Title Test is Failed===========")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("===========Verifying Login Test===========")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        Actual_title = self.driver.title

        if Actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("===========Login Test is Passed===========")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.logger.error("===========Login Test is Failed===========")
            assert False
