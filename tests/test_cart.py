import csv
import pytest
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
import time
# Load test data from CSV
user_data = [
    tuple(row[:]) for row in csv.reader(open("data/valid_user_data.csv"))
    if row[0] != "username"
]

@pytest.mark.functional
@pytest.mark.parametrize("username, password", user_data)
def test_continue_shopping(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.go_to_cart()

    assert "Sauce Labs Backpack" in driver.page_source, f"Backpack not in cart for {username}"

    cart_page = CartPage(driver)
    cart_page.click_shopping()

    assert "Products" in driver.page_source, f"Couldn't go back to products page for {username}"
    
@pytest.mark.functional
@pytest.mark.parametrize("username, password", user_data)
def test_checkout(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.go_to_cart()

    assert "Sauce Labs Backpack" in driver.page_source, f"Backpack not in cart for {username}"

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    assert "Checkout" in driver.page_source, f"Couldn't proceed to checkout page for {username}"

    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.enter_first_name("John")
    checkout_info_page.enter_last_name("Doe")
    checkout_info_page.enter_postal_code("123456")
    checkout_info_page.click_continue()

    assert "Checkout: Overview" in driver.page_source, f"Couldn't proceed to checkout overview page for {username}"
    assert "Payment Information:" in driver.page_source, f"Checkout overview not displayed properly for {username}"

    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_overview_page.click_finish()

    assert "Checkout: Complete!" in driver.page_source, f"Couldn't finalize payment for {username}"

@pytest.mark.performance
@pytest.mark.parametrize("username, password", user_data)
def test_continue_shopping_time(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.go_to_cart()

    assert "Sauce Labs Backpack" in driver.page_source, f"Backpack not in cart for {username}"

    cart_page = CartPage(driver)

    start_time = time.time()
    cart_page.click_shopping()

    # Test how long it takes to load the products page
    end_time = time.time()
    load_time = end_time - start_time
    max_time = 2.0

    assert load_time <= max_time, f"{username} took more than {max_time} seconds to load products page"


