import pytest
 
from config.settings import BASE_URL
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils.data_generator import generate_unique_email
 
 
# Verify subscription functionality
@pytest.mark.ui
@pytest.mark.regression
def test_subscription_functionality(page):
 
    home_page = HomePage(page)
    products_page = ProductsPage(page)
 
    # Open website
    home_page.open_home_page(BASE_URL)
 
    # Generate unique email
    email = generate_unique_email()
 
    # Subscribe
    products_page.subscribe(email)
 
    # Verify subscription success
    assert products_page.is_subscription_successful(), \
        "Subscription success message was not displayed"