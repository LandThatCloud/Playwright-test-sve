from Config.config import TestData
import pytest
from playwright.sync_api import Playwright, sync_playwright
from Test_Methods.BasePage import Base

class LoginPage(Base):
    userName = "input[name=\"user-name\"]"
    passWord = "input[name=\"password\"]"
    loginButton = "input[name=\"submit\"]"

    def __init__(self, plywr: Playwright, base_url: str, headless=False):
        self.browser = plywr.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url
    
    def LoginPage(self, page):
        self.page = page

    def navigate(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)
    
    def webPage_Launch(self, url):
        self.page.goto(url=url)

    def urlTitle(self):
        title = self.page.title()
        print("The URL page title is: ", title)
        return title

    def perform_login(self, username: str, password: str):
        self.page.fill(self.userName, username)
        self.page.fill(self.passWord, password)
        self.page.click(self.loginButton)
    
    def close_session(self):
        self.page.close()
        self.context.close()
        self.browser.close()