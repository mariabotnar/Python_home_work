from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from pages.CalcPage import CalcPage


def test_calculator():
    driver = webdriver.Chrome()

    calc_page = CalcPage(driver)
    calc_page.delay()
    calc_page.calculator()
    calc_page.result()
    driver.quit()

