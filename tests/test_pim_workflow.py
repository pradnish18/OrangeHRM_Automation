import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from config.config import Config
from utils.data_generator import generate_employee_list
from utils.logger import logger

class TestPIMWorkflow:

    def test_e2e_pim_employee_addition_and_verification(self, driver):
        """
        Automates the full E2E workflow requested by Omnify assignment:
        1. Login to OrangeHRM.
        2. Mouse hover over PIM sidebar menu and click it.
        3. Add 4 new employees via Add Employee form.
        4. Navigate to Employee List page.
        5. Scroll through list to locate each employee, verify name, and print "Name Verified".
        6. Log out from the Dashboard.
        """
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        pim_page = PIMPage(driver)

        # 1. Login Flow
        logger.info("=== STEP 1: Automating Login Flow ===")
        login_page.navigate_to_login()
        login_page.login(Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)
        assert dashboard_page.is_dashboard_displayed(), "Failed to log in to OrangeHRM dashboard!"

        # 2. Navigate to PIM module (Mouse Hover + Click)
        logger.info("=== STEP 2: Navigating to PIM Module via Mouse Hover & Click ===")
        dashboard_page.navigate_to_pim_module()

        # 3. Add 4 Employees
        logger.info("=== STEP 3: Adding 4 New Employees ===")
        test_employees = generate_employee_list(count=4)
        
        for emp in test_employees:
            pim_page.add_employee(
                first_name=emp["first_name"],
                middle_name=emp["middle_name"],
                last_name=emp["last_name"],
                emp_id=emp["emp_id"]
            )

        # 4 & 5. Verify Employees in Employee List & Print "Name Verified"
        logger.info("=== STEP 4 & 5: Verifying Employees in Employee List ===")
        verification_results = []
        for emp in test_employees:
            is_verified = pim_page.locate_and_verify_employee(emp)
            verification_results.append(is_verified)
            assert is_verified, f"Employee {emp['first_name']} {emp['last_name']} could not be verified!"

        # 6. Log Out from Dashboard
        logger.info("=== STEP 6: Logging Out from Dashboard ===")
        pim_page.click_employee_list_tab() # ensure header/userdropdown accessible
        dashboard_page.logout()
        
        logger.info("=== E2E PIM Workflow Completed Successfully! All names verified. ===")
