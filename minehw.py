import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def random_num(self):
        """Generate random number"""
        return str(random.choice(range(11111, 99999)))

    # 1 Валидация поля Username
    def test_invalid_username(self):
        '''Test invalid username and invalid password'''
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        username.send_keys(f"userName{self.random_num()}")
        sleep(3)
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys(f"Pwd{self.random_num()}")
        sleep(3)
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert message.text == "Error"

    def test_valid_username(self):
        '''Positive test with valid username and valid pass'''

        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        username.send_keys("tatyanam")
        sleep(3)
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys("1234567890qwerty")
        sleep(3)
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        logout = driver.find_element(by=By.XPATH, value=".//html/body/header/div/div/form/button")

    def test_comby_1(self):
        '''Test invalid username and valid password'''
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        username.send_keys(f"userName{self.random_num()}")
        sleep(3)
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys("1234567890qwerty")
        sleep(3)
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert message.text == "Error"

    def test_comby_2(self):
        '''Test valid username and invalid password'''
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        username.send_keys("tatyanam")
        sleep(3)
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys(f"Pwd{self.random_num()}")
        sleep(3)
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert message.text == "Error"

    # 2 Наличие Placeholder в поле Password
    def test_placeholder(self):
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        placeholder = driver.find_element(by=By.XPATH,
                                          value=".//input[@name='password' and @class='form-control form-control-sm input-dark']")
        sleep(3)

    # 3 Кликабельность кнопки Sign in - $x(".//button[@class='btn btn-primary btn-sm']")
    def test_sign_in(self):
        '''Positive test with valid username and valid pass'''

        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        username.send_keys("tatyanam")
        sleep(3)
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys("1234567890qwerty")
        sleep(3)
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        logout = driver.find_element(by=By.XPATH, value=".//html/body/header/div/div/form/button")

        # 4 Работоспособность рефки

    def test_link(self):
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        link = driver.find_element(by=By.XPATH, value=".//a[@href='/'and @class='text-white']")
        link.click()
        sleep(3)

        # 5 Наличие h1 на странице

    def test_h1(self):
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        h1 = driver.find_element(by=By.XPATH, value=".//H1")
        # тут хочу сравнить текст найденного h1 с значением на стартовой странице, что бы было Тру, но не знаю как
        sleep(3)
