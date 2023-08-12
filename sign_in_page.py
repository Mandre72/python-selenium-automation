from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pages.base_page import Page

service = Service(executable_path='/Users/matthewandre/Downloads/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

class SignInPage(Page):
    def verify_signin_opened(self):
        self.verify_url_contains_query('https://www.amazon.com/ap/signin')
