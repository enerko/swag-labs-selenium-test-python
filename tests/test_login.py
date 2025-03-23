import csv
import pytest
import time
from pages.login_page import LoginPage
from pages.cart_page import CartPage

# Load test data from CSV
user_data = [
    tuple(row[:]) for row in csv.reader(open("data/valid_user_data.csv"))
    if row[0] != "username"
]

@pytest.mark.performance
@pytest.mark.parametrize("username, password", user_data)
def test_login_time(driver, username, password):
    login_page = LoginPage(driver)

    start_time = time.time()
    login_page.login(username, password)

    end_time = time.time()
    login_duration = end_time - start_time
    
    max_login_time = 3.0

    assert login_duration <= max_login_time, f"{username} took more than {max_login_time} seconds to log in"

@pytest.mark.functional
@pytest.mark.parametrize("username, password", user_data)
def test_login_logout(driver, username, password):
    login_page = LoginPage(driver)

    login_page.login(username, password)

    cart_page = CartPage(driver)

    cart_page.click_menu()

    time.sleep(1)
    cart_page.click_logout()

    assert "Swag Labs" in driver.page_source, f"Couldn't logout for {username}"