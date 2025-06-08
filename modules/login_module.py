# modules/login_module.py
import time

from appium.webdriver.common.appiumby import AppiumBy
from utils.utils import find_element, click_element, send_keys_to_element, scroll_until_element_found

# Custom describe and it functions
def describe(description):
    def decorator(cls):
        cls.__description__ = description
        return cls
    return decorator

def it(description):
    def decorator(func):
        func.__it_description__ = description
        return func
    return decorator


@describe("Login Feature")
class LoginPage:
    @it("should allow the user to write phone number to mobile input element")
    def test_write_phone_number(self, driver):
        driver.implicitly_wait(15)
        phone_input = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText')
        assert phone_input.is_displayed(), "Phone input element is displayed"

        phone_number = "9157069965"  # Example phone number
        phone_input.send_keys(phone_number)
    @it("should allow the user to send phone number")
    def test_send_phone_number(self, driver):
        time.sleep(4)

        # Click the "Continue" button
        continue_button = driver.find_element(
            by=AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]'
        )
        assert continue_button.is_displayed(), "Continue button is  displayed"
        continue_button.click()
    @it("allow permission for autofill")
    def test_allow_permission_autofill(self, driver):
        time.sleep(10)
        # Click the "Allow" button for permissions
        allow_button = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.Button[@resource-id="com.google.android.gms:id/positive_button"]'
        )
        assert allow_button.is_displayed(), "Allow button is displayed"
        allow_button.click()
    @it("allow permission for notification")
    def test_allow_permission_notification(self, driver):
        driver.implicitly_wait(15)
        permission_talk_notif = driver.find_element(
            by=AppiumBy.XPATH ,
            value='//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]')
        assert permission_talk_notif.is_displayed(), "permission talk notif is displayed"
        permission_talk_notif.click()
        permission_notif_system = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
        assert permission_notif_system.is_displayed(), "permission notif system is displayed"
        permission_notif_system.click()