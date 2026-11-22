import pytest
 
from config.settings import BASE_URL
from pages.home_page import HomePage
 
 
@pytest.mark.ui
@pytest.mark.smoke
def test_home_page_loads(page):
 
    home_page = HomePage(page)
 
    # Open the home page
    home_page.open_home_page(BASE_URL)
 
    # Verify home page is loaded
    assert home_page.is_home_page_loaded(), \
        "Home page logo is not visible"
 
    # Verify page title
    assert "Automation Exercise" in home_page.get_title(), \
        "Incorrect home page title"