from typing import Iterator

import pytest
from playwright.sync_api import Page, BrowserContext, Browser, sync_playwright

from web_practice.pages.dashboard_page import DashboardPage


@pytest.fixture(scope="session")
def browser() -> Iterator[Browser]:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        try:
            yield browser
        finally:
            browser.close()


@pytest.fixture
def context(browser: Browser) -> Iterator[BrowserContext]:
    context = browser.new_context()
    try:
        yield context
    finally:
        context.close()


@pytest.fixture
def page(context: BrowserContext) -> Iterator[Page]:
    page = context.new_page()
    try:
        yield page
    finally:
        page.close()


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)


@pytest.fixture
def pump_id() -> str:
    return "12"
