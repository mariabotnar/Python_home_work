from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, _driver):
        self.driver = _driver
        self.driver.get('https://www.saucedemo.com/')

    def login(self):
        username = self.driver.find_element(By.CSS_SELECTOR, "input[name='user-name']")
        username.send_keys("standard_user")
        password = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password.send_keys("secret_sauce")
        login = self.driver.find_element(By.CSS_SELECTOR, "input#login-button")
        login.click()
