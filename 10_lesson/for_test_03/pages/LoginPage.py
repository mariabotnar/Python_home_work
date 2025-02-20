from selenium.webdriver.common.by import By
import allure

class LoginPage:
    """Класс для работы со страницей авторизации сайта https://www.saucedemo.com/.
    Attributes: driver: WebDriver. Экземпляр веб-драйвера, используемый для взаимодействия с браузером."""

    def __init__(self, _driver):
        """Инициализация страницы авторизации.
        Args: _driver: WebDriver. Экземпляр веб-драйвера, который будет использоваться для взаимодействия с браузером."""
        self.driver = _driver
        self.driver.get('https://www.saucedemo.com/')

    @allure.step('Ввод данных для авторизации')
    def login(self):
        """Метод для авторизации на сайте.
        Выполняет следующие действия:
        1. Находит поле для ввода имени пользователя и вводит "standard_user".
        2. Находит поле для ввода пароля и вводит "secret_sauce".
        3. Находит кнопку авторизации и нажимает её."""
        username = self.driver.find_element(By.CSS_SELECTOR, "input[name='user-name']")
        username.send_keys("standard_user")
        password = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password.send_keys("secret_sauce")
        login = self.driver.find_element(By.CSS_SELECTOR, "input#login-button")
        login.click()