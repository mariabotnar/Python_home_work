from selenium import webdriver
from pages.FormPage import FormPage


def test_complete_the_form():
    driver = webdriver.Chrome()

    form_page = FormPage(driver)
    form_page.complete_the_form()
    form_page.sublime_click()


    alert_danger_color = "rgba(248, 215, 218, 1)"
    color_zip = form_page.zip_code_red()
    assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"

    fields_to_check = ["first-name", "last-name", "address", "e-mail", "phone",
                       "city", "country", "job-position", "company"]
    for field_name in fields_to_check:
        background_color = form_page.other_green(field_name)
        assert background_color == "rgba(209, 231, 221, 1)"

    driver.quit()

