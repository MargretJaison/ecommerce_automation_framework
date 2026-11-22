E-Commerce Website Automation Testing

About the Project

This project focuses on automating the testing of an e-commerce website using Python, Playwright, Pytest, and Requests.
It includes UI automation and API testing to verify important website functionalities.
Website: https://automationexercise.com/

Technologies Used

Python
Playwright
Pytest
Requests
Page Object Model (POM)
HTML Test Reports
GitHub Actions

Project Structure

ecommerce_automation_framework/
│
├── config/          # Project configuration
├── pages/           # Page Object Model classes
├── tests/
│   ├── ui/          # UI test cases
│   └── api/         # API test cases
├── utils/           # Reusable utilities
├── reports/         # HTML test reports
├── screenshots/     # Failure screenshots
├── .github/
│   └── workflows/   # GitHub Actions workflow
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
└── README.md

UI Test Scenarios

The framework covers 15 UI test scenarios:

Verify home page loading.
Register a new user.
Verify account creation.
Login with valid credentials.
Login with invalid credentials.
Logout from the application.
Navigate to the Products page.
Search for a product.
View product details.
Add a product to the cart.
Verify product details and quantity in the cart.
Remove a product from the cart.
Navigate through product categories.
Navigate through product brands.
Verify subscription functionality.


API Test Scenarios

The framework covers following API scenarios:
GET Products List.
GET Brands List.
POST Search Product.
POST Verify Login.
POST Create Account.
PUT Update Account.
DELETE Account.
GET User Details by Email.


Installation and Setup

Step 1: Clone the repository
git clone <your-github-repository-url>

Step 2: Navigate to the project folder
cd ecommerce_automation_framework

Step 3: Install dependencies
pip install -r requirements.txt

Step 4: Install Playwright browser
playwright install chromium

Running Tests

Run all tests:
pytest tests -v

Run UI tests:
pytest tests/ui -v

Run API tests:
pytest tests/api -v

HTML Test Reports

Generate an HTML report:
pytest tests -v --html=reports/automation_report.html --self-contained-html
The report contains test execution results, including passed and failed test cases.

Screenshots

Screenshots are automatically captured when UI test cases fail.
They are stored in the screenshots/ folder.

CI/CD Integration

GitHub Actions is configured to execute automation tests automatically when code is pushed or a pull request is created.


\