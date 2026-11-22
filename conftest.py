 
import pytest
import re
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright
 
from config.settings import (
    BROWSER,
    HEADLESS,
    DEFAULT_TIMEOUT
)
from utils.api_client import APIClient
 
 
SCREENSHOTS_DIR = Path("screenshots")
SCREENSHOTS_DIR.mkdir(exist_ok=True)
 
 
@pytest.fixture
def page():
    with sync_playwright() as playwright:
 
        browser_type = getattr(playwright, BROWSER)
 
        browser = browser_type.launch(
            headless=HEADLESS
        )
 
        context = browser.new_context()
 
        browser_page = context.new_page()
 
        browser_page.set_default_timeout(
            DEFAULT_TIMEOUT
        )
 
        yield browser_page
 
        context.close()
        browser.close()
 
 
@pytest.fixture
def api_client():
    client = APIClient()
 
    yield client
 
    client.close()
 
 
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
 
    outcome = yield
    report = outcome.get_result()
 
    if report.when == "call" and report.failed:
 
        browser_page = item.funcargs.get("page")
 
        if browser_page:
 
            try:
                test_name = re.sub(
                    r"[^a-zA-Z0-9_-]",
                    "_",
                    item.nodeid
                )
 
                timestamp = datetime.now().strftime(
                    "%Y%m%d_%H%M%S"
                )
 
                screenshot_path = (
                    SCREENSHOTS_DIR /
                    f"{test_name}_{timestamp}.png"
                )
 
                browser_page.screenshot(
                    path=str(screenshot_path),
                    full_page=True
                )
 
                print(
                    f"\nScreenshot saved: {screenshot_path}"
                )
 
            except Exception as error:
                print(
                    f"\nScreenshot could not be saved: {error}"
                )
 