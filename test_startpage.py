from time import sleep

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from constants import start_page
from constants.base import BaseConstants
from pages.main_page import MainPage
from pages.start_page import StartPage


class TestStartPage:

    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.WebDriver(BaseConstants.DRIVER_PATH)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def start_page(self, driver):
        """Return start page object"""
        driver.get(BaseConstants.URL)
        return StartPage(driver)

    @pytest.fixture(scope="function")
    def main_page(self, driver):
        """Return start page object"""
        driver.get(BaseConstants.URL)
        return MainPage(driver)

    # 1 Валидация login
    def test_invalid_username(self, start_page):
        """Test invalid username and invalid password"""
        start_page.login("qqq11", "11w2")

    def test_valid_username(self, start_page, main_page):
        """Positive test with valid username and valid pass"""
        start_page.login("TatyanaMa", "TatyanaMaTatyanaMa")
        main_page.verify_logout_button()

    # 2 Наличие Placeholder в поле Password
    def test_placeholder(self, start_page):
        start_page.placeholder()

    # 3 Кликабельность кнопки Sign in
    def test_sign_in(self, start_page, main_page):
        """Positive test with valid username and valid pass"""
        start_page.login("TatyanaMa", "TatyanaMaTatyanaMa")
        main_page.verify_logout_button()

    # 4 Работоспособность рефки на странице авторизации/регистрации
    def test_link(self, start_page):
        start_page.test_link()

    # 5 Наличие h1 на странице авторизации/регистрации
    def test_h1(self, start_page):
        start_page.h1_on_page()
