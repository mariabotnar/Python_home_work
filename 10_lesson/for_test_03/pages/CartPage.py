from selenium.webdriver.common.by import By
import allure

class CartPage:
    """Класс для работы со страницей корзины интернет-магазина.
    Attributes: driver: WebDriver - экземпляр веб-драйвера для взаимодействия с браузером."""

    def __init__(self, _driver):
        """Конструктор класса CartPage.
        Args: _driver: WebDriver - экземпляр веб-драйвера, который будет использоваться для взаимодействия со страницей."""
        self.driver = _driver

    @allure.step('Выбор товаров')
    def cart(self):
        """Метод для добавления товаров в корзину и перехода к оформлению заказа.
        Шаги:
        1. Добавляет товар "Sauce Labs Backpack" в корзину.
        2. Добавляет товар "Sauce Labs Bolt T-Shirt" в корзину.
        3. Добавляет товар "Sauce Labs Onesie" в корзину.
        4. Переходит в корзину, нажимая на иконку корзины.
        5. Нажимает кнопку "Checkout" для перехода к оформлению заказа."""
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        basket = self.driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
        basket.click()
        checkout = self.driver.find_element(By.XPATH, "//*[@id='checkout']")
        checkout.click()