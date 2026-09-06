import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.pim_page import PIMPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_orange_hrm_workflow(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    login_pg = LoginPage(driver)
    pim_pg = PIMPage(driver)

    # 1. Login
    login_pg.login("Admin", "admin123")

    # 2. Navigate to PIM
    pim_pg.navigate_to_pim()

    # 3. Add 3 Employees
    employees = [("John", "Doe"), ("Jane", "Smith"), ("Alice", "Wonder")]
    for f, l in employees:
        pim_pg.add_employee(f, l)
    
    # 4. Verify Employees
    for f, l in employees:
        assert pim_pg.verify_employee(f"{f} {l}")

    # 5. Logout
    driver.find_element("css selector", ".oxd-userdropdown-name").click()
    driver.find_element("link text", "Logout").click()