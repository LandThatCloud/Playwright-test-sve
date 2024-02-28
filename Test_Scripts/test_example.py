from playwright.sync_api import sync_playwright, Page
from pages import login

with sync_playwright() as pageObj:
    def login_test():
        browser = pageObj.chromium.launch()
        page = browser.new_page()
        login_page = login(page)
        login_page.navigate()