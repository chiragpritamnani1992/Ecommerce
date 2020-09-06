import pytest
import time
from pageObjects.AddCustomer import AddCustomer
from pageObjects.LoginPage import LoginPage
import selenium.webdriver.chrome
from datetime import datetime
from Utilities.readproperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities.wrapper import wrapper
import string
import random
import selenium

from pageObjects.SearchCustomer import SearchCustomer


class Test_SearchCustByEmail:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_searchcustomerbyEmail(self,setup):

        self.driver = setup
        driver = self.driver
        self.logger.info("************Driver Intiliazed Successful************")
        driver.get(self.baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(2)
        titleof = driver.title

        try:
            if titleof == "tt":
                print("title matched")
        except Exception as e:
            print(e)
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file('screenshot-%s.png' % now)

        # except Exception as e:
        #     print(e)
        #     now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        #     self.driver.get_screenshot_as_file('screenshot-%s.png' % now)


            # self.lp = LoginPage(driver)
            # lp= self.lp
            # lp.setUserName(self.username)
            # lp.setPassword(self.password)
            # lp.clickLogin()
            # self.logger.info("************Login Successful************")
            # self.logger.info("************Searching Customer************")


    # @pytest.mark.sanity
    # def test_searchcustomerbyTest(self,setup):
    #     self.driver = setup
    #     driver = self.driver
    #     self.logger.info("************Driver Intiliazed Successful************")
    #     driver.get(self.baseUrl)
    #     driver.maximize_window()
    #     driver.implicitly_wait(2)
    #     self.lp = LoginPage(driver)
    #     lp= self.lp
    #     lp.setUserName(self.username)
    #     lp.setPassword(self.password)
    #     lp.clickLogin()
    #     self.logger.info("************Login Successful************")
    #     self.logger.info("************Searching Customer************")
    #     self.driver.quit()
    #
    # @pytest.mark.sanity
    # def test_searchcustTest(self, setup):
    #     self.driver = setup
    #     driver = self.driver
    #     self.logger.info("************Driver Intiliazed Successful************")
    #     driver.get(self.baseUrl)
    #     driver.maximize_window()
    #     driver.implicitly_wait(2)
    #     self.lp = LoginPage(driver)
    #     lp = self.lp
    #     lp.setUserName(self.username)
    #     lp.setPassword(self.password)
    #     lp.clickLogin()
    #     self.logger.info("************Login Successful************")
    #     self.logger.info("************Searching Customer************")
    #     self.driver.quit()
    #
    # @pytest.mark.sanity
    # def test_searchcustrbyTest(self, setup):
    #     self.driver = setup
    #     driver = self.driver
    #     self.logger.info("************Driver Intiliazed Successful************")
    #     driver.get(self.baseUrl)
    #     driver.maximize_window()
    #     driver.implicitly_wait(2)
    #     self.lp = LoginPage(driver)
    #     lp = self.lp
    #     lp.setUserName(self.username)
    #     lp.setPassword(self.password)
    #     lp.clickLogin()
    #     self.logger.info("************Login Successful************")
    #     self.logger.info("************Searching Customer************")
    #     self.driver.quit()
    #
    # @pytest.mark.sanity
    # def test_searchcustomerbyTet(self, setup):
    #     self.driver = setup
    #     driver = self.driver
    #     self.logger.info("************Driver Intiliazed Successful************")
    #     driver.get(self.baseUrl)
    #     driver.maximize_window()
    #     driver.implicitly_wait(2)
    #     self.lp = LoginPage(driver)
    #     lp = self.lp
    #     lp.setUserName(self.username)
    #     lp.setPassword(self.password)
    #     lp.clickLogin()
    #     self.logger.info("************Login Successful************")
    #     self.logger.info("************Searching Customer************")
    #     self.driver.quit()
    #
    # @pytest.mark.sanity
    # def test_search(self, setup):
    #     self.driver = setup
    #     driver = self.driver
    #     self.logger.info("************Driver Intiliazed Successful************")
    #     driver.get(self.baseUrl)
    #     driver.maximize_window()
    #     driver.implicitly_wait(2)
    #     self.lp = LoginPage(driver)
    #     lp = self.lp
    #     lp.setUserName(self.username)
    #     lp.setPassword(self.password)
    #     lp.clickLogin()
    #     self.logger.info("************Login Successful************")
    #     self.logger.info("************Searching Customer************")
    #     addcustomer = AddCustomer(driver)
    #     self.driver.implicitly_wait(2)
    #     addcustomer.click_customer_menu()
    #     addcustomer.click_customer_sub_menu()
    #     self.logger.info("************Searching Customer By Email************")
    #     self.searchcust = SearchCustomer(driver)
    #     self.searchcust.setEmail("admin@yourStore.com")
    #     self.searchcust.clickSearch()
    #     time.sleep(5)
    #     status = self.searchcust.searchCustomerEmail("admin@yourStore.com")
    #     assert True == status
    #     self.logger.info("************TC Search By Email Finished************")
    #     self.driver.quit()
    #
    # @pytest.mark.sanity
    # def testvearch(self, setup):
    #     self.driver = setup
    #     driver = self.driver
    #     self.logger.info("************Driver Intiliazed Successful************")
    #     driver.get(self.baseUrl)
    #     driver.maximize_window()
    #     driver.implicitly_wait(2)
    #     self.lp = LoginPage(driver)
    #     lp = self.lp
    #     lp.setUserName(self.username)
    #     lp.setPassword(self.password)
    #     lp.clickLogin()
    #     self.logger.info("************Login Successful************")
    #     self.logger.info("************Searching Customer************")
    #     self.driver.quit()
