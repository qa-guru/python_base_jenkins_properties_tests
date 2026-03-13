import os

# ENVIRONMENT=stage pytest . -s
def test_getenv():
    environment = os.getenv("ENVIRONMENT", "local")
    print(f"\nEnvironment: {environment}")

# pytest . -s --browser=chrome
def test_option(setup_browser):
    # assert True
    browser = setup_browser
    print(f"\nBrowser: {browser}")

# pytest . -s --browser=chrome --browser_version="100.0"
def test_options(setup_browser, browser_version):
    # assert True
    browser = setup_browser
    browser_version = browser_version
    print(f"\nBrowser: {browser}"
          f"\nVersion: {browser_version}")