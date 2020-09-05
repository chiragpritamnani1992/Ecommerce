import pytest
import time
from pageObjects.AddCustomer import AddCustomer
from Utilities.wrapper import wrapper

from pageObjects.LoginPage import LoginPage
import selenium.webdriver.chrome
from datetime import datetime
from Utilities.readproperties import ReadConfig
from Utilities.customLogger import LogGen
import string
import random
import selenium

from pageObjects.SearchCustomer import SearchCustomer


class Test_SearchCustByEmail:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    def test_searchcustomerbyEmail(self,setup):
        self.logger.info("************TC 004 Search Customer************")
        self.driver = setup
        driver = self.driver
        driver.get(self.baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(2)
        self.lp = LoginPage(driver)
        lp= self.lp
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************Login Successful************")
        self.logger.info("************Searching Customer************")
        addcustomer = AddCustomer(driver)
        self.driver.implicitly_wait(2)
        addcustomer.click_customer_menu()
        addcustomer.click_customer_sub_menu()
        self.logger.info("************Searching Customer By Email************")
        self.searchcust = SearchCustomer(driver)
        self.searchcust.setEmail("admin@yourStore.com")
        self.searchcust.clickSearch()
        time.sleep(5)
        status = self.searchcust.searchCustomerEmail("admin@yourStore.com")
        assert True == status
        self.logger.info("************TC Search By Email Finished************")