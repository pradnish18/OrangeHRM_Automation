import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import Config

class TestLogin:
    
    def test_tc_login_01_valid_credentials(self, driver):
        """TC_LOGIN_01: Verify login with valid credentials."""
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        
        login_page.navigate_to_login()
        login_page.login(Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)
        
        assert dashboard_page.is_dashboard_displayed(), "Dashboard header should be displayed after valid login!"

    def test_tc_login_02_lowercase_username(self, driver):
        """TC_LOGIN_02: Verify login with lowercase valid username."""
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        login_page.navigate_to_login()
        login_page.login("admin", Config.ADMIN_PASSWORD)

        assert dashboard_page.is_dashboard_displayed(), "Dashboard header should be displayed for lowercase 'admin'!"

    def test_tc_login_03_invalid_username(self, driver):
        """TC_LOGIN_03: Verify login with invalid username."""
        login_page = LoginPage(driver)
        
        login_page.navigate_to_login()
        login_page.login("InvalidAdminUser", Config.ADMIN_PASSWORD)
        
        error_msg = login_page.get_error_message()
        assert "Invalid credentials" in error_msg, f"Expected 'Invalid credentials' error message, got '{error_msg}'"

    def test_tc_login_04_invalid_password(self, driver):
        """TC_LOGIN_04: Verify login with invalid password."""
        login_page = LoginPage(driver)
        
        login_page.navigate_to_login()
        login_page.login(Config.ADMIN_USERNAME, "WrongPass123!")
        
        error_msg = login_page.get_error_message()
        assert "Invalid credentials" in error_msg, f"Expected 'Invalid credentials' error message, got '{error_msg}'"

    def test_tc_login_05_blank_username(self, driver):
        """TC_LOGIN_05: Verify field validation when username is left blank."""
        login_page = LoginPage(driver)

        login_page.navigate_to_login()
        login_page.enter_password("admin123")
        login_page.click_login()

        errors = login_page.get_field_validation_errors()
        assert len(errors) >= 1, "Validation error message 'Required' should appear when username is blank."

    def test_tc_login_06_blank_password(self, driver):
        """TC_LOGIN_06: Verify field validation when password is left blank."""
        login_page = LoginPage(driver)

        login_page.navigate_to_login()
        login_page.enter_username("Admin")
        login_page.click_login()

        errors = login_page.get_field_validation_errors()
        assert len(errors) >= 1, "Validation error message 'Required' should appear when password is blank."

    def test_tc_login_07_empty_credentials(self, driver):
        """TC_LOGIN_07: Verify field validation for empty username and password."""
        login_page = LoginPage(driver)
        
        login_page.navigate_to_login()
        login_page.click_login()
        
        errors = login_page.get_field_validation_errors()
        assert len(errors) >= 2, "Validation error messages should appear for both empty fields."

    def test_tc_login_08_special_characters(self, driver):
        """TC_LOGIN_08: Verify login with SQL injection / special characters in input fields."""
        login_page = LoginPage(driver)

        login_page.navigate_to_login()
        login_page.login("' OR '1'='1", "admin123'--")

        error_msg = login_page.get_error_message()
        assert "Invalid credentials" in error_msg, "System should safely reject special character injections."
