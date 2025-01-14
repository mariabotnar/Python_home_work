from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# ЗАДАНИЕ 3
# открытие страницы
driver.get("http://the-internet.herokuapp.com/login")

sleep(5)

# поле username и password
user_name_field = driver.find_elements(By.CSS_SELECTOR, 'username')
password_field = driver.find_element(By.CSS_SELECTOR, 'password')

sleep(5)

# данные пользователя
user_name_field.send_keys('mariyabotnar')
password_field.send_keys('abcd')

# нажатие кнопки login
login_button = driver.find_elements(By.CSS_SELECTOR, 'button')
login_button.click()