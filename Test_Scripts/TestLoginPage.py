import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from Test_Methods.LoginPage import *
import conftest
from Config.config import TestData

class TestLoginPage:
    """Test case to verify the URL Title"""

    def test_URL_Title(self, web_launch):
        urlTitle = web_launch.urlTitle()
        assert urlTitle == TestData.urlTitle

    def test_User_Login(self, perform_login):