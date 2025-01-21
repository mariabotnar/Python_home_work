from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# ЗАДАНИЕ 3
# открытие страницы
driver.get('http://uitestingplayground.com/classattr')
sleep(5)

# клик на синюю кнопку
button_with_dynamic_id = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
button_with_dynamic_id.click()

sleep(10)

alert = Alert(driver)
alert.accept()

sleep(10)

driver.quit()

# скрипт отрабатывает одинаково