import logging
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.wait = WebDriverWait(driver, timeout=5)

    def fill_field(self, by, locator, value):
        """Fill field using provided variables"""
        username = self.wait_until_find_element(by=by, value=locator)
        # username = self.driver.find_element(by=by, value=locator)
        username.clear()
        username.send_keys(value)

    def wait_until_find_element(self, by, value):
        """Wait until find element"""
        return self.wait.until(EC.presence_of_element_located(locator=(by, value)))
