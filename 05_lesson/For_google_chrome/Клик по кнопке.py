from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# ЗАДАНИЕ 1
# открытие страницы
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
sleep(5)

# клик по кнопке пять раз
for _ in range(5):
    add_element_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
    add_element_button.click()

sleep(5)

# список кнопок delete
delete_buttons = driver.find_elements(By.XPATH, '//*[@id="elements"]')

# размер списка
print('Размер списка кнопок Delete:', len(delete_buttons))

driver.quit()
