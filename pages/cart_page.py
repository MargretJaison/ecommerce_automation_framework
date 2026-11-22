from pages.base_page import BasePage
 
 
class CartPage(BasePage):
 
    def __init__(self, page):
        super().__init__(page)
 
        self.cart_link = "a[href='/view_cart']"
        self.cart_table = "#cart_info_table"
        self.cart_rows = "#cart_info_table tbody tr"
        self.product_name = ".cart_description h4 a"
        self.product_price = ".cart_price p"
        self.product_quantity = ".cart_quantity button"
        self.product_total = ".cart_total_price"
        self.delete_button = ".cart_delete a"
        self.empty_cart_message = "#empty_cart"
 
    def open_cart(self):
 
        cart_modal = self.page.locator("#cartModal")
 
        if cart_modal.is_visible():
            cart_modal.get_by_role(
                "link", name="View Cart"
            ).click()
        else:
            self.page.locator(
                self.cart_link
            ).first.click()
 
        self.page.wait_for_url("**/view_cart")
 
    def is_cart_page_loaded(self):
        return self.is_visible(self.cart_table)
 
    def get_cart_product_count(self):
        return self.page.locator(self.cart_rows).count()
 
    def get_product_name(self, index=0):
        return self.page.locator(
            self.product_name
        ).nth(index).inner_text().strip()
 
    def get_product_price(self, index=0):
        return self.page.locator(
            self.product_price
        ).nth(index).inner_text()
 
    def get_product_quantity(self, index=0):
        return self.page.locator(
            self.product_quantity
        ).nth(index).inner_text().strip()
 
    def get_product_total(self, index=0):
        return self.page.locator(
            self.product_total
        ).nth(index).inner_text()
 
    def remove_product(self, product_name):
 
        product_row = self.page.locator(
            self.cart_rows
        ).filter(has_text=product_name).first
 
        product_row.locator(
            self.delete_button
        ).click()
 
        product_row.wait_for(
            state="detached",
            timeout=10000
        )
 
    def is_cart_empty(self):
        try:
            self.page.locator(
                self.empty_cart_message
            ).wait_for(
                state="visible",
                timeout=10000
            )
            return True
        except Exception:
            return False
 
    def is_product_in_cart(self, product_name):
        return self.page.locator(
            self.cart_rows
        ).filter(has_text=product_name).count() > 0