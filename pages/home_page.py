from pages.base_page import BasePage
 
 
class HomePage(BasePage):
 
    def __init__(self, page):
        super().__init__(page)
 
        # Locators
        self.home_logo = "img[alt='Website for automation practice']"
        self.signup_login_link = "a[href='/login']"
        self.products_link = "a[href='/products']"
        self.cart_link = "a[href='/view_cart']"
        self.contact_us_link = "a[href='/contact_us']"
        self.test_cases_link = "a[href='/test_cases']"
        self.api_testing_link = "a[href='/api_list']"
 
    # Open home page
    def open_home_page(self, base_url):
        self.navigate(base_url)
 
    # Verify home page is loaded
    def is_home_page_loaded(self):
        try:
            self.page.locator(self.home_logo).wait_for(
                state="visible",
                timeout=10000
            )
            return True
        except Exception:
            return False
 
    # Click Signup/Login
    def click_signup_login(self):
        self.click(self.signup_login_link)
 
    # Click Products
    def click_products(self):
        self.click(self.products_link)
 
    # Click Cart
    def click_cart(self):
        self.click(self.cart_link)
 
    # Click Contact Us
    def click_contact_us(self):
        self.click(self.contact_us_link)
 
    # Click Test Cases
    def click_test_cases(self):
        self.click(self.test_cases_link)
 
    # Click API Testing
    def click_api_testing(self):
        self.click(self.api_testing_link)