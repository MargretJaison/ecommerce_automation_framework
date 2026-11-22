class BasePage:
 
    def __init__(self, page):
        self.page = page
 
    # Navigate to a URL
    def navigate(self, url):
     self.page.goto( url,
        wait_until="domcontentloaded",
        timeout=60000
    )
 
    # Click an element
    def click(self, locator):
        self.page.locator(locator).click()
 
    # Enter text
    def enter_text(self, locator, text):
        self.page.locator(locator).fill(text)
 
    # Get element text
    def get_text(self, locator):
        return self.page.locator(locator).inner_text()
 
    # Check whether an element is visible
    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()
 
    # Get page title
    def get_title(self):
        return self.page.title()
 
    # Wait for an element
    def wait_for_element(self, locator):
        self.page.locator(locator).wait_for(state="visible")
 
    # Select dropdown option
    def select_option(self, locator, value):
        self.page.locator(locator).select_option(value)
 
    # Check whether an element is enabled
    def is_enabled(self, locator):
        return self.page.locator(locator).is_enabled()