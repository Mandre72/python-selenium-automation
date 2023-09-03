from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# service = Service(executable_path='/Users/matthewandre/Downloads/Automation/python-selenium-automation/chromedriver')
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
#
# driver.get('https://www.amazon.com/')


#@when('User Click on the cart icon')
#def click_search(context):
    #context.driver.find_element(By.ID, 'nav-cart-count').click()


#@then('Verify your amazon cart is empty')
#def verify_click_result(context):
    #expected_result = 'Your Amazon Cart is empty'
    #actual_result = context.driver.find_element(By.XPATH, "//h2['Your Amazon Cart is empty']").text
    #assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


class AmazonHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.amazon_url = "https://www.amazon.com/"

    def open(self):
        self.driver.get(self.amazon_url)

    def click_cart_icon(self):
        cart_icon = self.driver.find_element(By.ID, 'nav-cart-count')
        cart_icon.click()


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    def is_empty_cart_message_present(self):
        try:
            message_element = self.driver.find_element(By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]")
            return message_element.text
        except NoSuchElementException:
            return None


@when('User Click on the cart icon')
def click_cart_icon(context):
    amazon_home_page = AmazonHomePage(context.driver)
    amazon_home_page.click_cart_icon()


@then('Verify Your Amazon Cart is empty text present')
def verify_click_result(context):
    shopping_cart_page = ShoppingCartPage(context.driver)
    actual_result = shopping_cart_page.is_empty_cart_message_present()
    assert actual_result is not None, "Expected 'Your Amazon Cart is empty' message, but it's not present."
