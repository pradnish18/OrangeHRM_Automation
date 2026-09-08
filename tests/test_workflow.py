import time
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from pages.dashboard_page import DashboardPage

def test_orange_hrm_workflow(driver):
    login_pg = LoginPage(driver)
    pim_pg = PIMPage(driver)
    dashboard_pg = DashboardPage(driver)

    # 1. Automate Login
    login_pg.navigate_to_login()
    login_pg.login("Admin", "admin123")
    assert dashboard_pg.is_dashboard_displayed(), "Dashboard header should be visible after login!"

    # 2. Navigate to PIM (Hover + Click)
    pim_pg.navigate_to_pim()

    # 3. Add 3 Employees
    suffix = str(int(time.time()))[-5:]
    employees = [
        (f"Alice{suffix}", "One"),
        (f"Bob{suffix}", "Two"),
        (f"Charlie{suffix}", "Three"),
    ]
    for f, l in employees:
        pim_pg.add_employee(f, "", l)
    
    # 4. Verify Employees in Employee List
    for f, l in employees:
        assert pim_pg.verify_employee(f"{f} {l}"), f"Employee {f} {l} verification failed!"

    # 5. Log Out from Dashboard
    dashboard_pg.logout()