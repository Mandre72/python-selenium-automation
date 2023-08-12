from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# init driver
service = Service(executable_path='/Users/matthewandre/Downloads/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()


@when('Click on Best Sellers')
def click_search(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()


@then('Verify that header has {expected_amount} links')
def verify_header_link_count(context, expected_amount,):
    print('Original Type: ', type(expected_amount))
    expected_amount = int(expected_amount)
    print('Type after converting: ', type(expected_amount))

    header_links = context.driver.find_elements(By.CSS_SELECTOR, '#zg_header a')
    print(header_links)
    print('\nLink count: ', len(header_links))
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links, but got {len(header_links)}'
