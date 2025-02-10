from selenium.webdriver.common.by import By


class OverviewPage:

    def __init__(self, _driver):
        self.driver = _driver

    def overview(self):
        total = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        return total