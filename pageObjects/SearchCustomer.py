from selenium.webdriver.common.by import By
from selenium import webdriver
from Utilities.wrapper import wrapper
import time


class SearchCustomer(wrapper):
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
        super().__init__(driver)

    def setEmail(self, email):
        wrapper.enter_text_byXpath(self, self.txt_search_email, email)

    def setFName(self, lname):
        wrapper.enter_text_byXpath(self, self.txt_search_fname, lname)

    def setLName(self, fname):
        wrapper.enter_text_byXpath(self, self.txt_search_lname, fname)

    def clickSearch(self):
        wrapper.click_link_btn_byXpath(self, self.search_btn)

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
