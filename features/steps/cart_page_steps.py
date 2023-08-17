from selenium.webdriver.common.by import By
from behave import given, when, then


CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.CSS_SELECTOR, "sc-active-cart li")


@when('Click go to cart button')
def open_cart_page (context):
    # context.driver.get('https://www.amazon.com/go/cart/view.html?ref_=nav_cart')
    context.driver.find_element(By.CSS_SELECTOR, '#sw-gtc span.a-button-inner').click()


@then('Verify cart has product')
def verify_cart_product(context):
    expected_result = '1'
    actual_result = context.driver.find_element(By.ID, 'sc-subtotal-label-buybox').text
    assert expected_result in actual_result, f'Expected {expected_result} but got actual {actual_result}'

