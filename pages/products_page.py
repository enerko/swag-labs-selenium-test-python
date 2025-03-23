from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_backpack_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.remove_backpack_from_cart_button = (By.ID, "remove-sauce-labs-backpack")
        self.add_bike_to_cart_button = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.product_images = (By.CLASS_NAME, "inventory_item_img")
        self.product_title = (By.CLASS_NAME, "inventory_item_name")

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.add_backpack_to_cart_button).click()

    def add_bike_to_cart(self):
        self.driver.find_element(*self.add_bike_to_cart_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()

    def remove_backpack_from_cart(self):
        self.driver.find_element(*self.remove_backpack_from_cart_button).click()
        
    def get_product_images(self):
        return self.driver.find_elements(*self.product_images)
    
    def get_product_title(self):
        return self.driver.find_element(*self.product_title)