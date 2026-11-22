from pages.base_page import BasePage
 
 
class AccountPage(BasePage):
 
    def __init__(self, page):
        super().__init__(page)
 
        # Account creation confirmation
        self.account_created_message = "[data-qa='account-created']"
        self.continue_button = "[data-qa='continue-button']"
 
        # Logged-in user confirmation
        self.logged_in_user = "a:has-text('Logged in as')"
 
        # Account deletion
        self.delete_account_link = "a[href='/delete_account']"
        self.account_deleted_message = "[data-qa='account-deleted']"
 
    # Verify account creation
    def is_account_created(self):
        return self.is_visible(self.account_created_message)
 
    # Get account creation confirmation
    def get_account_created_message(self):
        return self.get_text(self.account_created_message)
 
    # Continue after account creation
    def continue_after_registration(self):
        self.click(self.continue_button)
 
    # Verify user is logged in
    def is_user_logged_in(self):
        return self.is_visible(self.logged_in_user)
 
    # Delete the current account
    def delete_account(self):
        self.click(self.delete_account_link)
 
    # Verify account deletion
    def is_account_deleted(self):
        return self.is_visible(self.account_deleted_message)
 
    # Get account deletion confirmation
    def get_account_deleted_message(self):
        return self.get_text(self.account_deleted_message)