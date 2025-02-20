from selenium.webdriver.common.by import By
import allure


class FormPage:
    """Класс для работы с формой на веб-странице.
    Предоставляет методы для заполнения формы, отправки данных и проверки цветов полей."""

    def __init__(self, _driver):
        """Инициализация класса FormPage.
        Args: _driver: WebDriver, используемый для взаимодействия с веб-страницей."""
        self.driver = _driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    @allure.step('Заполнение формы')
    def complete_the_form(self):
        """Заполняет все поля формы тестовыми данными.
        Метод заполняет поля: имя, фамилия, адрес, город, страна, email, телефон, должность и компания.
        Поле ZIP-кода остаётся пустым."""
        first_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
        first_name.send_keys("Иван")

        last_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
        last_name.send_keys("Петров")

        address = self.driver.find_element(By.CSS_SELECTOR, "input[name='address']")
        address.send_keys("Ленина, 55-3")

        zip_code = self.driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
        zip_code.send_keys("")

        city = self.driver.find_element(By.CSS_SELECTOR, "input[name='city']")
        city.send_keys("Москва")

        country = self.driver.find_element(By.CSS_SELECTOR, "input[name='country']")
        country.send_keys("Россия")

        email = self.driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
        email.send_keys("test@skypro.com")

        phone_number = self.driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
        phone_number.send_keys("+7985899998787")

        job_position = self.driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
        job_position.send_keys("QA")

        company = self.driver.find_element(By.CSS_SELECTOR, "input[name='company']")
        company.send_keys("SkyPro")

    @allure.step('Клик на кнопку')
    def sublime_click(self):
        """Нажимает кнопку отправки формы."""
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    @allure.step('Проверка поля красного цвета')
    def zip_code_red(self):
        """Проверяет, что поле ZIP-кода выделено красным цветом.
        Returns: str: Значение CSS-свойства 'background-color' для поля ZIP-кода."""
        zip_code = self.driver.find_element(By.CSS_SELECTOR, "#zip-code")
        return zip_code.value_of_css_property("background-color")

    @allure.step('Проверка полей зелёного цвета')
    def other_green(self, field_name):
        """Проверяет, что указанное поле выделено зелёным цветом.
        Args: field_name (str): Имя поля, которое нужно проверить.
        Returns: str: Значение CSS-свойства 'background-color' для указанного поля."""
        field = self.driver.find_element(By.CSS_SELECTOR, f"#{field_name}")
        return field.value_of_css_property("background-color")