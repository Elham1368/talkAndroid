import pytest
from modules.login_module import LoginPage
from conftests import driver

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_write_phone_number(self, driver):
        login_page = LoginPage(self.driver)
        login_page.enter_phone_number("9157069965")

    def test_send_phone_number(self, driver):
        login_page = LoginPage(driver)
        login_page.click_continue_button()

    def test_allow_permission_autofill(self, driver):
        login_page = LoginPage(driver)
        login_page.allow_autofill_permission()

    def test_allow_permission_notification(self, driver):
        login_page = LoginPage(driver)
        login_page.allow_notification_permission()