OrangeHRM Test Automation Framework (POM)

A professional Selenium-Python test automation framework for the OrangeHRM application, built using the Page Object Model (POM) design pattern.

The framework is designed to provide better maintainability, readability, reusability, and scalability by separating page-level actions and locators from test logic.

🚀 Features

* Page Object Model (POM)
    Separates page locators and page actions from test cases for better maintainability.
* Dynamic Waits
    Uses Selenium’s WebDriverWait to handle asynchronous element loading and improve test stability.
* Data-Driven Approach
    Supports adding and validating multiple employees using reusable test logic and loops.
* Reusable Page Methods
    Common browser interactions such as clicking, typing, and hovering are implemented as reusable wrapper methods.
* Pytest Integration
    Uses Pytest for test execution and clear pass/fail reporting.
* End-to-End Workflow Automation
    Automates the OrangeHRM employee-management workflow from login through employee verification.

📂 Project Structure

OrangeHRM_Automation/
│
├── pages/
│   ├── base_page.py          # Common reusable Selenium methods
│   ├── login_page.py         # Login page locators and actions
│   └── pim_page.py           # PIM/Employee management locators and actions
│
├── tests/
│   └── test_workflow.py      # Main end-to-end test workflow
│
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation

🛠️ Technologies Used

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)

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

* Login-related changes → login_page.py
* Employee/PIM changes → pim_page.py
* Common Selenium interactions → base_page.py
* Test scenarios → test_workflow.py

This reduces code duplication and makes the test suite easier to scale.
