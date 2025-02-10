from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, _driver):
        self.driver = _driver

    def cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        basket = self.driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
        basket.click()
        checkout = self.driver.find_element(By.XPATH, "//*[@id='checkout']")
        checkout.click()