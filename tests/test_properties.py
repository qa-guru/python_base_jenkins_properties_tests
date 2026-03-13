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

# create .env file with content
# LOGIN=...
# PASSWORD=...
def test_env():
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    print(f"\nLOGIN: {login}\n"
          f"PASSWORD: {password}\n")
    assert True

    # create .env file with content
    # LOGIN=...
    # PASSWORD=...

# ENVIRONMENT=prod pytest . -s
def test_env_with_environment_choice():
    environment = os.getenv("ENVIRONMENT", "local")
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    print(f"\nEnvironment: {environment}"
          f"\nLOGIN: {login}"
          f"\nPASSWORD: {password}\n")
    assert True


# pytest . -s --environment=prod
def test_env_with_environment_choice_with_options(request):
    environment = request.config.getoption("--environment", "")
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    print(f"\nEnvironment: {environment}"
          f"\nLOGIN: {login}"
          f"\nPASSWORD: {password}\n")
    assert True