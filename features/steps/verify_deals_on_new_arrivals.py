from selenium.webdriver.common.by import By
from behave import when, given, then
from selenium.webdriver.common.action_chains import ActionChains


@given('Open Amazon product B074TBCSC8 page')
def open_product(context):
    context.driver.get('https://www.amazon.com/gp/product/B074TBCSC8')


@when('User hovers over {element}')
def hover_over_element(context, element):
    element_locator = None

    if element == "New Arrivals":
        element_locator = (By.XPATH, "//a[contains(text(),'New Arrivals')]")
    # Add more conditions for other elements if needed

    if element_locator:
        element = context.driver.find_element(*element_locator)
        action = ActionChains(context.driver)
        action.move_to_element(element).perform()


@then('Verify user sees the deals')
def verify_deals_visibility(context):
    deals_element = context.driver.find_element(By.XPATH, "//a[contains( @href, 'New-Arrivals' )]")

    assert deals_element.is_displayed(), "Deals are not visible."

    context.driver.quit()
