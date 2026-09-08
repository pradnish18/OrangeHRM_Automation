import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)

try:
    print("1. Navigating to login page...")
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    print("2. Logging in...")
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    print("3. Waiting for dashboard / main menu...")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='PIM']")))
    print("Logged in successfully. Current URL:", driver.current_url)
    
    print("4. Hovering and clicking PIM...")
    pim_elem = driver.find_element(By.XPATH, "//span[text()='PIM']")
    from selenium.webdriver.common.action_chains import ActionChains
    ActionChains(driver).move_to_element(pim_elem).click().perform()
    
    wait.until(lambda d: "pim" in d.current_url.lower())
    print("PIM page loaded. Current URL:", driver.current_url)
    
    print("5. Clicking Add Employee...")
    add_emp_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Add Employee']")))
    add_emp_tab.click()
    
    wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
    print("Add Employee form visible. Current URL:", driver.current_url)
    
    print("6. Adding employee...")
    driver.find_element(By.NAME, "firstName").send_keys("TestFirst")
    driver.find_element(By.NAME, "lastName").send_keys("TestLast")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    print("7. Waiting for save completion...")
    wait.until(lambda d: "viewPersonalDetails" in d.current_url)
    print("Employee saved! Personal details URL:", driver.current_url)
    
    print("8. Navigating to Employee List...")
    emp_list_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Employee List']")))
    emp_list_tab.click()
    
    wait.until(lambda d: "viewEmployeeList" in d.current_url)
    print("Employee List page loaded.")
    
    print("9. Searching for employee TestFirst...")
    search_input = wait.until(EC.visibility_of_element_located((
        By.XPATH, "//label[normalize-space()='Employee Name']/parent::div/following-sibling::div//input"
    )))
    search_input.send_keys("TestFirst")
    time.sleep(2) # allow autocomplete options to render
    
    # Check if autocomplete dropdown appears
    autocomplete_options = driver.find_elements(By.CSS_SELECTOR, ".oxd-autocomplete-option")
    print(f"Found {len(autocomplete_options)} autocomplete options")
    for opt in autocomplete_options:
        print("Option text:", opt.text)
        if "TestFirst" in opt.text:
            opt.click()
            break
            
    print("10. Clicking Search button...")
    search_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
    search_btn.click()
    
    time.sleep(3)
    
    # Locate table rows/cards
    cards = driver.find_elements(By.CSS_SELECTOR, ".oxd-table-card")
    print(f"Found {len(cards)} table cards")
    found = False
    for card in cards:
        print("Card text:", card.text)
        if "TestFirst" in card.text:
            found = True
            break
    print("Verification result:", found)
    
    print("11. Testing Logout...")
    user_dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-name")))
    user_dropdown.click()
    
    logout_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']")))
    logout_link.click()
    
    wait.until(lambda d: "login" in d.current_url.lower())
    print("Logout successful. Current URL:", driver.current_url)

finally:
    driver.quit()
