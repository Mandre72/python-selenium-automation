from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# Define Page Objects
class AmazonHomePage:
    def __init__(self, context):
        self.context = context

    def open(self):
        self.context.driver.get('https://www.amazon.com/')

    def click_orders_icon(self):
        orders_icon = self.context.driver.find_element(By.ID, 'nav-orders')
        orders_icon.click()


class SignInPage:
    def __init__(self, context):
        self.context = context

    def verify_sign_in_page_opened(self):
        expected_result = 'Sign in'
        actual_result = self.context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
        assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@given('Open Amazon page')
def open_amazon(context,):
    context.driver.get('https://www.amazon.com/')
    sleep(2)
    context.driver.refresh()
    #amazon_home_page = AmazonHomePage(context)
    #amazon_home_page.open()


@when('User Click on Returns and Orders icon')
def click_search(context):
    #context.driver.find_element(By.ID, 'nav-orders').click()
    amazon_home_page = AmazonHomePage(context)
    amazon_home_page.click_orders_icon()


@then('Verify Sign in page opened')
def verify_click_result(context):
    #expected_result = 'Sign in'
    #actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    #assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
    sign_in_page = SignInPage(context)
    sign_in_page.verify_sign_in_page_opened()