import pytest
from pages.cart_page import CartPage
from pages.login_page import LoginPage

def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    cart_page = CartPage(driver)
    cart_page.add_item_to_cart()
    cart_page.go_to_cart()

    assert "Sauce Labs Backpack" in driver.page_source