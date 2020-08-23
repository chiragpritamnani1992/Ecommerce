from selenium.webdriver.common.by import By
from Utilities.wrapper import wrapper
import time
from selenium import webdriver


class AddCustomer:
    customer_menu_xpath = "//span[text()='Customers']//parent::a//i[contains(@class,'fa-angle-left pull-right')]"
    customer_menuitem_xpath = "//span[@class='menu-item-title' and text()='Customers']"
    btn_addcustomer = "//a[contains(@class,'btn bg-blue')]"
    txt_email_xpath = "//input[@name='Email']"
    txt_company_xpath = "//input[@name='Company']"
    txt_fname_xpath = "//input[@name='FirstName']"
    txt_lname_xpath = "//input[@name='LastName']"
    txt_ip_xpath = "//input[@name='SearchIpAddress']"
    txt_pass_xpath = "//input[@name='Password']"
    radio_Male = "//input[@name='Gender' and @value='M']"
    radio_FeMale = "//input[@name='Gender' and @value='F']"
    txt_dob_xpath = "//input[@name='DateOfBirth']"
    # drp_customer_role_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']/ul[@id='SelectedCustomerRoleIds_taglist']"
    drp_customer_role_xpath = "//div[@class='label-wrapper']/label[text()='Customer roles']/../..//following-sibling::div[@class='col-md-9']//following-sibling::div[@class='k-widget k-multiselect k-multiselect-clearable']"
    txt_admin_comment_xpath = "//textarea[@id='AdminComment']"
    btn_save = "//button[@name='save']"
    drp_vendor_xpath = "//select[@id='VendorId']"
    drp_newletter_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']/ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']"
    input_tax_xpath = "//input[@id='IsTaxExempt']"
    list_registered_xpath = "//li[contains(text(),'Registered')]"
    list_admin_xpath = "//li[contains(text(),'Administrators')]"
    list_guest_xpath = "//li[contains(text(),'Guests')]"
    list_vendor_xpath = "//li[contains(text(),'Vendors')]"

    def __init__(self, driver):
        self.driver = driver

    def click_customer_menu(self):
        self.driver.find_element_by_xpath(self.customer_menu_xpath).click()
        #wrapper.click_link_btn_byXpath(self.driver, self.customer_menu_xpath)

    def click_customer_sub_menu(self):
        self.driver.find_element_by_xpath(self.customer_menuitem_xpath).click()
        #wrapper.click_link_btn_byXpath(self.driver, self.customer_menuitem_xpath)

    def add_new_customer(self):
        wrapper.click_link_btn_byXpath(self.driver, self.btn_addcustomer)

    def setEmail(self, email):
        wrapper.enter_text_byXpath(self.driver, self.txt_email_xpath, email)

    def setPassword(self, password):
        wrapper.enter_text_byXpath(self.driver, self.txt_pass_xpath, password)

    def setCustomerRole(self, role):
        wrapper.click_link_btn_byXpath(self.driver, self.drp_customer_role_xpath)
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.list_registered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.list_admin_xpath)
        elif role == "Guests":
            time.sleep(3)
            # self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.list_guest_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.list_registered_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.list_vendor_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.list_registered_xpath)
        time.sleep(3)
        wrapper.javaScriptExecutor(self.driver, self.listitem)

    def selectManagerofVendor(self, value):
        wrapper.selectDropDownValue(self.driver, self.drp_vendor_xpath, value)

    def setGender(self, value):

        if value == "male":
            wrapper.selectRadioButton(self.driver, self.radio_Male, value)
        else:
            wrapper.selectRadioButton(self.driver, self.radio_FeMale, value)

    def setFname(self, value):
        wrapper.enter_text_byXpath(self.driver, self.txt_fname_xpath, value)

    def setLname(self, value):
        wrapper.enter_text_byXpath(self.driver, self.txt_lname_xpath, value)

    def setIp(self, value):
        wrapper.enter_text_byXpath(self.driver, self.txt_ip_xpath, value)

    def clickSave(self):
        wrapper.click_link_btn_byXpath(self.driver, self.btn_save)

    def setDob(self, value):
        wrapper.enter_text_byXpath(self.driver, self.txt_dob_xpath, value)

    def setCompany(self, value):
        wrapper.enter_text_byXpath(self.driver, self.txt_company_xpath, value)

    def setAdminComment(self,value):
        wrapper.enter_text_byXpath(self.driver, self.txt_admin_comment_xpath,value)

    def clickonSave(self):
        wrapper.click_link_btn_byXpath(self.driver, self.btn_save)