from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# ЗАДАНИЕ 2
# открытие страницы
driver.get("http://the-internet.herokuapp.com/inputs")

sleep(5)

# ввод - очистка - ввод
input_1 = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input_1.send_keys('1000')
input_1.clear()
input_1.send_keys('999')

sleep(5)

driver.quit()