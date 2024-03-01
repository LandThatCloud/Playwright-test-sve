from playwright.sync_api import Page
from Config.config import TestData
from playwright.sync_api import Playwright, sync_playwright


class Base(object):
    userName = "input[id=\"user-name\"]"
    passWord = "input[id=\"password\"]"
    loginButton = "[data-test=\"login-button\"]"

    def __init__(self, plywr: Playwright, base_url: str, headless=False):
        self.browser = plywr.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    """Go to base-URL"""

    def webPage_Launch(self, url):
        self.page.goto(url=url)

    def login(self, username: str, password: str):
        self.page.fill(self.userName, username)
        self.page.fill(self.passWord, password)
        self.page.click(self.loginButton)
