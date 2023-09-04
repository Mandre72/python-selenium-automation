from behave import when, given, then
from selenium.webdriver.common.by import By


DOG_IMG = (By.CSS_SELECTOR, 'img#d')


@given('Open Amazon T&C page')
def open_product(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html?nodeId=GLSBYFE9MGKKQXXM&pop-up=1')


@when('Store original windows')
def store_current_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.driver.find_element(By.XPATH, "//a[@href='https://www.amazon.com/privacy']").click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.windows = context.driver.window_handles
    print('\nAll WINDOWS: ', context.windows)
    context.driver.switch_to.window(context.windows[1])

    context.current_window = context.driver.current_window_handle
    print('\nAFTER WE SWITCHED:')
    print(context.current_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_opened(context):
    context.driver.get('https://www.amazon.com/privacy')


@then('User can close new window and switch back to original')
def switch_to_original_window(context):
    context.driver.switch_to.window(context.original_window)


