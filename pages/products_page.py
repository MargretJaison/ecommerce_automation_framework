 
from pages.base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
 
 
class ProductsPage(BasePage):
 
    def __init__(self, page):
        super().__init__(page)
 
        self.products_link = "a[href='/products']"
        self.products_title = "h2.title"
 
        # Search locators
        self.search_input = "#search_product"
        self.search_button = "#submit_search"
 
        # Product locators
        self.product_cards = ".product-image-wrapper"
        self.view_product_links = "a[href^='/product_details/']"
        self.product_information = ".product-information"
 
        # Category locators
        self.categories_section = "#accordian"
 
        # Brand locators
        self.brands_section = ".brands-name"
 
        # Subscription locators
        self.subscription_email = "#susbscribe_email"
        self.subscribe_button = "#subscribe"
        self.subscription_success = "#success-subscribe"
 
    # Open Products page
    def open_products_page(self):
        self.click(self.products_link)
 
    # Verify Products page
    def is_products_page_loaded(self):
        return self.is_visible(self.products_title)
 
    # Search product
    def search_product(self, product_name):
        self.enter_text(self.search_input, product_name)
        self.click(self.search_button)
 
    # Verify search results
    def is_search_results_displayed(self):
        return self.page.get_by_role(
            "heading", name="Searched Products"
        ).is_visible()
 
    # Get product count
    def get_product_count(self):
        return self.page.locator(self.product_cards).count()
 
    # View product details
    def view_product_details(self, index=0):
        self.page.locator(
            self.view_product_links
        ).nth(index).click()
 
    # Verify product details
    def is_product_details_displayed(self):
        return self.is_visible(self.product_information)
 
    # Add product to cart
    def add_product_to_cart(self, product_name):
 
        product = self.page.locator(
            self.product_cards
        ).filter(has_text=product_name).first
 
        product.wait_for(state="visible")
        product.scroll_into_view_if_needed()
        product.hover()
 
        add_button = product.locator(
            "a.add-to-cart"
        ).first
 
        add_button.wait_for(state="visible")
        add_button.click()
 
        # Wait for the cart popup, but do not fail
        # if the website does not display it.
        try:
            self.page.locator("#cartModal").wait_for(
                state="visible",
                timeout=5000
            )
        except PlaywrightTimeoutError:
            print(
                "\nCart popup was not displayed. "
                "Will verify the product directly in the cart."
            )
 
    # Select category
    def select_category(self, category_name):
        self.page.locator(
            self.categories_section
        ).get_by_text(
            category_name, exact=True
        ).click()
 
    # Select subcategory
    def select_subcategory(self, subcategory_name):
        self.page.get_by_role(
            "link",
            name=subcategory_name,
            exact=True
        ).click()
 
    # Select brand
    def select_brand(self, brand_name):
 
        brand_locator = self.page.locator(
            f".brands-name a[href='/brand_products/{brand_name}']"
        )
 
        brand_locator.wait_for(
            state="visible",
            timeout=10000
        )
 
        brand_locator.click()
 
    # Enter subscription email
    def enter_subscription_email(self, email):
        self.enter_text(
            self.subscription_email,
            email
        )
 
    # Subscribe
    def subscribe(self, email):
        self.enter_subscription_email(email)
        self.click(self.subscribe_button)
 
    # Verify subscription
    def is_subscription_successful(self):
        return self.is_visible(
            self.subscription_success
        )
 