import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from config.config import Config
from utils.logger import logger

class TestEmployeeScenarios:

    @pytest.fixture(autouse=True)
    def setup_and_login(self, driver):
        self.login_page = LoginPage(driver)
        self.dashboard_page = DashboardPage(driver)
        self.pim_page = PIMPage(driver)

        self.login_page.navigate_to_login()
        self.login_page.login(Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)
        assert self.dashboard_page.is_dashboard_displayed()
        self.dashboard_page.navigate_to_pim_module()

    def test_tc_emp_01_to_07_full_lifecycle(self, driver):
        """
        Executes explicit test lifecycle for TC_EMP_01 through TC_EMP_07:
        - TC_EMP_01: Add employee with valid details
        - TC_EMP_02: Verify newly added employee in Employee List
        - TC_EMP_03: View employee details
        - TC_EMP_04: Update employee information
        - TC_EMP_05: Verify updated employee information
        - TC_EMP_07: Cancel employee deletion
        - TC_EMP_06: Delete employee
        """
        test_first_name = "Samantha"
        test_middle_name = "QA"
        initial_last_name = "Roberts"
        updated_last_name = "UpdatedRoberts"
        test_emp_id = "998877"

        # TC_EMP_01: Add employee with valid details
        logger.info("--- Testing TC_EMP_01: Add employee with valid details ---")
        self.pim_page.add_employee(test_first_name, test_middle_name, initial_last_name, test_emp_id)
        assert self.pim_page.is_displayed(PIMPage.PERSONAL_DETAILS_HEADER, timeout=10), "TC_EMP_01 Failed: Personal Details page not loaded!"
        logger.info("TC_EMP_01 PASSED: Employee created successfully.")

        # TC_EMP_02: Verify newly added employee in Employee List
        logger.info("--- Testing TC_EMP_02: Verify newly added employee in Employee List ---")
        is_in_list = self.pim_page.locate_and_verify_employee({"first_name": test_first_name, "last_name": initial_last_name, "emp_id": test_emp_id})
        assert is_in_list, "TC_EMP_02 Failed: Newly added employee not found in Employee List!"
        logger.info("TC_EMP_02 PASSED: Employee appeared in the list.")

        # TC_EMP_03: View employee details
        logger.info("--- Testing TC_EMP_03: View employee details ---")
        self.pim_page.click_edit_employee(test_first_name)
        assert self.pim_page.is_displayed(PIMPage.PERSONAL_DETAILS_HEADER, timeout=10), "TC_EMP_03 Failed: Employee details not displayed!"
        logger.info("TC_EMP_03 PASSED: Correct employee details displayed.")

        # TC_EMP_04 & TC_EMP_05: Update employee information & Verify updated info
        logger.info("--- Testing TC_EMP_04 & 05: Update & Verify employee information ---")
        self.pim_page.update_last_name(updated_last_name)
        is_updated_in_list = self.pim_page.locate_and_verify_employee({"first_name": test_first_name, "last_name": updated_last_name, "emp_id": test_emp_id})
        assert is_updated_in_list, "TC_EMP_04 / 05 Failed: Updated employee last name not reflected!"
        logger.info("TC_EMP_04 & TC_EMP_05 PASSED: Updated information saved and verified.")

        # TC_EMP_07: Cancel employee deletion
        logger.info("--- Testing TC_EMP_07: Cancel employee deletion ---")
        self.pim_page.click_delete_employee(test_first_name)
        self.pim_page.cancel_deletion()
        is_still_there = self.pim_page.locate_and_verify_employee({"first_name": test_first_name, "last_name": updated_last_name, "emp_id": test_emp_id})
        assert is_still_there, "TC_EMP_07 Failed: Employee was removed after canceling deletion!"
        logger.info("TC_EMP_07 PASSED: Employee remains in the list after canceling deletion.")

        # TC_EMP_06: Delete employee
        logger.info("--- Testing TC_EMP_06: Delete employee ---")
        self.pim_page.click_delete_employee(test_first_name)
        self.pim_page.confirm_deletion()
        self.pim_page.search_employee(emp_id=test_emp_id)
        # Verify employee no longer in table
        cards = driver.find_elements(*PIMPage.TABLE_CARDS)
        assert len(cards) == 0 or test_first_name not in cards[0].text, "TC_EMP_06 Failed: Employee still exists after deletion!"
        logger.info("TC_EMP_06 PASSED: Employee deleted after confirmation.")
