from selenium.webdriver.common.by import By
from behave import when, given, then


COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "variation_color_name .selection")


@given('Open Amazon product B07F2546TD page')
def open_product(context):
    context.driver.get('https://www.amazon.com/Amazon-Essentials-Regular-Fit-Long-Sleeve-Pocket/dp/B07F2546TD/')


@then('Verify user can click through colors')
def verify_user_can_select_colors(context):
    context.driver.find_element(*COLOR_OPTIONS).click()

    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('ALL color:, all_color_options')

    for color in all_color_options:
        color.click()

