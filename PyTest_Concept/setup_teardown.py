import pytest
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class Test_PyTest_Concept():
    driver = None

    def setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.google.com/")

    def test_01(self):
        var = driver.title
        print(var)

    @pytest.mark.skip
    def test_02(self):
        var = driver.title
        print(var)

    @pytest.mark.skip
    def test_03(self):
        var = driver.title
        print(var)

    def test_04(self):
        var = driver.title
        print(var)

    def teardown(self):
        driver.quit()
