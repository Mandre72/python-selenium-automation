from selenium.webdriver.common.by import By
from behave import given, when, then


@when('User Click on the cart icon')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()


@then('Verify your amazon cart is empty')
def verify_click_result(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h2['Your Amazon Cart is empty']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
