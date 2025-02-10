from selenium.webdriver.common.by import By


class FormPage:

    def __init__(self, _driver):
        self.driver = _driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    def complete_the_form(self):
        first_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
        first_name.send_keys("Иван")

        last_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
        last_name.send_keys("Петров")

        address = self.driver.find_element(By.CSS_SELECTOR, "input[name='address']")
        address.send_keys("Ленина, 55-3")

        zip_code = self.driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
        zip_code.send_keys("")

        city = self.driver.find_element(By.CSS_SELECTOR, "input[name='city']")
        city.send_keys("Москва")

        country = self.driver.find_element(By.CSS_SELECTOR, "input[name='country']")
        country.send_keys("Россия")

        email = self.driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
        email.send_keys("test@skypro.com")

        phone_number = self.driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
        phone_number.send_keys("+7985899998787")

        job_position = self.driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
        job_position.send_keys("QA")

        company = self.driver.find_element(By.CSS_SELECTOR, "input[name='company']")
        company.send_keys("SkyPro")

    def sublime_click(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def zip_code_red(self):
        zip_code = self.driver.find_element(By.CSS_SELECTOR, "#zip-code")
        return zip_code.value_of_css_property("background-color")

    def other_green(self, field_name):
        field = self.driver.find_element(By.CSS_SELECTOR, f"#{field_name}")
        return field.value_of_css_property("background-color")
