import pytest
 
from config.settings import BASE_URL
from pages.home_page import HomePage
from pages.products_page import ProductsPage
 
 
# Navigate to Products page
@pytest.mark.ui
@pytest.mark.regression
def test_navigate_to_products_page(page):
 
    home_page = HomePage(page)
    products_page = ProductsPage(page)
 
    home_page.open_home_page(BASE_URL)
    home_page.click_products()
 
    assert products_page.is_products_page_loaded(), \
        "Products page is not loaded"
 
 
#Search for a product
@pytest.mark.ui
@pytest.mark.regression
def test_search_product(page):
 
    home_page = HomePage(page)
    products_page = ProductsPage(page)
 
    home_page.open_home_page(BASE_URL)
    home_page.click_products()
 
    products_page.search_product("Blue Top")
 
    assert products_page.is_search_results_displayed(), \
        "Search results heading is not displayed"
 
    assert products_page.get_product_count() > 0, \
        "No products found"
 
 
# View product details
@pytest.mark.ui
@pytest.mark.regression
def test_view_product_details(page):
 
    home_page = HomePage(page)
    products_page = ProductsPage(page)
 
    home_page.open_home_page(BASE_URL)
    home_page.click_products()
 
    products_page.view_product_details()
 
    assert products_page.is_product_details_displayed(), \
        "Product details are not displayed"
 
 
# Navigate through product categories
@pytest.mark.ui
@pytest.mark.regression
def test_navigate_through_product_categories(page):
 
    home_page = HomePage(page)
    products_page = ProductsPage(page)
 
    home_page.open_home_page(BASE_URL)
    home_page.click_products()
 
    products_page.select_category("Women")
    products_page.select_subcategory("Dress")
 
    assert "category_products/1" in page.url, \
        "Women Dress category page was not opened"
 
    assert products_page.get_product_count() > 0, \
        "No products found in Women Dress category"
 
 
# Navigate through product brands
@pytest.mark.ui
@pytest.mark.regression
def test_navigate_through_product_brands(page):
 
    home_page = HomePage(page)
    products_page = ProductsPage(page)
 
    home_page.open_home_page(BASE_URL)
    home_page.click_products()
 
    products_page.select_brand("Polo")
 
    assert "brand_products/Polo" in page.url, \
        "Polo brand page was not opened"
 
    assert products_page.get_product_count() > 0, \
        "No products found for Polo brand"