from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def click_menu(self):
        """Opens the sidebar menu."""
        self.driver.find_element(*self.menu_button).click()

    def click_logout(self):
        """Clicks logout button (only works if menu is open)."""
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()

    def get_cart_num(self):
        """Get the number next to the cart icon."""
        return int(self.driver.find_element(*self.cart_badge).text)
    
    def get_cart_badge(self):
        return self.driver.find_elements(*self.cart_badge) 
