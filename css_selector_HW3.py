from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/matthewandre/Automation/python-selenium-automation/chromedriver')


driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']")
driver.find_element(By.CSS_SELECTOR, "h1[class='a-spacing-small']")
driver.find_element(By.CSS_SELECTOR, "input[id='ap_customer_name']")
driver.find_element(By.CSS_SELECTOR, "input[type='email']")
driver.find_element(By.CSS_SELECTOR, "input[type='password']")
driver.find_element(By.CSS_SELECTOR, "div[class='a-alert-content']")
driver.find_element(By.CSS_SELECTOR, "input[id='ap_password_check']")
driver.find_element(By.CSS_SELECTOR, "input[id='continue']")
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin']")
