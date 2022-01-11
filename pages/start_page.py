import logging
import random
from selenium.webdriver.common.by import By
from constants.start_page import StartPageConstants
from pages.base import BasePage

from pages.main_page import MainPage
from pages.utils import log_decorator


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    @log_decorator
    def login(self, username_value, password_value):
        """Login using provided password and username"""

        self.fill_field(locator=self.constants.SIGN_IN_USERNAME_XPATH, value=username_value)
        self.fill_field(locator=self.constants.SIGN_IN_PASSWORD_XPATH, value=password_value)
        self.log.debug("fields are filled with invalid values")

        # Click on Sign In button
        button = self.wait_until_element_enabled(value=self.constants.SIGN_IN_BUTTON_XPATH)
        button.click()
        self.log.debug("clicked on Sign In")
        return MainPage(self.driver)

    @log_decorator
    def verify_incorrect_login(self):
        """Verify error message om invalid login"""

        # Find error message
        message = self.wait_until_element_enabled(value=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        # Verify message
        message = self.wait_until_find_element(value=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        assert message.text == self.constants.SIGN_IN_ERROR_MESSAGE_TEXT
        return self

    @log_decorator
    def test_link(self):
        """Link in start page is displayed"""
        link = self.wait_until_find_element(value=self.constants.LINK_XPATH)
        link.is_displayed()

    def h1_on_page(self):
        """h1 on start page is displayed"""
        h1 = self.wait_until_find_element(value=self.constants.H1_XPATH)
        h1.is_displayed()

    def placeholder(self):
        """Link in start page is displayed"""
        placeholder = self.wait_until_find_element(value=self.constants.SIGN_IN_PLACEHOLDER_XPATH)
        placeholder.is_displayed()

    @wait_until_ok()
    def _click_on_sign_up_button(self):
        """Click on button until it disappear"""
        self.wait_until_element_enabled(value=self.constants.SIGN_IN_BUTTON_XPATH).click()
        self.wait_until_element_disappear(value=self.constants.SIGN_IN_BUTTON_XPATH)
