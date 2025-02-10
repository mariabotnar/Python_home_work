from selenium import webdriver
from pages.CalcPage import CalcPage


def test_calculator():
    driver = webdriver.Chrome()

    calc_page = CalcPage(driver)
    calc_page.delay()
    calc_page.calculator()
    result = calc_page.result()

    driver.quit()

    assert result == 15
