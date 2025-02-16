import time
from wsgiref.validate import validator

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import pytest
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

# Appium setup and teardown
@pytest.fixture(scope="module")
def driver():
    capabilities = {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "deviceName": "Galaxy A52",
        "appium:appPackage": "ir.dotin.talk",
        "appium:appActivity": "ir.dotin.talk.presentation.main.MainActivity",
        "appium:newCommandTimeout": 120000,
        # "appium:noReset": True,

        # "app":apk_path,
    }
    appium_server_url = 'http://127.0.0.1:4723'  #Appium Server Address
    driver = None

    driver = webdriver.Remote(appium_server_url,
                              options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver


# Test cases
@describe("Login Feature")
class TestLogin:
    @it("should allow the user to write phone number to mobile input element")
    def test_write_phone_number(self, driver):
        driver.implicitly_wait(15)
        phone_input = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText')
        assert phone_input.is_displayed(), "Phone input element is displayed"

        phone_number = "9157069965"  # Example phone number
        phone_input.send_keys(phone_number)
    @it("should allow the user to send phone number")
    def test_send_phone_number(self, driver):
        driver.implicitly_wait(15)

        # Click the "Continue" button
        continue_button = driver.find_element(
            by=AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]'
        )
        assert continue_button.is_displayed(), "Continue button is  displayed"
        continue_button.click()
    @it("allow permission for autofill")
    def test_allow_permission_autofill(self, driver):
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

@describe("create single thread")
class TestCreateSingleThread:
    @it("open menu and add contact")
    def test_open_menu_add_contact(self, driver):
        #click on menu
        toggle_menu = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="Toggle drawer"]'
        )
        assert toggle_menu.is_displayed(), 'toggle menu find'
        toggle_menu.click()
        #click on add contact
        add_contact=driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.TextView[@text="افزودن مخاطب جدید"]'
        )
        assert add_contact.is_displayed(),'add contact find'
        add_contact.click()
        #check add contact modal is opened
        add_contact_modal = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View/android.view.View[2]'

        )
        assert add_contact_modal.is_displayed(),'add contact modal find'
    @it("create contact")
    def test_create_contact(self, driver):
        name = 'elham'
        family = 'تست 2'
        phone_number = '09371521106'
        #fill contact name
        contact_name = driver.find_element(
            by=AppiumBy,
            value='//android.widget.ScrollView/android.widget.EditText[1]'
        )
        assert contact_name.is_displayed(), 'contact name find'
        contact_name.click()
        # contact_name.send_keys(name)
        # #fill contact family
        # contact_family = driver.find_element(
        #     by=AppiumBy,
        #     value='//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]'
        # )
        # assert contact_family.is_displayed(),'contact family find'
        # contact_family.send_keys(family)
        # #fill contact mobile number
        # contact_phone = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value= '//android.widget.ScrollView/android.widget.EditText[3]'
        # )
        # assert contact_phone.is_displayed()
        # contact_phone.send_keys(phone_number)
        # #click on add contact افزودن
        # add_button = driver.find_element(
        #     by=AppiumBy,
        #     value='//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View'
        # )
        # assert add_button.is_displayed(),'add button find'
        # add_button.click()
    # @it("check contact is added or not")
    # def test_check_contact_add(self,driver):








