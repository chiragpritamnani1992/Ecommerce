from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class wrapper:

    def __init__(self, driver):
        self.driver = driver

    def click_link_btn_byXpath(self, web_element):
        self.driver.find_element(By.XPATH, web_element).click()

    def enter_text_byXpath(self, web_element, value):

        try:
            ele = self.driver.find_element(By.XPATH, web_element)
            ele.clear()
            ele.send_keys(value)
        except NoSuchElementException:
            pass

    def javaScriptExecutor(self, web_element):
        self.driver.execute_script("arguments[0].click();", web_element)

    def listValue(self, web_element):
        self.driver.find_element(By.XPATH, web_element)

    def selectDropDownValue(self, web_element, value):
        drp = Select(self.driver.find_element(By.XPATH, web_element))
        drp.select_by_visible_text(value)

    def selectRadioButton(self, web_element, value):
        self.driver.find_element(By.XPATH, web_element).click()