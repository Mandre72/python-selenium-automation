from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path='/Users/matthewandre/Downloads/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.CSS_SELECTOR, "sc-active-cart li")


@when('Open cart page')
def open_cart_page (context):
    context.driver.get('https://www.amazon.com/go/cart/view.html?ref_=nav_cart')


@then('Verify cart has product')
def verify_cart_product(context):
    expected_result = 'Added to Cart'
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-fixed-left-grid']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

