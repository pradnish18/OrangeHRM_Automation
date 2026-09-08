import time
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config.config import Config
from utils.logger import logger

class BasePage:
    SPINNER_LOADER = (By.CSS_SELECTOR, ".oxd-form-loader, .oxd-loading-spinner")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    def open_url(self, url):
        logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible_element(self, locator):
        self.wait_for_spinner()
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_spinner(self, timeout=10):
        """Waits until any loading spinner overlay disappears from the DOM."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(self.SPINNER_LOADER)
            )
        except Exception:
            pass

    def click(self, locator):
        self.safe_click(locator)

    def safe_click(self, locator, retries=3):
        self.wait_for_spinner()
        for attempt in range(retries):
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                self.scroll_into_view(element)
                element.click()
                return
            except Exception as e:
                if attempt == retries - 1:
                    # Fallback to JavaScript click if standard click is intercepted
                    try:
                        element = self.driver.find_element(*locator)
                        self.driver.execute_script("arguments[0].click();", element)
                        return
                    except Exception:
                        raise e
                time.sleep(1)

    def type_text(self, locator, text, clear_first=True):
        element = self.find_visible_element(locator)
        if clear_first:
            try:
                element.clear()
            except Exception:
                pass
            # Cross-platform select-all + delete
            modifier = Keys.COMMAND if sys.platform == "darwin" else Keys.CONTROL
            element.send_keys(modifier, "a")
            element.send_keys(Keys.BACKSPACE)
            if element.get_attribute("value"):
                # Fallback manual backspace matching value length
                val_len = len(element.get_attribute("value"))
                element.send_keys(Keys.BACKSPACE * val_len)
        element.send_keys(str(text))

    def get_text(self, locator):
        element = self.find_visible_element(locator)
        return element.text.strip()

    def is_displayed(self, locator, timeout=5):
        try:
            custom_wait = WebDriverWait(self.driver, timeout)
            element = custom_wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except Exception:
            return False

    def hover_element(self, locator):
        element = self.find_visible_element(locator)
        logger.info("Performing mouse hover action...")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scroll_into_view(self, locator_or_element):
        if isinstance(locator_or_element, tuple):
            element = self.find_element(locator_or_element)
        else:
            element = locator_or_element
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def scroll_page(self, pixels=300):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        time.sleep(0.2)
