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
from Utilities.ExcelUtility import *
from Utilities import ExcelUtility
import time


class Test_001_Login():
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = "D:\\NopCommerceApp\\TestData\\LoginTest.xlsx"

    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("===========Test_001_Login===========")
        self.logger.info("===========Verifying Login DDT Test===========")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtility.getRowCount(self.path, "Login")
        print("No of rows in sheet", self.rows)
        list_status = []
        for i in range(2, self.rows + 1):  # it will not take the last , hence +1
            self.username = ExcelUtility.readDataFile(self.path, "Login", i, 1)
            self.password = ExcelUtility.readDataFile(self.path, "Login", i, 2)
            self.expected = ExcelUtility.readDataFile(self.path, "Login", i, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            Actual_title = self.driver.title
            Expected_title = "Dashboard / nopCommerce administration"

            if Actual_title == Expected_title:
                if self.expected == "pass":
                    self.logger.info("-***************Test Case Passed-***************")
                    time.sleep(3)
                    self.lp.clickLogout()
                    list_status.append("pass")
                elif self.expected == "fail":
                    self.logger.info("-***************Test Case Failed-***************")
                    time.sleep(3)
                    self.lp.clickLogout()
                    list_status.append("fail")
            if Actual_title != Expected_title:
                if self.expected == "pass":
                    self.logger.info("-***************Test Case Failed-***************")
                    list_status.append("fail")
                elif self.expected == "false":
                    self.logger.info("-***************Test Case Passed-***************")
                    list_status.append("pass")

        if "fail" not in list_status:
            self.logger.info("-***************Test_001_Login_DDT_Passed-***************")
            self.driver.close()
            assert True
        else:
            self.logger.info("-***************Test_001_Login_DDT_Failed-***************")
            self.driver.close()
            assert False

        self.logger.info("-***************Test_001_Completed-***************")
        self.logger.info("-***************Browser Closed-***************")
