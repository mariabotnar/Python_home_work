import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# создаём WebDriver
@pytest.fixture
def driver():
    # указываем путь к драйверу
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# создаём условия для теста
def test_02_calc(driver):
    # открываем страницу
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    # вводим задержку
    delay = driver.find_element(By.CSS_SELECTOR, 'input#delay')
    # очищаем поле
    delay.clear()
    # вводим значение 45
    delay.send_keys('45')

    # нажимаем на кнопки и ожидаем загрузку 5 секунд
    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.implicitly_wait(5)

    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.implicitly_wait(5)

    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.implicitly_wait(5)

    driver.find_element(By.XPATH, '//span[text()="="]').click()
    driver.implicitly_wait(5)

    # ожидаем появления результата
    WebDriverWait(driver, 45).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    # проверяем результат
    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert int(result) == 15

    # закрываем браузер
    driver.quit()


