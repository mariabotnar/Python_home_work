from selenium.webdriver.common.by import By
import allure

class OverviewPage:
    """Класс для работы со страницей обзора заказа.
    Attributes: driver: WebDriver - экземпляр веб-драйвера для взаимодействия с браузером."""

    def __init__(self, _driver):
        """Инициализация класса OverviewPage.
        Args: _driver: WebDriver - экземпляр веб-драйвера, который будет использоваться для взаимодействия со страницей."""
        self.driver = _driver

    @allure.step('Проверка суммы стоимости товаров')
    def overview(self):
        """Получает общую стоимость товаров на странице обзора заказа.
        Returns: str: Текст, содержащий общую стоимость товаров."""
        total = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        return total