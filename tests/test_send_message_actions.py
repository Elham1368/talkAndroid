# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from appium.webdriver.common.appiumby import AppiumBy
# from utils.utils import find_element, click_element, send_keys_to_element, scroll_until_element_found,actionBuilder
# import subprocess
# import pytest
# import logging
# import time
# # Setup once at the top of your test or in conftest.py
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
# import os
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.actions import interaction
# from selenium.common.exceptions import NoSuchElementException
# from conftests import login, driver
#
# # @pytest.mark.usefixtures("driver","login")
# # Custom describe and it functions
# def describe(description):
#     def decorator(cls):
#         cls.__description__ = description
#         return cls
#     return decorator
#
# def it(description):
#     def decorator(func):
#         func.__it_description__ = description
#         return func
#     return decorator
#
# # @pytest.fixture(scope="session", autouse=True)
# # def run_prerequisite_tests(): برای اجرای یک فایل قبل از اجرای این فایل به عنوان فایل پیش نیاز
# #     # مسیر کامل فایل تستی
# #     file_path = os.path.abspath('tests/send_diff_message.py')
# #     print("Test file path:", file_path)
# #
# #     result = subprocess.run(['pytest', file_path], capture_output=True, text=True)
# #
# #     # چاپ جزئیات خروجی
# #     print("Exit Code:", result.returncode)
# #     print("STDOUT:", result.stdout)
# #     print("STDERR:", result.stderr)
# #
# #     if result.returncode != 0:
# #         print(f"Error: Prerequisite tests failed with exit code {result.returncode}")
# #         if result.stderr:
# #             print("Error Details:", result.stderr)
# #         else:
# #             print("No additional error details available.", result.stderr)
# #         raise Exception("Prerequisite tests failed!", result)
#
# @pytest.mark.usefixtures("driver","login") # اجرای لاگین قبل از هر تست
# class TestMessageActions:
#     @it("select single thread")
#     def test_select_single_thread(self, driver):
#         # single_thread = driver.find_element(
#         #     by=AppiumBy.XPATH,
#         #     value='//android.widget.TextView[@text="الهام test"]')
#         # assert single_thread.is_displayed(), "single thread الهام test is find"
#         # single_thread.click()
#         click_element(self.driver,AppiumBy.XPATH,'//android.widget.TextView[@text="الهام test"]')
#     # @it("type and send simple text history")
#     # def test_type_and_send_simple_text_history(self, driver):
#     #     click_input = click_element(driver, AppiumBy.XPATH,'//android.widget.EditText[@text="اینجا بنویسید…"]')
#     #     click_input.send_keys("این یک پیام تستی برای اتومیشن اندروید است ")
#     #     #send message to history
#     #     click_element(driver, AppiumBy.XPATH,'//android.view.View[@content-desc="send"]')
#     #
#     # @it("action on single message")
#     # def test_actions_on_single_thread_message(self, driver):
#     #     print("hellllllo")
#     #     message_text = "این یک پیام تستی برای اتومیشن اندروید است"
#     #     #scroll until find message and click to open contex menu
#     #     scrollable_document = 'new UiScrollable(new UiSelector().className("android.view.View").instance(3)).scrollIntoView(new UiSelector().descriptionContains("{}"))'.format(message_text)
#     #     driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scrollable_document)
#     #     click_element(driver, AppiumBy.XPATH, f'(//android.widget.TextView[@text={message_text}])')

import pytest
from conftests import login, driver
from modules.message_actios_module import SendMessageActions

@pytest.mark.usefixtures("driver","login") # اجرای لاگین قبل از هر تست
class TestMessageActions:
    def test_actions_send_messages(self, driver):
        send_message_actions = SendMessageActions(driver)
        send_message_actions.open_single_thread("الهام test")
        send_message_actions.find_child_text_with_scroll("این یک پیام تستی برای اتومیشن اندروید است")
        # send_message_actions.open_context_menu()
        send_message_actions.edit("ویرایش",'این یک پیام تستی برای اتومیشن اندروید است',"پیام برای ویرایش پیام اصلی در اتومیشن اندروید هست")
        send_message_actions.delete_for_me("پیام برای ویرایش پیام اصلی در اتومیشن اندروید هست",'حذف','برای من و دیگران','فقط برای من','تایید')
        # send_message_actions.forward()
        # send_message_actions.copy()
        # send_message_actions.select()