from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from pages.LoginPage import LoginPage
from pages.CartPage import CartPage
from pages.InformPage import InformPage
from pages.OverviewPage import OverviewPage


def test_shop():
    driver = webdriver.Chrome()

    login_page = LoginPage(driver)
    login_page.login()
    cart_page = CartPage(driver)
    cart_page.cart()
    inform_page = InformPage(driver)
    inform_page.inform()
    overveiw_page = OverviewPage(driver)
    overveiw_page.overview()
    overveiw_page.assert_sum()
    driver.quit()












