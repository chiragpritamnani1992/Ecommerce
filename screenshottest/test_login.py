from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Test_login():


    @pytest.fixture()
    def setUp(self):
        global driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_01(self, setUp):
        tt = self.driver.title
        print(tt)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.screenshot(setUp)
        try:
            if tt == "YTest":
                print("Matched")
        except Exception as e:
            print("Exception Caught" + str(e))

    def screenshot(self,setUp):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.driver.get_screenshot_as_file('Screenshots\\Test_login-%s.png' % now)


#System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "sandbox allow-scripts; default-src 'self'; script-src * 'unsafe-eval'; img-src *; style-src * 'unsafe-inline'; font-src *");
#System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")