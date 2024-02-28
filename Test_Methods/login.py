class Login:
    def __init__(self, page):
        self.page = page
        self.username_text = page.locator("input[name=\"username\"]")
        self.password_text = page.locator("input[name=\"password\"]")
        self.login_btn = page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto("https://mbg73.mivb.kanata.cloudlink.systems")

    def perform_login(self, uname, pwd):
        self.username_text.fill(uname)
        self.password_text.press(pwd)
        self.login_btn.click()
        # expect(self.page).to_have_title(re.compile("mbg73"))