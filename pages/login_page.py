from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config
from utils.logger import logger

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-alert-content-text")
    FIELD_ERROR_MSG = (By.CSS_SELECTOR, ".oxd-input-field-error-message")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_login(self):
        self.open_url(Config.BASE_URL)
        self.wait_for_spinner()

    def enter_username(self, username):
        logger.info(f"Entering username: '{username}'")
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        logger.info("Entering password...")
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        logger.info("Clicking Login button...")
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        if self.is_displayed(self.ERROR_MESSAGE, timeout=5):
            return self.get_text(self.ERROR_MESSAGE)
        return ""

    def get_field_validation_errors(self):
        if self.is_displayed(self.FIELD_ERROR_MSG, timeout=3):
            elements = self.find_elements(self.FIELD_ERROR_MSG)
            return [e.text for e in elements]
        return []
