# E-Commerce Automation Testing Framework
 
## Project Overview
 
An automation testing framework developed to test the functionalities of an e-commerce website using Python, Playwright, Pytest, and Requests.
 
The framework performs UI automation and API testing to validate application functionality and verify expected results.
 
**Application Under Test:** https://automationexercise.com/
 
## Tech Stack
 
- Python
- Playwright
- Pytest
- Requests
- Page Object Model (POM)
- Pytest HTML Reporting
- GitHub Actions
 
## Testing Coverage
 
### UI Automation
 
A total of 15 UI test scenarios are automated:
 
1. Home page verification
2. User registration
3. Successful account creation
4. Login with valid credentials
5. Login with invalid credentials
6. User logout
7. Products page navigation
8. Product search
9. Product details verification
10. Add product to cart
11. Cart product and quantity verification
12. Remove product from cart
13. Product category navigation
14. Product brand navigation
15. Subscription functionality
 
### API Automation
 
The framework covers the following 8 API functionalities:
 
| HTTP Method | Functionality |
|---|---|
| GET | Retrieve Products List |
| GET | Retrieve Brands List |
| POST | Search Products |
| POST | Verify Login |
| POST | Create Account |
| PUT | Update Account |
| DELETE | Delete Account |
| GET | Retrieve User Details by Email |
 
Additional positive and negative test scenarios are included to validate API responses.
 
## Project Execution
 
### Install Dependencies
 

pip install -r requirements.txt

 
### Install Playwright Browser
 

playwright install chromium

 
### Run UI Tests
 

pytest tests/ui -v

 
### Run API Tests
 

pytest tests/api -v

 
### Run All Tests
 

pytest tests -v

 
## Automation Reports
 
HTML reports are generated using Pytest HTML.
 
The framework generates three types of reports:
 
1. **UI Automation Report:** Displays the execution results of UI test cases.
2. **API Automation Report:** Displays the execution results of API test cases.
3. **Combined Automation Report:** Provides a consolidated view of both UI and API test execution results in a single HTML report.
 
### Generate UI Report
 
pytest tests/ui -v -s --html=reports/ui_report.html --self-contained-html

 
### Generate API Report
 

pytest tests/api -v -s --html=reports/api_report.html --self-contained-html

 
### Generate Combined Automation Report
 

pytest tests -v -s --html=reports/automation_report.html --self-contained-html

 
All reports are saved in the `reports/` directory.
 
The reports provide details about passed and failed test cases, execution status, and failure information.
 
Screenshots are automatically captured when UI test cases fail.
 
## Test Execution Results
 
| Test Suite | Total Tests | Passed |
|---|---:|---:|
| UI Automation | 15 | 15 |
| API Automation | 9 | 9 |
| **Overall** | **24** | **24** |
 
## CI/CD Integration
 
GitHub Actions is integrated to execute automation tests whenever code is pushed or a pull request is created.
 
Test reports and screenshots are uploaded as workflow artifacts.