from selenium.webdriver.common.by import By
from behave import when, then


@when('Click department dropdown')
def click_department_dropdown(context):
    context.driver.find_element(By.ID, 'searchDropdownBox').click()


@when('Click on Computers department')
def click_computers_department(context):
    context.driver.find_element(By.XPATH, "//option[text()='Computers']").click()


@when('Input {search_word} into search field')
def input_laptops(context, search_word):
    search_field = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search_field.send_keys(search_word)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Product results for {search_word} are shown')
def verify_product_results(context, search_word):
    search_results = context.driver.find_element(By.XPATH, "//span[contains( @class, 'a-color-state')]")
    assert search_word.lower() in search_results.text.lower(), f"Search term '{search_word}'not found in search results."




