import allure
from selenium import webdriver


from pages.LoginPage import LoginPage
from pages.CartPage import CartPage
from pages.InformPage import InformPage
from pages.OverviewPage import OverviewPage


@allure.feature('Тестирование магазина')
@allure.description('Этот тест проверяет, что подсчёт суммы товаров при покупке в интернет-магазине соответствует ожидаемому результату.')
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    """Тест для проверки функциональности интернет-магазина.
    Шаги теста:
    1. Открытие страницы логина и авторизация.
    2. Добавление товаров в корзину.
    3. Заполнение информации о пользователе.
    4. Проверка итоговой суммы заказа.
    5. Закрытие браузера.
    Ожидаемый результат: - Итоговая сумма заказа должна быть равна 'Total: $58.29'."""
    driver = webdriver.Chrome()

    with allure.step('Открытие страницы логина'):
        login_page = LoginPage(driver)
        login_page.login()

    with allure.step('Добавление товаров в корзину'):
        cart_page = CartPage(driver)
        cart_page.cart()

    with allure.step('Заполнение информации о пользователе'):
        inform_page = InformPage(driver)
        inform_page.inform()

    with allure.step('Проверка итоговой суммы'):
        overview_page = OverviewPage(driver)
        result = overview_page.overview()
        assert result == 'Total: $58.29'

    with allure.step('Закрытие браузера'):
        driver.quit()