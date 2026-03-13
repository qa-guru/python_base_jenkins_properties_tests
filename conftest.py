import pytest


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

@pytest.fixture(scope='function')
def setup_browser(request):
    browser = request.config.getoption("--browser")

    # print(f"\nBrowser: {browser}")
    return browser

@pytest.fixture(scope='function')
def browser_version(request):
    return request.config.getoption("--browser_version")