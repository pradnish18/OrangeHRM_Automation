import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import logger

class DashboardPage(BasePage):
    DASHBOARD_HEADER = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb")
    PIM_MENU_ITEM = (By.XPATH, "//span[text()='PIM']/ancestor::a")
    USER_DROPDOWN = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    LOGOUT_OPTION = (By.XPATH, "//a[contains(@href, '/auth/logout')] | //a[text()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_dashboard_displayed(self):
        return self.is_displayed(self.DASHBOARD_HEADER, timeout=10)

    def navigate_to_pim_module(self):
        """Hovers over the PIM menu item in sidebar and clicks it as per workflow requirement."""
        logger.info("Hovering mouse over PIM menu sidebar item...")
        self.wait_for_spinner()
        self.hover_element(self.PIM_MENU_ITEM)
        logger.info("Clicking on PIM module...")
        self.click(self.PIM_MENU_ITEM)
        self.wait_for_spinner()

    def logout(self):
        logger.info("Initiating Logout flow from Dashboard...")
        self.wait_for_spinner()
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_OPTION)
        logger.info("Logout clicked successfully.")
