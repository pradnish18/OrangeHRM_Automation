from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class PIMPage(BasePage):
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    ADD_BUTTON = (By.XPATH, "//button[text()=' Add ']")
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    EMP_LIST_TAB = (By.XPATH, "//a[text()='Employee List']")
    
    def navigate_to_pim(self):
        self.hover(self.PIM_MENU)
        self.click(self.PIM_MENU)

    def add_employee(self, fname, lname):
        self.click(self.ADD_BUTTON)
        self.type(self.FIRST_NAME, fname)
        self.type(self.LAST_NAME, lname)
        self.click(self.SAVE_BUTTON)
        time.sleep(2) # Wait for save

    def verify_employee(self, full_name):
        self.click(self.EMP_LIST_TAB)
        # Simplified check: scroll and look for text
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if full_name in self.driver.page_source:
            print(f"{full_name}: Name Verified")
            return True
        return False