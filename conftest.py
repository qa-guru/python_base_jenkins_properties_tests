import os

import pytest
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=("chrome", "mozilla", "firefox", "safari", "opera", "edge"),
        help="Browser to use"
    )
    parser.addoption(
        "--browser_version",
        default="100.0",
        help="Browser version to use"
    )
    parser.addoption(
        "--headless",
        default=False,
        choices=(True, False),
        help="Browser version to use"
    )
    parser.addoption(
        "--environment",
        default="",
        choices=("", "stage", "prod", "dev"),
        help="Browser version to use"
    )

@pytest.fixture(scope='function')
def setup_browser(request):
    browser = request.config.getoption("--browser")

    # print(f"\nBrowser: {browser}")
    return browser


@pytest.fixture(scope='function') # Not good practice
def browser_version(request):
    return request.config.getoption("--browser_version")



# pytest . -s --environment=prod
@pytest.fixture(scope='session', autouse=True)
def load_env(request):
    env_file = request.config.getoption("--environment", "") + ".env"
    load_dotenv(dotenv_path=env_file)

# # ENVIRONMENT=prod pytest . -s
# @pytest.fixture(scope='session', autouse=True)
# def load_env():
#     ENV_FILE = os.getenv("ENVIRONMENT", "") + ".env"
#     load_dotenv(dotenv_path=ENV_FILE)


# Base method to read from .env
# @pytest.fixture(scope='session', autouse=True)
# def load_env():
#     load_dotenv()
#     login = os.getenv("LOGIN")
#     password = os.getenv("PASSWORD")
#     print(f"\nLOGIN: {login}\n"
#           f"PASSWORD: {password}\n")