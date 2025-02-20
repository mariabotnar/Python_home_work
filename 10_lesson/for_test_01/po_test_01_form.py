import allure
from selenium import webdriver


from pages.FormPage import FormPage


@allure.feature('Тестирование формы')
@allure.description('Этот тест проверяет, что после заполнения формы происходит валидация цветов полей.')
@allure.severity(allure.severity_level.NORMAL)
def test_complete_the_form():
    """Тест для проверки заполнения формы и валидации цветов полей.
    Шаги:
    1. Открытие страницы и заполнение формы.
    2. Проверка цвета поля ZIP код на соответствие ожидаемому значению.
    3. Проверка цветов других полей на соответствие ожидаемому значению.
    4. Закрытие браузера после завершения теста."""
    driver = webdriver.Chrome()

    with allure.step('Открытие страницы и заполнение формы'):
        """Шаг 1: Открытие страницы с формой, заполнение всех полей и отправка формы."""
        form_page = FormPage(driver)
        form_page.complete_the_form()
        form_page.sublime_click()

    with allure.step('Проверка цвета поля ZIP код'):
        """Шаг 2: Проверка, что поле ZIP код подсвечивается красным цветом при ошибке.
        Ожидаемый цвет: rgba(248, 215, 218, 1)."""
        alert_danger_color = "rgba(248, 215, 218, 1)"
        color_zip = form_page.zip_code_red()
        assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"

    with allure.step('Проверка цветов других полей'):
        """Шаг 3: Проверка, что остальные поля подсвечиваются зеленым цветом при успешной валидации.
        Ожидаемый цвет: rgba(209, 231, 221, 1)."""
        fields_to_check = ["first-name", "last-name", "address", "e-mail", "phone",
                       "city", "country", "job-position", "company"]
        for field_name in fields_to_check:
            background_color = form_page.other_green(field_name)
            assert background_color == "rgba(209, 231, 221, 1)"

    with allure.step('Закрытие браузера'):
        """Шаг 4: Закрытие браузера после завершения теста."""
        driver.quit()
