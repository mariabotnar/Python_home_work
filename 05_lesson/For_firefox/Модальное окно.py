from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# ЗАДАНИЕ 1
# открытие страницы
driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(5)

# нажатие на кнопку Close
close_button = driver.find_element(By.CSS_SELECTOR, 'div.modal-footer > p')
close_button.click()

search_field = "div.modal"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys(Keys.RETURN)

driver.quit()