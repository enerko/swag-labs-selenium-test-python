from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.back_home_button = (By.ID, "back-to-products")

    def click_back_home(self):
        self.driver.find_element(*self.back_home_button).click()