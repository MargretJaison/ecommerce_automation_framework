import pytest
 
from config.settings import BASE_URL
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
 
 
@pytest.mark.ui
@pytest.mark.regression
def test_add_product_to_cart(page):
 
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
 
    home_page.open_home_page(BASE_URL)
    home_page.click_products()
 
    products_page.add_product_to_cart("Blue Top")
 
    cart_page.open_cart()
 
    assert cart_page.is_product_in_cart("Blue Top"), \
        "Blue Top was not added to the cart"
 
 
@pytest.mark.ui
@pytest.mark.regression
def test_verify_product_details_and_quantity_in_cart(page):
 
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
 
    home_page.open_home_page(BASE_URL)
    home_page.click_products()
 
    products_page.add_product_to_cart("Blue Top")
 
    cart_page.open_cart()
 
    assert cart_page.is_product_in_cart("Blue Top"), \
        "Product is not displayed in cart"
 
    assert cart_page.get_product_name() == "Blue Top", \
        "Incorrect product displayed in cart"
 
    assert cart_page.get_product_quantity() == "1", \
        "Product quantity is incorrect"
 
 
@pytest.mark.ui
@pytest.mark.regression
def test_remove_product_from_cart(page):
 
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
 
    # Step 1: Open application
    home_page.open_home_page(BASE_URL)
 
    # Step 2: Navigate to Products
    home_page.click_products()
 
    # Step 3: Add Blue Top to cart
    products_page.add_product_to_cart("Blue Top")
 
    # Step 4: Open cart
    cart_page.open_cart()
 
    # Step 5: Verify product is present
    assert cart_page.is_product_in_cart("Blue Top"), \
        "Product is not present before removal"
 
    # Step 6: Remove product
    cart_page.remove_product("Blue Top")
 
    # Step 7: Verify cart is empty
    assert cart_page.is_cart_empty(), \
        "Cart is not empty after removing the product"