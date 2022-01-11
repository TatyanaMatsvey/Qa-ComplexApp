import logging

from selenium.webdriver.common.by import By

from constants.main_page import MainPageConstants
from pages.base import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MainPageConstants()
        self.log = logging.getLogger(__name__)

    def verify_logout_button(self):
        """Verify sign out button"""
        logout_button = self.wait_until_element_enabled(value=self.constants.LOGOUT_BUTTON_XPATH)
        logout_button.click()
        return MainPage(self.driver)
