import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.config import Config
from utils.logger import logger

def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default="false", help="Run browser in headless mode: true or false")

@pytest.fixture(scope="function")
def driver(request):
    headless_opt = request.config.getoption("--headless").lower() == "true" or Config.HEADLESS
    
    logger.info("Initializing Chrome WebDriver...")
    chrome_options = Options()
    if headless_opt:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("window-size=1920,1080")

    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    driver.implicitly_wait(0)

    yield driver

    logger.info("Tearing down Chrome WebDriver...")
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            reports_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(reports_dir, exist_ok=True)
            file_name = f"{item.name}.png"
            screenshot_path = os.path.join(reports_dir, file_name)
            driver.save_screenshot(screenshot_path)
            logger.error(f"Test failed! Screenshot saved to: {screenshot_path}")
            if pytest_html:
                html = f'<div><img src="screenshots/{file_name}" alt="screenshot" style="width:600px;height:auto;" onclick="window.open(this.src)"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
