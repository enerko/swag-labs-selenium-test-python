from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.shopping_button = (By.ID, "continue-shopping")

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
    
    def click_shopping(self):
        self.driver.find_element(*self.shopping_button).click()