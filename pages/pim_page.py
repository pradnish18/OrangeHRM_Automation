import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from utils.logger import logger

class PIMPage(BasePage):
    # Top Navigation Tabs
    PIM_MENU = (By.XPATH, "//span[text()='PIM']/ancestor::a")
    ADD_EMPLOYEE_TAB = (By.XPATH, "//a[normalize-space()='Add Employee']")
    EMPLOYEE_LIST_TAB = (By.XPATH, "//a[normalize-space()='Employee List']")
    ADD_EMPLOYEE_BTN = (By.XPATH, "//button[contains(., 'Add')]")

    # Add / Edit Employee Form Locators
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    MIDDLE_NAME_INPUT = (By.NAME, "middleName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    EMP_ID_INPUT = (By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div/input")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    PERSONAL_DETAILS_HEADER = (By.XPATH, "//h6[normalize-space()='Personal Details']")

    # Employee List Locators
    SEARCH_EMP_NAME = (By.XPATH, "//label[text()='Employee Name']/parent::div/following-sibling::div//input")
    SEARCH_EMP_ID = (By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div/input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    RESET_BUTTON = (By.XPATH, "//button[contains(., 'Reset')]")
    TABLE_CARDS = (By.CSS_SELECTOR, ".oxd-table-card")
    TABLE_BODY = (By.CSS_SELECTOR, ".oxd-table-body")

    # Confirmation Modal Locators
    CONFIRM_DELETE_BTN = (By.XPATH, "//button[contains(., 'Yes, Delete')]")
    CANCEL_DELETE_BTN = (By.XPATH, "//button[contains(., 'No, Cancel')]")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_pim(self):
        """Legacy helper matching assignment workflow."""
        DashboardPage(self.driver).navigate_to_pim_module()

    def click_add_employee_tab(self):
        logger.info("Clicking 'Add Employee' tab...")
        self.safe_click(self.ADD_EMPLOYEE_TAB)
        self.wait_for_spinner()

    def click_employee_list_tab(self):
        logger.info("Clicking 'Employee List' tab...")
        self.safe_click(self.EMPLOYEE_LIST_TAB)
        self.wait_for_spinner()

    def reset_search(self):
        if self.is_displayed(self.RESET_BUTTON, timeout=3):
            try:
                self.click(self.RESET_BUTTON)
                self.wait_for_spinner()
            except Exception:
                pass

    def add_employee(self, first_name, middle_name="", last_name="", emp_id=None):
        """Fills and submits the Add Employee form."""
        logger.info(f"Adding Employee: {first_name} {middle_name} {last_name} (ID: {emp_id})")
        self.click_add_employee_tab()
        
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        if middle_name:
            self.type_text(self.MIDDLE_NAME_INPUT, middle_name)
        if last_name:
            self.type_text(self.LAST_NAME_INPUT, last_name)
        if emp_id:
            self.type_text(self.EMP_ID_INPUT, emp_id)
            
        logger.info("Clicking Save button...")
        self.safe_click(self.SAVE_BUTTON)
        
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: "viewPersonalDetails" in d.current_url or self.is_displayed(self.PERSONAL_DETAILS_HEADER, timeout=2)
            )
        except Exception:
            pass
        self.wait_for_spinner()
        logger.info(f"Employee {first_name} {last_name} added successfully.")

    def search_employee(self, emp_id=None, first_name=None):
        self.click_employee_list_tab()
        self.reset_search()
        
        if emp_id:
            logger.info(f"Searching Employee List for ID: {emp_id}")
            self.type_text(self.SEARCH_EMP_ID, emp_id)
        elif first_name:
            logger.info(f"Searching Employee List for Name: {first_name}")
            emp_input = self.find_visible_element(self.SEARCH_EMP_NAME)
            self.type_text(self.SEARCH_EMP_NAME, first_name)
            time.sleep(0.5)
            emp_input.send_keys(Keys.ESCAPE) # dismiss autocomplete overlay

        self.click(self.SEARCH_BUTTON)
        self.wait_for_spinner()
        time.sleep(1)

    def _check_table_for_name(self, first_name, last_name=""):
        try:
            self.wait_for_spinner()
            if self.is_displayed(self.TABLE_BODY, timeout=5):
                cards = self.driver.find_elements(*self.TABLE_CARDS)
                for card in cards:
                    card_text = card.text
                    if first_name in card_text and (not last_name or last_name in card_text):
                        self.scroll_into_view(card)
                        logger.info(f"Employee match found in table row: {card_text.replace(chr(10), ' | ')}")
                        print("Name Verified")
                        logger.info("Name Verified")
                        return True
        except Exception as e:
            logger.warning(f"Exception during table check: {e}")
        return False

    def locate_and_verify_employee(self, employee_data):
        if isinstance(employee_data, str):
            parts = employee_data.split(maxsplit=1)
            first_name = parts[0]
            last_name = parts[1] if len(parts) > 1 else ""
            emp_id = None
        else:
            first_name = employee_data["first_name"]
            last_name = employee_data.get("last_name", "")
            emp_id = employee_data.get("emp_id")

        logger.info(f"Verifying presence of Employee: {first_name} {last_name} (ID: {emp_id})")
        
        if emp_id:
            self.search_employee(emp_id=emp_id)
            if self._check_table_for_name(first_name, last_name):
                return True

        if first_name:
            self.search_employee(first_name=first_name)
            if self._check_table_for_name(first_name, last_name):
                return True

        self.click_employee_list_tab()
        self.reset_search()
        self.click(self.SEARCH_BUTTON)
        if self._check_table_for_name(first_name, last_name):
            return True

        logger.error(f"Failed to locate employee {first_name} {last_name} in list!")
        return False

    def verify_employee(self, full_name):
        """Legacy compatibility wrapper matching workflow requirements."""
        return self.locate_and_verify_employee(full_name)

    def click_edit_employee(self, first_name):
        logger.info(f"Clicking Edit (pencil icon) for employee '{first_name}'...")
        edit_xpath = f"//div[contains(@class, 'oxd-table-card')][contains(., '{first_name}')]//button[i[contains(@class, 'bi-pencil-fill')]]"
        self.safe_click((By.XPATH, edit_xpath))
        self.wait_for_spinner()

    def click_delete_employee(self, first_name):
        logger.info(f"Clicking Delete (trash icon) for employee '{first_name}'...")
        delete_xpath = f"//div[contains(@class, 'oxd-table-card')][contains(., '{first_name}')]//button[i[contains(@class, 'bi-trash')]]"
        self.safe_click((By.XPATH, delete_xpath))
        self.wait_for_spinner()

    def confirm_deletion(self):
        logger.info("Confirming deletion in popup modal...")
        self.safe_click(self.CONFIRM_DELETE_BTN)
        self.wait_for_spinner()

    def cancel_deletion(self):
        logger.info("Canceling deletion in popup modal...")
        self.safe_click(self.CANCEL_DELETE_BTN)
        self.wait_for_spinner()

    def update_last_name(self, new_last_name):
        logger.info(f"Updating employee last name to '{new_last_name}'...")
        self.type_text(self.LAST_NAME_INPUT, new_last_name)
        save_btn_xpath = "//h6[text()='Personal Details']/ancestor::form//button[@type='submit']"
        if self.is_displayed((By.XPATH, save_btn_xpath), timeout=3):
            self.safe_click((By.XPATH, save_btn_xpath))
        else:
            self.safe_click(self.SAVE_BUTTON)
        self.wait_for_spinner()
