# Omnify QA Engineer Assignment - Test Automation Framework

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.18%2B-green)
![Pytest](https://img.shields.io/badge/Pytest-8.0%2B-orange)
![Design Pattern](<https://img.shields.io/badge/Pattern-Page%20Object%20Model%20(POM)-purple>)

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
OrangeHRM Test Automation Framework (POM)

A professional Selenium-Python test automation framework for the OrangeHRM application, built using the Page Object Model (POM) design pattern.

The framework is designed to provide better maintainability, readability, reusability, and scalability by separating page-level actions and locators from test logic.

🚀 Features

- Page Object Model (POM)
  Separates page locators and page actions from test cases for better maintainability.
- Dynamic Waits
  Uses Selenium’s WebDriverWait to handle asynchronous element loading and improve test stability.
- Data-Driven Approach
  Supports adding and validating multiple employees using reusable test logic and loops.
- Reusable Page Methods
  Common browser interactions such as clicking, typing, and hovering are implemented as reusable wrapper methods.
- Pytest Integration
  Uses Pytest for test execution and clear pass/fail reporting.
- End-to-End Workflow Automation
  Automates the OrangeHRM employee-management workflow from login through employee verification.

📂 Project Structure

OrangeHRM_Automation/
│
├── pages/
│ ├── base_page.py # Common reusable Selenium methods
│ ├── login_page.py # Login page locators and actions
│ └── pim_page.py # PIM/Employee management locators and actions
│
├── tests/
│ └── test_workflow.py # Main end-to-end test workflow
│
├── requirements.txt # Project dependencies
└── README.md # Project documentation

🛠️ Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)

⚙️ Setup Instructions

1. Clone the Repository

git clone <your-repo-link>
cd OrangeHRM_Automation

2. Install Dependencies

pip install -r requirements.txt

3. Run the Automation Tests

pytest tests/test_workflow.py -s

The -s flag allows console output, including the “Name Verified” messages, to be displayed during test execution.

🧪 Test Workflow

The automation framework covers the following workflow:

1. Launch the OrangeHRM application.
2. Log in using valid credentials.
3. Navigate to the PIM (Personnel Information Management) module.
4. Add employee records.
5. Verify the added employee names.
6. Display verification results in the console.
7. Generate the final Pytest test result.

📊 Test Execution

Run:

pytest tests/test_workflow.py -s

Example console output:

Name Verified: John Doe
Name Verified: Jane Smith
===================== test session starts =====================
...
===================== 1 passed ================================

🏗️ Architecture

The framework follows the Page Object Model (POM) architecture:

                 ┌─────────────────────┐
                 │    Test Workflow    │
                 │ test_workflow.py    │
                 └──────────┬──────────┘
                            │
                ┌───────────┴───────────┐
                │                       │
        ┌───────▼────────┐     ┌────────▼───────┐
        │   Login Page   │     │    PIM Page    │
        │  login_page.py │     │   pim_page.py  │
        └───────┬────────┘     └────────┬───────┘
                │                       │
                └───────────┬───────────┘
                            │
                   ┌────────▼────────┐
                   │    Base Page    │
                   │  base_page.py   │
                   └────────┬────────┘
                            │
                   ┌────────▼─────────┐
                   │ Selenium WebDriver│
                   └──────────────────┘

This structure keeps test logic independent from page implementation, making the framework easier to update when the application’s UI changes.

📌 Maintainability

The framework is designed so that changes to OrangeHRM’s UI can be handled primarily within the relevant page object.

For example:

- Login-related changes → login_page.py
- Employee/PIM changes → pim_page.py
- Common Selenium interactions → base_page.py
- Test scenarios → test_workflow.py

This reduces code duplication and makes the test suite easier to scale.
