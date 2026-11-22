from pages.base_page import BasePage
 
 
class SignupPage(BasePage):
 
    def __init__(self, page):
        super().__init__(page)
 
        # Initial signup form
        self.signup_name = "[data-qa='signup-name']"
        self.signup_email = "[data-qa='signup-email']"
        self.signup_button = "[data-qa='signup-button']"
 
        # Account information
        self.gender_male = "#id_gender1"
        self.gender_female = "#id_gender2"
        self.password = "#password"
 
        # Date of birth
        self.days = "#days"
        self.months = "#months"
        self.years = "#years"
 
        # Additional information
        self.newsletter = "#newsletter"
        self.special_offers = "#optin"
 
        # Personal details
        self.first_name = "[data-qa='first_name']"
        self.last_name = "[data-qa='last_name']"
        self.company = "[data-qa='company']"
        self.address1 = "[data-qa='address']"
        self.address2 = "[data-qa='address2']"
        self.country = "#country"
        self.state = "[data-qa='state']"
        self.city = "[data-qa='city']"
        self.zipcode = "[data-qa='zipcode']"
        self.mobile_number = "[data-qa='mobile_number']"
 
        # Create account
        self.create_account_button = "[data-qa='create-account']"
 
        # Account creation confirmation
        self.account_created_message = "[data-qa='account-created']"
 
    # Start signup using name and email
    def start_signup(self, name, email):
        self.enter_text(self.signup_name, name)
        self.enter_text(self.signup_email, email)
        self.click(self.signup_button)
 
    # Fill account information
    def fill_account_information(self, details):
 
        # Select gender
        if details.get("gender") == "Male":
            self.page.locator(self.gender_male).check()
        else:
            self.page.locator(self.gender_female).check()
 
        # Enter password
        self.enter_text(self.password, details["password"])
 
        # Select date of birth
        self.page.locator(self.days).select_option(
            details["day"]
        )
 
        self.page.locator(self.months).select_option(
            details["month"]
        )
 
        self.page.locator(self.years).select_option(
            details["year"]
        )
 
        # Fill personal details
        self.enter_text(self.first_name, details["first_name"])
        self.enter_text(self.last_name, details["last_name"])
        self.enter_text(self.company, details["company"])
        self.enter_text(self.address1, details["address"])
        self.enter_text(self.address2, details.get("address2", ""))
 
        # Select country by visible label
        self.page.locator(self.country).select_option(
            label=details["country"]
        )
 
        self.enter_text(self.state, details["state"])
        self.enter_text(self.city, details["city"])
        self.enter_text(self.zipcode, details["zipcode"])
        self.enter_text(
            self.mobile_number,
            details["mobile_number"]
        )
 
        # Optional checkboxes
        if details.get("newsletter", False):
            self.page.locator(self.newsletter).check()
 
        if details.get("special_offers", False):
            self.page.locator(self.special_offers).check()
 
    # Submit account creation form
    def create_account(self):
        self.click(self.create_account_button)
 
    # Verify account creation
    def is_account_created(self):
        return self.is_visible(self.account_created_message)
 
    # Get account creation confirmation text
    def get_account_created_message(self):
        return self.get_text(self.account_created_message)