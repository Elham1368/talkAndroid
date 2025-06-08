import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import os

# Define the APK path
apk_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', 'talk-app-v2.5.4.3.13.apk')
print(apk_path)
# Define capabilities
capabilities = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "deviceName": "emulator-5554",  # نام دستگاه شبیه‌ساز یا فیزیکی
    "appium:appPackage": "ir.dotin.talk",  # نام بسته اپلیکیشن که می‌خواهید حذف کنید
    "appium:appActivity": "ir.dotin.talk.presentation.login.ui.pkce.WebLoginActivity",  # نام activity اپلیکیشن
    "appium:newCommandTimeout":120000,
    "app":apk_path,
}

appium_server_url = 'http://127.0.0.1:4723'  # آدرس سرور اپیوم
driver = None


try:
    print("Starting Appium session...")
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    print("App installed successfully on the emulator!")

    # Perform any additional actions here, e.g., navigating in the app
    print("Waiting for interaction with the app...")
    driver.install_app(apk_path)
    # driver.launch_app()  # Launch the installed app

finally:
    # Quit the driver after operations are complete
    if driver:
        print("Closing the session.")
        driver.quit()
    else:
        print("Driver was not initialized. No session to close.")