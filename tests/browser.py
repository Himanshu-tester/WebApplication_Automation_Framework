import pytest

from selenium import webdriver


@pytest.mark.usefixtures("driverSetup")
class browser():
    def browser(self):
        return self.driver.get("http://automationpractice.com/index.php")
        return self.driver.maximize_window()