from selenium.webdriver.common.by import By
from selenium import webdriver
from Utilities.wrapper import wrapper
import time


class SearchCustomer():
    txt_search_email = "//input[@name='SearchEmail']"
    txt_search_fname = "//input[@name='SearchFirstName']"
    txt_search_lname = "//input[@name='SearchLastName']"
    search_btn = "//button[@id='search-customers']"

    table_xpath = "//table[@id='customers-grid']"
    table_row_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_col_xpath = "//table[@id='customers-grid']//tbody/tr/td"
    table_searchresult_xpath = "//table[@role='grid']"
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txt_search_email).send_keys(email)
        #wrapper.enter_text_byXpath(self.driver, self.txt_search_email, email)

    def setFName(self, lname):
        self.driver.find_element_by_xpath(self.txt_search_fname).send_keys(lname)
        #wrapper.enter_text_byXpath(self.driver, self.txt_search_fname, password)

    def setLName(self, fname):
        self.driver.find_element_by_xpath(self.txt_search_lname).send_keys(fname)
        #wrapper.enter_text_byXpath(self.driver, self.txt_search_lname, password)

    def clickSearch(self):
        self.driver.find_element_by_xpath(self.search_btn).click()
        #wrapper.click_link_btn_byXpath(self.driver, self.search_btn)

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath("//table[@id='customers-grid']//tbody/tr"))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.table_col_xpath))

    def searchCustomerEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']")
            email_id = table.find_element(By.XPATH,
                                          "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if email_id == email:
                flag = True
                break
        return flag

    def searchCustomerName(self, name):
        flag = False
        for r in range(1, 10):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name_id = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]")[
                0].text
            if name_id == name:
                flag = True
                break
        return flag
