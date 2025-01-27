from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import pytest
import os

import subprocess
import re
import time


# Define the APK path
# apk_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', 'talk-app-v2.6.1.2.2.apk')
# print(apk_path)
# Define capabilities
capabilities = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "deviceName": "Galaxy A52",
    "appium:appPackage": "ir.dotin.talk",
    "appium:appActivity": "ir.dotin.talk.presentation.main.MainActivity",
    "appium:newCommandTimeout":120000,
    # "appium:noReset": True,

    # "app":apk_path,
}

appium_server_url = 'http://127.0.0.1:4723'  #Appium Server Address
driver = None
class TestAppium:
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    # driver.install_app(apk_path)
    driver.implicitly_wait(15)
    phone_input = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText')
    # phone_input.click()

    phone_number = "9157069965"  # enter your phone number
    phone_input.send_keys(phone_number)
    print(" enter phone number:"+ phone_number)
    continue_button = driver.find_element(by=AppiumBy.XPATH, value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]')
    continue_button.click()
    allow_button= driver.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[@resource-id="com.google.android.gms:id/positive_button"]')
    allow_button.click()
    driver.implicitly_wait(15)
    permission_talk_notif = driver.find_element(by=AppiumBy.XPATH , value='//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]')
    permission_talk_notif.click()
    permission_notif_system = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
    permission_notif_system.click()

    single_thread = driver.find_element(by=AppiumBy.XPATH, value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]')
    single_thread.click()
    focus_input = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="اینجا بنویسید…"]')
    focus_input.click()
    focus_input.send_keys("این یک پیام تستی است ")
    send_text_message = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="send"]')
    send_text_message.click()