import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        "appium:newCommandTimeout": 1200000,
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

@describe("create channel thread")
class TestCreateChannelThread:
    @it("click menu and create new channel")
    def test_click_menu_create_new_channel(self,driver):
        time.sleep(5)

        #click on menu
        toggle_menu = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="Toggle drawer"]'
        )
        assert toggle_menu.is_displayed(), 'toggle menu find'
        toggle_menu.click()

        #click on create new channel
        create_new_channel = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("ایجاد کانال جدید")'))
        )
        assert create_new_channel.is_displayed(),'create new channel find'
        create_new_channel.click()

        #click search participants icon
        search_participant_icon =  driver.find_element(
            by = AppiumBy.XPATH,
            value = '//android.view.View[@content-desc="Search"]'
        )
        assert search_participant_icon.is_displayed(), 'search icon find '
        search_participant_icon.click()

        #search and select first participant
        search_input = driver.find_element(
            by = AppiumBy.XPATH,
            value = '//android.widget.EditText'
        )
        assert search_input.is_displayed(), 'search input find'
        search_input.send_keys('الهام test')

        #click on expected search result
        time.sleep(2)
        select_first_participant = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("الهام test")'))
        )
        assert select_first_participant.is_displayed(), ' find الهام test'
        time.sleep(2)
        select_first_participant.click()

        #clear search or second participant
        clear_search_input = driver.find_element(
            by = AppiumBy.XPATH,
            value = '//android.view.View[@content-desc="Search"]'
        )
        assert clear_search_input.is_displayed(),'clear search find'
        clear_search_input.click()

        #search and select second participant
        time.sleep(2)
        search_input = driver.find_element(
            by = AppiumBy.XPATH,
            value = '//android.widget.EditText'
        )
        assert search_input.is_displayed(), 'search input find'
        search_input.send_keys('آزیتا تست')

        #click on expected search result
        # select_second_participant = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("آزیتا تست")'))
        # )
        select_second_participant = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//android.widget.TextView[@text="آزیتا تست"]'
        )
        assert select_second_participant.is_displayed(), ' find آزیتا تست'
        select_second_participant.click()
        time.sleep(2)
        #click on next to go for define name for group

        next_icon = driver.find_element(
            by = AppiumBy.XPATH,
            value = '//android.widget.TextView[@text="بعدی"]'
        )
        assert next_icon.is_displayed(),'next icon find'
        time.sleep(2)
        next_icon.click()

        #define name for group
        channel_name = 'کانال تستی اندروید برای اتومیشن'
        channel_name_input = driver.find_element(
            by = AppiumBy.XPATH,
            value = '//android.widget.EditText'
        )
        assert channel_name_input.is_displayed(),'group name input find'
        channel_name_input.click()
        channel_name_input.send_keys(channel_name)

        #click image icon
        time.sleep(2)
        image_icon = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View'
        )
        assert image_icon.is_displayed(),'image icon find'
        image_icon.click()
        #scroll and select an specific image
        # image_name = "Photo taken on 29 Jan 2025, 11:08:23 pm"
        #
        # # Use UiScrollable to scroll until the image is found
        # scrollable_gallery = '''
        #     new UiScrollable(new UiSelector().resourceId("com.google.android.providers.media.module:id/bottom_sheet"))
        #         .setAsVerticalList()
        #         .scrollToBeginning(10)
        #         .scrollBackward()
        #         .scrollIntoView(new UiSelector().descriptionContains("{}"))
        #     '''.format(image_name)
        #
        # # Execute scrolling command
        # driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scrollable_gallery)

        #select first image in gallery
        select_image = driver.find_element(
            by=AppiumBy.XPATH,
            value='(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]'
        )
        assert select_image.is_displayed(),'select image find'
        time.sleep(2)
        select_image.click()

        #confirm selected image
        confirm_image = driver.find_element(
            by=AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]'
        )
        assert confirm_image.is_displayed(),'confirm image find'
        confirm_image.click()

        #click on created group button and jump to history
        create_channel_button =  driver.find_element(
            by = AppiumBy.XPATH,
            value = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[4]'
        )
        assert create_channel_button.is_displayed(),'create group find'
        create_channel_button.click()

        #send simple message to history
        click_input = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.EditText[@text="اینجا بنویسید…"]')
        assert click_input.is_displayed(), "input for typing message is find a"
        click_input.click()
        click_input.send_keys("این یک پیام تستی برای اتومیشن اندروید است ")
        send_text_message = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="send"]'
        )
        assert send_text_message.is_displayed(), "send icon is find"
        send_text_message.click()
        time.sleep(3)

        #close keyboard
        close_keyboard = driver.find_element(
            by= AppiumBy.XPATH,
            value='//android.view.View[@content-desc="Menu"]'
        )
        assert close_keyboard.is_displayed(),'close_keyboard find'
        close_keyboard.click()

        #back from new history to thread list
        back_to_history = driver.find_element(
            by= AppiumBy.XPATH,
            value='//android.view.View[@content-desc="Menu"]'
        )
        assert back_to_history.is_displayed(),'back to history find'
        time.sleep(3)
        back_to_history.click()

        #check the new group is displaying in thread list
        time.sleep(3)
        scrollable_container = driver.find_element(
            by=AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]')
        channel_thread_name= 'کانال تستی اندروید برای اتومیشن'
        # Scroll until the element is found
        max_attempts = 10
        attempts = 0

        while attempts < max_attempts:
            try:
                # Find the element by text using XPath
                element = driver.find_element(
                    by=AppiumBy.XPATH,
                    value=f'//*[@text="{channel_thread_name}"]')
                print("Element found!")
                element.click()  # Perform actions on the found element
                break
            except:
                # Scroll down if the element is not found
                size = scrollable_container.size
                location = scrollable_container.location
                start_x = location['x'] + size['width'] / 2
                start_y = location['y'] + size['height'] * 0.8  # Start from 80% of the container height
                end_y = location['y'] + size['height'] * 0.2  # End at 20% of the container height
                driver.swipe(start_x, start_y, start_x, end_y, 500)
                print("Scrolling...")
                attempts += 1

        if attempts == max_attempts:
            print("Element not found after maximum scroll attempts.")
