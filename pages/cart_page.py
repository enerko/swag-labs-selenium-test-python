from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()