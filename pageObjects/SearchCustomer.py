from Utilities.wrapper import wrapper


class SearchCustomer():
    txt_search_email = "//input[@name='SearchEmail']"
    txt_search_fname = "//input[@name='SearchFirstName']"
    txt_search_lname = "//input[@name='SearchLastName']"
    search_btn = "//button[@id='search-customers']"

    table_xpath = "//table[@id='customers-grid']"
    table_row_xpath = "//table[@id='customers-grid']/tbody/tr"
    table_col_xpath = "//table[@id='customers-grid']/tbody/tr/td"
    table_searchresult_xpath = "//table[@role='grid']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        wrapper.enter_text_byXpath(self.driver, self.txt_search_email, email)

    def setFName(self, password):
        wrapper.enter_text_byXpath(self.driver, self.txt_search_fname, password)

    def setLName(self, password):
        wrapper.enter_text_byXpath(self.driver, self.txt_search_lname, password)

    def clickSearch(self):
        wrapper.click_link_btn_byXpath(self.driver, self.search_btn)

    def getNoRows(self):
        return len(self.driver.find_elements_by_xpath(self.table_row_xpath))

    def getNoCols(self):
        return len(self.driver.find_elements_by_xpath(self.table_col_xpath))

    def searchCustomerEmail(self, email):
        flag = False
        for r in range(1, self.getNoRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + ")]/td[2]").text
            if email == email:
                flag = True
                break
        return flag

    def searchCustomerName(self, name):
        flag = False
        for r in range(1, self.getNoRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name_id = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + ")]/td[3]").text
            if name_id == name:
                flag = True
                break
        return flag
