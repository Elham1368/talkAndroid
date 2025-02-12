import time
# from wsgiref.validate import assert_

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium.options.common.base import APPIUM_PREFIX
from appium.webdriver.common.appiumby import AppiumBy
import pytest
import os

from selenium.webdriver.common.devtools.v129.fed_cm import click_dialog_button


# Custom describe and it functions
def describe(description):
    def decorator(func):
        func.__description__ = description
        return func

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
# @describe("Send Message")
# class SendTextMessage:
    @it("select single thread")
    def test_select_single_thread(self, driver):
        single_thread = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.TextView[@text="الهام Test😶"]')
        assert single_thread.is_displayed(), "single thread الهام test is find"
        single_thread.click()

    # @it("type and send simple text history")
    # def test_type_and_send_simple_text_history(self, driver):
    #     click_input = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.EditText[@text="اینجا بنویسید…"]')
    #     assert click_input.is_displayed(), "input for typing message is find a"
    #     click_input.click()
    #     click_input.send_keys("این یک پیام تستی برای اتومیشن اندروید است ")
    #     send_text_message = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.view.View[@content-desc="send"]'
    #     )
    #     assert send_text_message.is_displayed(), "send icon is find"
    #     send_text_message.click()
    #
    # @it("select image and send to history")
    # def test_select_image_and_send_to_history(self, driver):
    #     click_attach_icon = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]'
    #     )
    #     assert click_attach_icon.is_displayed(), "attach Icon is find"
    #     click_attach_icon.click()
    #     select_gallery = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.TextView[@text="گالری"]'
    #     )
    #     assert select_gallery.is_displayed(), "gallery is find"
    #     select_gallery.click()
    #
    #     permission_gallery = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]'
    #     )
    #     assert permission_gallery.is_displayed()
    #     permission_gallery.click()
    #
    #     allow_permission = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_all_button"]'
    #     )
    #     assert allow_permission.is_displayed()
    #     allow_permission.click()
    #
    #     image_name = "Photo taken on 29 Jan 2025, 11:08:23 pm"
    #
    #     # Use UiScrollable to scroll until the image is found
    #     scrollable_gallery = 'new UiScrollable(new UiSelector().resourceId("com.google.android.providers.media.module:id/bottom_sheet")).scrollIntoView(new UiSelector().descriptionContains("{}"))'.format(image_name)
    #
    #     # Execute scrolling command
    #     driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scrollable_gallery)
    #
    #     select_galley = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value=f'//android.widget.FrameLayout[@content-desc="{image_name}"]'
    #     )
    #     assert select_galley.is_displayed()
    #     select_galley.click()
    #
    #     select_image = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.Button[@resource-id="com.google.android.providers.media.module:id/button_add"]'
    #     )
    #     assert select_image.is_displayed()
    #     select_image.click()
    #
    #     # close_galley= driver.find_element(
    #     #     by=AppiumBy.XPATH,
    #     #     value='//android.widget.ImageButton[@content-desc="Cancel"]'
    #     # )
    #     # assert close_galley.is_displayed()
    #     # close_galley.click()
    #
    #     send_image = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.view.View[@content-desc="send"]'
    #     )
    #     assert send_image.is_displayed()
    #     send_image.click()
    #
    # @it("select document and send to history")
    # def test_select_document_and_send_to_history(self, driver):
    #     attach_file_icon =  driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value= "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]"
    #     )
    #     assert attach_file_icon.is_displayed(), "file attach icon is find"
    #     attach_file_icon.click()
    #
    #     select_file_action = driver.find_element(
    #         by= AppiumBy.XPATH,
    #         value="//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]"
    #     )
    #     assert select_file_action.is_displayed(), "file Icon is displayed"
    #     select_file_action.click()
    #
    #     select_file_document = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value= '//android.widget.Button[@text="Documents"]'
    #     )
    #     assert select_file_document.is_displayed(), "documents is find in phone files tabs"
    #     select_file_document.click()
    #
    #     document_file = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.TextView[@resource-id="android:id/title" and @text="ISTQB- CTFL-dotin 11-PDF.PDF"]'
    #     )
    #     assert document_file.is_displayed(), 'pdf document is find'
    #     document_file.click()
    #
    #     send_document = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]'
    #     )
    #     assert send_document.is_displayed(), 'pdf is find'
    #     send_document.click()
    #
    # @it("select video and send to history")
    # def test_select_video_and_send_to_history(self, driver):
    #     attach_video_icon =  driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value= "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]"
    #     )
    #     assert attach_video_icon.is_displayed(), "file attach icon is find"
    #     attach_video_icon.click()
    #
    #     select_video_action = driver.find_element(
    #         by= AppiumBy.XPATH,
    #         value="//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]"
    #     )
    #     assert select_video_action.is_displayed(), "file Icon is displayed"
    #     select_video_action.click()
    #
    #     select_file_video = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value= '//android.widget.Button[@text="Videos"]'
    #     )
    #     assert select_file_video.is_displayed(), "video is find in phone files tabs"
    #     select_file_video.click()
    #
    #     video_name = 'Talk App New Features2 V2-MP4.MP4'
    #
    #     # Use UiScrollable to scroll until the video is found
    #     scrollable_video = 'new UiScrollable(new UiSelector().resourceId("com.google.android.documentsui:id/container_search_fragment")).scrollIntoView(new UiSelector().descriptionContains("{}"))'.format(video_name)
    #     driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scrollable_video)
    #
    #
    #     video_file = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value=f'//android.widget.TextView[@resource-id="android:id/title" and @text="{video_name}"]'
    #     )
    #     assert video_file.is_displayed(), 'video file is find'
    #     video_file.click()
    #
    #     send_video = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]'
    #     )
    #     assert send_video.is_displayed(), 'video is find'
    #     send_video.click()
    #
    # @it("send voice to history")
    # def test_send_voice_to_history(self,driver):
    #     click_mic = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.view.View[@content-desc="Mic"]'
    #     )
    #     assert click_mic.is_displayed(), 'mic icon is find'
    #     click_mic.click()
    #
    #     allow_mic_permission = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.TextView[@text="تایید"]'
    #     )
    #     assert allow_mic_permission.is_displayed() , 'permission is find'
    #     allow_mic_permission.click()
    #
    #     permission_allow_foreground  = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'
    #     )
    #     assert permission_allow_foreground.is_displayed() , 'permission_allow_foreground is find'
    #     permission_allow_foreground.click()
    #
    #     stop_voice = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.view.View[@content-desc="send"]'
    #     )
    #     assert stop_voice.is_displayed(), 'send_voice is find'
    #     time.sleep(10)
    #     stop_voice.click()
    #
    #     send_voice = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.view.View[@content-desc="send"]'
    #     )
    #     assert send_voice.is_displayed(), 'send_voice is find'
    #     send_voice.click()

    @it('back to history')
    def test_back_to_history(self,driver):
        back_button = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="Menu"]'
        )
        assert back_button.is_displayed(), 'back to history find'
        back_button.click()


    @it("select group thread")
    def test_select_group_thread(self, driver):

        group_name= 'گروه قدیم خودم😐😐😐'
        # Use UiScrollable to scroll until the group thread is found
        scrollable_thread_list = 'new UiScrollable(new UiSelector().resourceId("android:id/content")).scrollIntoView(new UiSelector().descriptionContains("{}"))'.format(group_name)
        # Execute scrolling command
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scrollable_thread_list)
        group_thread = driver.find_element(
            by=AppiumBy.XPATH,
            value=f'//android.widget.TextView[@text="{group_name}"]'
        )
        assert group_thread.is_displayed(), 'single thread group_name is find'
        # group_thread.click()













