# Omnify QA Engineer Assignment - Test Automation Framework

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.18%2B-green)
![Pytest](https://img.shields.io/badge/Pytest-8.0%2B-orange)
![Design Pattern](https://img.shields.io/badge/Pattern-Page%20Object%20Model%20(POM)-purple)

Professional test automation framework built for the **Omnify QA Engineer Assignment 2026** using **Python**, **Selenium WebDriver**, **Pytest**, and **Page Object Model (POM)** pattern.

---

## 🎯 Target Application
- **Application**: OrangeHRM Open Source Demo
- **URL**: [https://opensource-demo.orangehrmlive.com/web/index.php/auth/login](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)
- **Credentials**: Username: `Admin` | Password: `admin123`

---

## 🏗️ Framework Architecture

```
Omnify/
├── config/
│   └── config.py               # Application configuration & constants
├── pages/
│   ├── base_page.py            # Common Selenium interactions (waits, hover, scroll, type)
│   ├── login_page.py           # Login page locators & methods
│   ├── dashboard_page.py       # Dashboard header, sidebar navigation, mouse hover, logout
│   └── pim_page.py             # PIM module: Add Employee form & Employee List search/verification
├── utils/
│   ├── logger.py               # Custom logger for clean output & "Name Verified" logs
│   └── data_generator.py       # Helper to generate unique employee test data
├── tests/
│   ├── test_login.py           # Automated login test suite (valid, invalid, boundary)
│   └── test_pim_workflow.py    # Main E2E workflow requested by assignment
├── conftest.py                 # Pytest fixtures, driver management, screenshot on failure
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🚀 Key Features
1. **Page Object Model (POM)**: Strict separation of page locators, page actions, and test assertions.
2. **Explicit Waits**: Avoids hardcoded sleep calls by using Selenium `WebDriverWait` for high reliability.
3. **Mouse Hover Action**: Demonstrates mouse hovering over the PIM sidebar menu as specified in assignment requirements.
4. **Smooth Scrolling**: Dynamically scrolls to table elements when verifying added employees.
5. **Console Reporting**: Automatically logs `"Name Verified"` upon locating each added employee.
6. **HTML Test Reports**: Generates detailed execution reports using `pytest-html`.
7. **Failure Screenshots**: Automatically captures screenshots on test failure and embeds them in the HTML report.

---

## 💻 Prerequisites & Setup

### 1. Requirements
- Python 3.10 or higher
- Google Chrome Browser installed

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/<your-username>/Omnify-QA-Assignment.git
cd Omnify-QA-Assignment
pip install -r requirements.txt
```

---

## 🧪 Running Tests

### Run All Tests (Headed Mode)
```bash
pytest -s -v
```

### Run E2E PIM Workflow Test Only
```bash
pytest tests/test_pim_workflow.py -s -v
```

### Run Tests in Headless Mode
```bash
pytest --headless=true -s -v
```

### Generate HTML Test Report
```bash
pytest --html=reports/report.html --self-contained-html -s -v
```

---

## 📺 Assignment Verification Log Sample
```text
[2026-09-07 17:35:00] [INFO] [OmnifyQA]: === STEP 1: Automating Login Flow ===
[2026-09-07 17:35:01] [INFO] [OmnifyQA]: Opening URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
[2026-09-07 17:35:03] [INFO] [OmnifyQA]: Entering username: 'Admin'
[2026-09-07 17:35:03] [INFO] [OmnifyQA]: Entering password...
[2026-09-07 17:35:04] [INFO] [OmnifyQA]: Clicking Login button...
[2026-09-07 17:35:06] [INFO] [OmnifyQA]: === STEP 2: Navigating to PIM Module via Mouse Hover & Click ===
[2026-09-07 17:35:06] [INFO] [OmnifyQA]: Hovering mouse over PIM menu sidebar item...
[2026-09-07 17:35:07] [INFO] [OmnifyQA]: Clicking on PIM module...
[2026-09-07 17:35:09] [INFO] [OmnifyQA]: === STEP 3: Adding 4 New Employees ===
[2026-09-07 17:35:09] [INFO] [OmnifyQA]: Adding Employee: Alex QA Turner1 (ID: 9400101)
...
Name Verified
[2026-09-07 17:35:30] [INFO] [OmnifyQA]: Name Verified
...
[2026-09-07 17:35:45] [INFO] [OmnifyQA]: === STEP 6: Logging Out from Dashboard ===
```

---

## 📄 License
This project is submitted as part of the Omnify QA Engineer Hiring Assignment.
