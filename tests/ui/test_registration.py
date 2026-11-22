import pytest
 
from config.settings import BASE_URL
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.account_page import AccountPage
from utils.data_generator import generate_user_data
 
 
#  Register a new user
@pytest.mark.ui
@pytest.mark.regression
def test_register_new_user(page):
 
    user_data = generate_user_data()
 
    home_page = HomePage(page)
    signup_page = SignupPage(page)
 
    home_page.open_home_page(BASE_URL)
    home_page.click_signup_login()
 
    signup_page.start_signup(
        user_data["name"],
        user_data["email"]
    )
 
    signup_page.fill_account_information(user_data)
    signup_page.create_account()
 
    assert page.locator(
        "[data-qa='account-created']"
    ).is_visible(), "Account registration failed"
 
 
# Verify successful account creation
@pytest.mark.ui
@pytest.mark.regression
def test_verify_account_creation(page):
 
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
        "Account created message is not displayed"
 
    assert "ACCOUNT CREATED" in \
        account_page.get_account_created_message().upper(), \
        "Incorrect account creation message"
 
    account_page.continue_after_registration()
 
    assert account_page.is_user_logged_in(), \
        "User is not logged in after account creation"