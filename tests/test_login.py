import pytest
from pages.login_page import LoginPage

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("wrong_user", "wrong_password")
    assert "Epic sadface" in driver.page_source

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "Products" in driver.page_source