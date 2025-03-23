from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutOverviewPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.finish_button = (By.ID, "finish")

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()