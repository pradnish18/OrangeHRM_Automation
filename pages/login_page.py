from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, username, password):
        self.type(self.USERNAME_FIELD, username)
        self.type(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)