import allure
from selenium import webdriver


from pages.CalcPage import CalcPage


@allure.feature('Тестирование калькулятора')
@allure.description('Этот тест проверяет, что сумма двух чисел вычисляется корректно.')
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    """Тест проверяет функциональность калькулятора.
    Шаги теста:
    1. Открытие страницы калькулятора.
    2. Выполнение расчёта.
    3. Получение результата.
    4. Проверка результата.
    5. Закрытие браузера.
    Ожидаемый результат: результат вычислений должен быть равен 15."""
    driver = webdriver.Chrome()

    with allure.step('Открытие страницы калькулятора'):
        calc_page = CalcPage(driver)
        calc_page.delay()

    with allure.step('Выполнение расчёта'):
        calc_page.calculator()

    with allure.step('Получение результата'):
        result = calc_page.result()

    with allure.step('Проверка результата'):
        driver.quit()

    with allure.step('Проверка результата'):
        assert result == 15

    with allure.step('Закрытие браузера'):
        driver.quit()