from selenium import webdriver


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
    overview_page = OverviewPage(driver)
    result = overview_page.overview()
    assert result == 'Total: $58.29'
    driver.quit()












