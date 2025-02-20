from selenium.webdriver.common.by import By
import allure

class InformPage:
    """Класс для работы со страницей оформления покупок.
    Предоставляет методы для ввода данных пользователя и перехода к следующему шагу оформления заказа."""

    def __init__(self, _driver):
        """Конструктор класса InformPage.
        :param _driver: Объект веб-драйвера, который используется для взаимодействия с веб-страницей."""
        self.driver = _driver

    @allure.step('Ввод данных для оформления покупок')
    def inform(self):
        """Метод для ввода данных пользователя на странице оформления покупок.
        Вводит имя, фамилию, почтовый индекс и нажимает кнопку для продолжения оформления заказа."""
        first_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']")
        first_name.send_keys("Мария")
        last_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']")
        last_name.send_keys("Ботнарь")
        zp_code = self.driver.find_element(By.CSS_SELECTOR, "input[name='postalCode']")
        zp_code.send_keys("292940")
        cont = self.driver.find_element(By.CSS_SELECTOR, "input[class='submit-button btn btn_primary cart_button btn_action']")
        cont.click()