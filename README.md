# **Automated Testing for SauceDemo**

This project is a data-driven automated testing framework for [**SauceDemo**](https://www.saucedemo.com) written in Python, designed to validate UI functionality, 
login authentication, shopping cart operations, and performance. It includes tests for user interactions, visual consistency, and system responsiveness, ensuring a seamless e-commerce experience.

The framework supports:
- Headless execution for faster and efficient tests.
- Test categorization (UI, performance, functional).
- Structured test reporting to help you track test results and their outcomes.

The tests are implemented using:
- **[Selenium](https://www.selenium.dev/)** for automating web browser interactions.
- **[Chrome WebDriver](https://sites.google.com/chromium.org/driver/)** to run tests on Chrome.
- **[Pytest](https://docs.pytest.org/en/stable/)** for organizing, running, and reporting tests.

## Key Features:
- Automated UI Testing: Tests the core UI elements of the website.
- Performance Testing: Measures page load times and responsiveness.
- Functional Testing: Validates core functionalities like login, cart operations, and checkouts.
- Headless Execution: Run tests without opening the browser, making the tests faster.
- Detailed Reporting: Generates detailed test reports categorized by users and test types.
- Parameterized Tests: Supports multiple user roles, including `standard_user`, `problem_user`, and others.
