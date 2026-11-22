from pages.base_page import BasePage
 
 
class LoginPage(BasePage):
 
    def __init__(self, page):
        super().__init__(page)
 
        # Login form locators
        self.login_email = "[data-qa='login-email']"
        self.login_password = "[data-qa='login-password']"
        self.login_button = "[data-qa='login-button']"
 
        # Login error message
        self.login_error = ".login-form p"
 
        # Logged-in user and logout
        self.logged_in_user = "a:has-text('Logged in as')"
        self.logout_link = "a[href='/logout']"
 
    # Enter login credentials and submit
    def login(self, email, password):
        self.enter_text(self.login_email, email)
        self.enter_text(self.login_password, password)
        self.click(self.login_button)
 
    # Verify login error message
    def get_login_error(self):
        return self.get_text(self.login_error)
 
    # Verify successful login
    def is_logged_in(self):
        return self.is_visible(self.logged_in_user)
 
    # Logout from the application
    def logout(self):
        self.click(self.logout_link)