from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    text_field_email = "Email"
    text_field_password = "Password"
    login_button = "//input[@type='submit']"
    logout_btn = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.text_field_email).clear()
        self.driver.find_element_by_id(self.text_field_email).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.text_field_password).clear()
        self.driver.find_element_by_id(self.text_field_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_btn).click()


"""
self.driver is intiating  class variable
"""
