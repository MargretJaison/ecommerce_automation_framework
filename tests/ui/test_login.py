import pytest
 
from config.settings import BASE_URL
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from utils.data_generator import generate_user_data
 
 
def register_test_user(page):
    """Create a new user for login and logout tests."""
 
    user_data = generate_user_data()
 
    home_page = HomePage(page)
    signup_page = SignupPage(page)
    account_page = AccountPage(page)
 
    home_page.open_home_page(BASE_URL)
    home_page.click_signup_login()
 
    signup_page.start_signup(
        user_data["name"],
        user_data["email"]
    )
 
    signup_page.fill_account_information(user_data)
    signup_page.create_account()
 
    assert account_page.is_account_created(), \
        "Test account creation failed"
 
    account_page.continue_after_registration()
 
    return user_data
 
 
@pytest.mark.ui
@pytest.mark.regression
def test_valid_login(page):
 
    # Create a test account
    user_data = register_test_user(page)
 
    home_page = HomePage(page)
    login_page = LoginPage(page)
 
    # Logout after registration
    login_page.logout()
 
    # Login with valid credentials
    home_page.click_signup_login()
 
    login_page.login(
        user_data["email"],
        user_data["password"]
    )
 
    # Verify successful login
    assert login_page.is_logged_in(), \
        "Login with valid credentials failed"
 
 
@pytest.mark.ui
@pytest.mark.regression
def test_invalid_login(page):
 
    home_page = HomePage(page)
    login_page = LoginPage(page)
 
    # Open login page
    home_page.open_home_page(BASE_URL)
    home_page.click_signup_login()
 
    # Enter invalid credentials
    login_page.login(
        "invaliduser@example.com",
        "WrongPassword123"
    )
 
    # Verify error message
    assert "incorrect" in login_page.get_login_error().lower(), \
        "Invalid login error message was not displayed"
 
 
@pytest.mark.ui
@pytest.mark.regression
def test_logout(page):
 
    # Create and login a test user
    register_test_user(page)
 
    login_page = LoginPage(page)
 
    # Verify user is logged in
    assert login_page.is_logged_in(), \
        "User is not logged in before logout"
 
    # Logout
    login_page.logout()
 
    # Verify logout redirects to login page
    assert page.url.endswith("/login"), \
        "User was not redirected to login page after logout"