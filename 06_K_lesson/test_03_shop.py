from time import sleep
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
def test_03_shop(driver):
    # открываем страницу
    driver.get('https://www.saucedemo.com/')

    wait = WebDriverWait(driver, 10)

    # заполняем форму значениями
    username = driver.find_element(By.CSS_SELECTOR, "input[name='user-name']")
    username.clear()
    username.send_keys("standard_user")

    password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    password.clear()
    password.send_keys("secret_sauce")

    # кликаем на кнопку Login
    login = driver.find_element(By.CSS_SELECTOR, "input#login-button")
    login.click()

    # добавляем товары в корзину
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    # переходим в корзину
    basket = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
    basket.click()

    # нажимаем Checkout
    checkout = driver.find_element(By.XPATH, "//*[@id='checkout']")
    checkout.click()

    # заполняем форму данными
    first_name = driver.find_element(By.CSS_SELECTOR, "input[name='firstName']")
    first_name.send_keys("Мария")

    last_name = driver.find_element(By.CSS_SELECTOR, "input[name='lastName']")
    last_name.send_keys("Ботнарь")

    zp_code = driver.find_element(By.CSS_SELECTOR, "input[name='postalCode']")
    zp_code.send_keys("292940")

    # нажимаем Continue
    cont = driver.find_element(By.CSS_SELECTOR, "input[class='submit-button btn btn_primary cart_button btn_action']")
    cont.click()

    # читаем итоговую стоимость
    total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    print(total)
    sleep(5)
    return total

# проверяем итоговую сумму ЗДЕСЬ ТЕСТ ПАДАЕТ ПОМОГИТЕ )
def test_purchase_total(driver):
    total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    print(total)
    assert total == 'Total: $58.29'


