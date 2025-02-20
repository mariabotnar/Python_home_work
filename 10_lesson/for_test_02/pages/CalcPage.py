from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    """Класс для работы с веб-страницей калькулятора.
    Предоставляет методы для взаимодействия с элементами на странице калькулятора,
    включая ввод задержки, выполнение арифметических операций и проверку результата."""

    def __init__(self, _driver):
        """Инициализация класса CalcPage.
        :param _driver: WebDriver, используемый для взаимодействия с браузером."""
        self.driver = _driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    @allure.step('Ввод задержки')

    def delay(self):
        """Устанавливает задержку выполнения операций на калькуляторе.
        Метод находит поле ввода задержки, очищает его и устанавливает значение 45."""
        delay = self.driver.find_element(By.CSS_SELECTOR, 'input#delay')
        delay.clear()
        delay.send_keys('45')

    @allure.step('Ввод данных для арифметического действия')
    def calculator(self):
        """Выполняет арифметическую операцию на калькуляторе.
        Метод последовательно нажимает кнопки для ввода числа 7, операции сложения, числа 8 и кнопки "равно".
        Затем ожидает появления результата на экране."""
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

        WebDriverWait(self.driver, 46).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    @allure.step('Проверка результата')
    def result(self) -> int:
        """Получает результат вычисления с экрана калькулятора.
        :return: Результат вычисления в виде целого числа."""
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return int(result)