import csv
import pytest
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

# Load test data from CSV
user_data = [
    tuple(row[:]) for row in csv.reader(open("data/valid_user_data.csv"))
    if row[0] != "username"
]

@pytest.mark.functional
@pytest.mark.parametrize("username, password", user_data)
def test_add_remove_backpack(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()

    assert products_page.get_cart_num() == 1, "Backpack was not added to the cart"

    products_page.remove_backpack_from_cart()

    # Verify cart is empty (cannot use get_cart_num since the element may not exist)
    assert len(products_page.get_cart_badge()) == 0, "Backpack was not removed from the cart"

@pytest.mark.functional
@pytest.mark.parametrize("username, password", user_data)
def test_add_backpack_go_to_cart(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.go_to_cart()

    assert "Sauce Labs Backpack" in driver.page_source, f"Backpack not in cart for {username}"

@pytest.mark.ui
@pytest.mark.parametrize("username, password", user_data)
def test_ui_elements(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    products_page = ProductsPage(driver)

    assert driver.find_element(*products_page.cart_button).is_displayed(), f"Cart icon is missing for {username}"
    assert driver.find_element(*products_page.menu_button).is_displayed(), f"Menu button is missing for {username}"

@pytest.mark.ui
@pytest.mark.parametrize("username, password", user_data)
def test_images(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    products_page = ProductsPage(driver)
    for img in products_page.get_product_images():
        assert img.get_attribute("src") != "", f"Broken image detected for {username}"

@pytest.mark.ui
@pytest.mark.parametrize("username, password", user_data)
def test_responsive_layout(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    products_page = ProductsPage(driver)
    # Set window to small size (mobile view)
    driver.set_window_size(375, 812)  # iPhone X size
    assert driver.find_element(*products_page.menu_button).is_displayed(), f"Menu button missing in mobile view for {username}"
    
    # Set window back to desktop size
    driver.set_window_size(1280, 800)
    assert driver.find_element(*products_page.cart_button).is_displayed(), f"Cart icon missing in desktop view for {username}"

@pytest.mark.ui
@pytest.mark.parametrize("username, password", user_data)
def test_text_style(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    products_page = ProductsPage(driver)

    product_title = products_page.get_product_title()
    assert product_title.value_of_css_property("font-size") == "20px", f"Incorrect font size for {username}"
