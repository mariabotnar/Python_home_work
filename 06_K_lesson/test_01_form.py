import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
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
def test_01_form(driver):
    # открываем страницу
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    wait = WebDriverWait(driver, 10)

    # заполняем форму значениями
    first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
    first_name.clear()
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
    last_name.clear()
    last_name.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
    address.clear()
    address.send_keys("Ленина, 55-3")

    zip_code = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
    zip_code.clear()
    zip_code.send_keys("")

    city = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
    city.clear()
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
    country.clear()
    country.send_keys("Россия")

    email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
    email.clear()
    email.send_keys("test@skypro.com")

    phone_number = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
    phone_number.clear()
    phone_number.send_keys("+7985899998787")

    job_position = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
    job_position.clear()
    job_position.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
    company.clear()
    company.send_keys("SkyPro")

    # нажимаем на кнопку Sublime
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # проверяем цвет пустого поля Zip code (ожидаем красный)
    alert_danger_color = "rgba(248, 215, 218, 1)"
    zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    color_zip = zip_code.value_of_css_property("background-color")
    assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"

    # проверяем цвет заполненных полей (ожидаем зелёный)
    fields_to_check = ["first-name", "last-name", "address", "e-mail", "phone",
                       "city", "country", "job-position", "company"]
    for field_name in fields_to_check:
        field = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, f"div.alert.py-2.alert-success[id='{field_name}']")))
        background_color = field.value_of_css_property("background-color")
        assert background_color == "rgba(209, 231, 221, 1)"

    # тест завершён