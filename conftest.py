import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    return driver

@pytest.fixture
def driver():
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

test_results = {}

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.when == "call": 
        nodeid = report.nodeid
        keywords = report.keywords
        outcome = report.outcome

        # Extract username from test parameters in format: test_name[username-password])
        if "[" in nodeid and "-" in nodeid:
            username = nodeid.split("[")[1].split("-")[0]
        else:
            username = "unknown_user"

        valid_markers = [mark for mark in keywords if mark in {"ui", "performance", "functional"}]

        if username not in test_results:
            test_results[username] = {}

        for marker in valid_markers:
            if marker not in test_results[username]:
                test_results[username][marker] = {"passed": 0, "failed": 0}

            test_results[username][marker][outcome] += 1

def pytest_sessionfinish(session, exitstatus):
    report_lines = []
    report_lines.append("\n===== Test Results by Username & Test Type =====\n")

    for user, test_types in test_results.items():
        report_lines.append(f"\nUsername: {user}")
        for test_type, counts in test_types.items():
            total = counts["passed"] + counts["failed"]
            pass_percentage = (counts["passed"] / total) * 100 if total > 0 else 0
            fail_percentage = (counts["failed"] / total) * 100 if total > 0 else 0
            report_lines.append(f"  {test_type.capitalize()} Tests - Passed: {counts['passed']} ({pass_percentage:.2f}%), Failed: {counts['failed']} ({fail_percentage:.2f}%)")

    # Print summary to console
    report = "\n".join(report_lines)
    print(report)

    # Write to a file
    with open("test_summary_report.txt", "w") as f:
        f.write(report)

    print("\nTest summary report has been saved to 'test_summary_report.txt'")
