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


class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    #
    def test_AddCust(self, setup):
        self.logger.info("************TC 003 Add Customer************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************Login Successful************")
        self.logger.info("************Adding Customer************")
        addcustomer = AddCustomer(self)
        self.driver.implicitly_wait(2)
        addcustomer.click_customer_menu()
        addcustomer.click_customer_sub_menu()
        addcustomer.add_new_customer()
        self.logger.info("************Providing Customer Details************")
        self.email = random_generator() + "@gmail.com"
        addcustomer.setEmail(self.email)
        addcustomer.setPassword("Teaser")
        addcustomer.setFname("Raj")
        addcustomer.setLname("Par")
        addcustomer.setGender("female")
        addcustomer.setDob("1/1/2004")
        addcustomer.setCompany("Google")
        # addcustomer.setCustomerRole("Vendors")
        addcustomer.setAdminComment("This is for Testing")
        addcustomer.clickonSave()
        self.logger.info("************Customer Details Added************")
        self.logger.info("************Customer Validation Started************")

        message = self.driver.find_element_by_tag_name("body").text
        print(message)

        if "The new customer has been added successfully." in message:
            assert True == True
            self.logger.info("************Customer Added Successful************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_customer.png")
            assert True == False
            self.logger.error("************Add customer test Failed************")

        self.driver.close()
        self.logger.info("************Ending Add Customer Page************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return '' .join(random.choice(chars) for x in range(size))
