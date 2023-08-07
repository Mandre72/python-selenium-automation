from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('User Click on Returns and Orders icon')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify Sign in page opened')
def verify_click_result(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
