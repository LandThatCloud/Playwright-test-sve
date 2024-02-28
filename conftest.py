"""This python file provides all the test setup/teardown and other important entities for our testing"""

"Import the necessary library"
from pytest import fixture
from playwright.sync_api import sync_playwright
from Test_methods.sauceDemo_LoginPage import LoginPage
from Test_methods.sauceDemo_HomePage import HomePage
from Config.config import TestData



@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def web_launch(get_playwright):
    web = LoginPage(get_playwright, base_url=TestData.baseURL)
    web.goto('/')
    yield web
    web.close_session()


@fixture()
def web_login(web_launch):
    web = web_launch
    web.login(TestData.userName, TestData.passWord)
    yield web


@fixture()
def home_Page_launch(get_playwright, web_login):
    home = HomePage(get_playwright, base_url=TestData.baseURL)
    home.goto('/')
    home.login(TestData.userName, TestData.passWord)
    yield home
