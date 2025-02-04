from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from pages.FormPage import FormPage


def test_complete_the_form():
    driver = webdriver.Chrome()

    form_page = FormPage(driver)
    form_page.complete_the_form()
    form_page.sublime_click()
    form_page.zip_code_red()
    driver.quit()



