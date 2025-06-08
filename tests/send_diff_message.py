import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from utils.utils import find_element, click_element, send_keys_to_element, scroll_until_element_found,actionBuilder
# درا ولین فرصت استفاده از توابع  utilsبرای تمیزتر شدن اسکریپت
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
@describe("Send Message to single thread")
class TestSingleThreadMessaging:
    @it("select single thread")
    def test_select_single_thread(self, driver):
        single_thread = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.TextView[@text="الهام test"]')
        assert single_thread.is_displayed(), "single thread الهام test is find"
        single_thread.click()

    @it("type and send simple text history")
    def test_type_and_send_simple_text_history(self, driver):
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

    @it("select image and send to history")
    def test_select_image_and_send_to_history(self, driver):
        click_attach_icon = driver.find_element(
            by=AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]'
        )
        assert click_attach_icon.is_displayed(), "attach Icon is find"
        click_attach_icon.click()
        select_gallery = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.TextView[@text="گالری"]'
        )
        assert select_gallery.is_displayed(), "gallery is find"
        select_gallery.click()

        # permission_gallery = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]'
        # )
        # assert permission_gallery.is_displayed()
        # permission_gallery.click()

        allow_all_permission = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_all_button"]'
        )
        assert allow_all_permission.is_displayed()
        allow_all_permission.click()

        select_album = driver.find_element(
            by= AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.widget.Button'
        )
        assert select_album.is_displayed()
        select_album.click()

        select_favorites = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//android.widget.TextView[@text="Favorites"]'
        )
        assert select_favorites.is_displayed()
        select_favorites.click()

        # image_name = "Photo taken on 27 Feb 2024 09:52"

        # Use UiScrollable to scroll until the image is found
        # scrollable_gallery = 'new UiScrollable(new UiSelector().resourceId("com.google.android.providers.media.module:id/bottom_sheet")).scrollIntoView(new UiSelector().descriptionContains("{}"))'.format(image_name)
        # scrollable_gallery = 'new UiScrollable(new UiSelector().className("android.view.View").instance(8)).scrollIntoView(new UiSelector().descriptionContains("{}"))'.format(image_name)
        time.sleep(3)
        # مرجع به کانتینر اسکرول‌پذیر (بدون اشاره مستقیم به فرزندان)
        scrollable_container = driver.find_element(
            by=AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[4]'
        )

        image_name = "Photo taken on 27 Feb 2024 09:52"
        max_attempts = 5
        attempts = 0
        found = False

        while attempts < max_attempts and not found:
            try:
                # جستجوی مستقیم برای عنصر مورد نظر در سطح فرزند دوم (child of child)
                element = driver.find_element(
                    by=AppiumBy.XPATH,
                    value=f'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[@content-desc="{image_name}"]'
                )
                print("Element found!")
                element.click()
                found = True  # خروج از حلقه پس از یافتن و کلیک
            except:
                # اسکرول در صورت عدم یافتن عنصر
                size = scrollable_container.size
                location = scrollable_container.location
                start_x = location['x'] + size['width'] / 2
                start_y = location['y'] + size['height'] * 0.5
                end_y = location['y'] + size['height'] * 0.2
                driver.swipe(start_x, start_y, start_x, end_y, 420)
                print("Scrolling...")
                attempts += 1

        if found:
            print("عکس مورد نظر با موفقیت انتخاب شد.")
        else:
            print("عکس پس از تلاش‌های مجاز یافت نشد.")

        # Execute scrolling command
        # driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scrollable_gallery)
        #
        # select_galley = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value=f'//android.widget.FrameLayout[@content-desc="{image_name}"]'
        # )
        # assert select_galley.is_displayed()
        # select_galley.click()
        #
        # select_image = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='//android.widget.Button[@resource-id="com.google.android.providers.media.module:id/button_add"]'
        # )
        # assert select_image.is_displayed()
        # select_image.click()

        # close_galley= driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='//android.widget.ImageButton[@content-desc="Cancel"]'
        # )
        # assert close_galley.is_displayed()
        # close_galley.click()

        done_button = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.TextView[@text="Done"]'
        )
        assert done_button.is_displayed()
        done_button.click()

        #confrim image cropper
        confirm_image = driver.find_element(
            by= AppiumBy.XPATH,
            value= '//android.widget.TextView[@text="تایید"]'
        )
        assert confirm_image.is_displayed()
        confirm_image.click()

        send_image = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="send"]'
        )
        assert send_image.is_displayed()
        send_image.click()

    @it("select document and send to history")
    def test_select_document_and_send_to_history(self, driver):
        attach_file_icon =  driver.find_element(
            by=AppiumBy.XPATH,
            value= "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]"
        )
        assert attach_file_icon.is_displayed(), "file attach icon is find"
        attach_file_icon.click()

        select_file_action = driver.find_element(
            by= AppiumBy.XPATH,
            value="//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]"
        )
        assert select_file_action.is_displayed(), "file Icon is displayed"
        select_file_action.click()

        select_file_document = driver.find_element(
            by=AppiumBy.XPATH,
            value= '//android.widget.Button[@text="Documents"]'
        )
        assert select_file_document.is_displayed(), "documents is find in phone files tabs"
        select_file_document.click()

        document_name = "آزمون istqb-PDF.PDF"

        scrollable_document = 'new UiScrollable(new UiSelector().resourceId("com.google.android.documentsui:id/drawer_layout")).scrollIntoView(new UiSelector().descriptionContains("{}"))'.format(document_name)
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scrollable_document)

        pdf_file = driver.find_element(
            by=AppiumBy.XPATH,
            value=f'//android.widget.TextView[@resource-id="android:id/title" and @text="{document_name}"]'
        )

        pdf_file.click()

        send_document = driver.find_element(
            by=AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]'
        )
        assert send_document.is_displayed(), 'pdf is find'
        send_document.click()

    @it("select video and send to history")
    def test_select_video_and_send_to_history(self, driver):
        attach_video_icon =  driver.find_element(
            by=AppiumBy.XPATH,
            value= "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]"
        )
        assert attach_video_icon.is_displayed(), "file attach icon is find"
        attach_video_icon.click()

        select_video_action = driver.find_element(
            by= AppiumBy.XPATH,
            value="//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]"
        )
        assert select_video_action.is_displayed(), "file Icon is displayed"
        select_video_action.click()

        select_file_video = driver.find_element(
            by=AppiumBy.XPATH,
            value= '//android.widget.Button[@text="Videos"]'
        )
        assert select_file_video.is_displayed(), "video is find in phone files tabs"
        select_file_video.click()

        video_name = 'نوروز 1404-MP4.MP4'

        # Use UiScrollable to scroll until the video is found
        scrollable_video = 'new UiScrollable(new UiSelector().resourceId("com.google.android.documentsui:id/dir_list")).scrollIntoView(new UiSelector().descriptionContains("{}"))'.format(video_name)
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scrollable_video)


        video_file = driver.find_element(
            by=AppiumBy.XPATH,
            value=f'//android.widget.TextView[@resource-id="android:id/title" and @text="{video_name}"]'
        )
        assert video_file.is_displayed(), 'video file is find'
        video_file.click()

        send_video = driver.find_element(
            by=AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]'
        )
        assert send_video.is_displayed(), 'video is find'
        send_video.click()

    @it("send voice to history")
    def test_send_voice_to_history(self,driver):
        click_mic = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="Mic"]'
        )
        assert click_mic.is_displayed(), 'mic icon is find'
        click_mic.click()
        try:
            allow_mic_permission = driver.find_element(
                by=AppiumBy.XPATH,
                value='//android.widget.TextView[@text="تایید"]'
            )
            if allow_mic_permission.is_displayed():
                assert allow_mic_permission.is_displayed() , 'permission is find'
                allow_mic_permission.click()
                print("✅ Permission 'Allow All' clicked.")
            else:
                print("⚠️ Permission dialog is not displayed.")
        except NoSuchElementException:
            print("❌ No permission dialog found, skipping...")

        permission_allow_foreground  = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'
        )
        assert permission_allow_foreground.is_displayed() , 'permission_allow_foreground is find'
        permission_allow_foreground.click()

        stop_voice = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="send"]'
        )
        assert stop_voice.is_displayed(), 'send_voice is find'
        time.sleep(10)
        stop_voice.click()

        send_voice = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="send"]'
        )
        assert send_voice.is_displayed(), 'send_voice is find'
        send_voice.click()

    @it('back to thread_list')
    def test_back_to_list(self,driver):
        back_button = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="Menu"]'
        )
        assert back_button.is_displayed(), 'back to history find'
        back_button.click()

@describe("Send Message to group thread")
class TestGroupThreadMessaging:

    @it("select group thread")
    def test_select_group_thread(self, driver):

        scrollable_container = driver.find_element(
            by=AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]')
        group_name= 'گروه قدیم خودم'
        # Scroll until the element is found
        max_attempts = 10
        attempts = 0

        while attempts < max_attempts:
            try:
                # Find the element by text using XPath
                element = driver.find_element( by=AppiumBy.XPATH,
                                           value=f'//*[@text="{group_name}"]')
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

    @it("type and send simple text history")
    def test_type_and_send_simple_text_history(self, driver):
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

    @it("select image and send to history")
    def test_select_image_and_send_to_history(self, driver):
        # click_attach_icon = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]'
        # )
        # assert click_attach_icon.is_displayed(), "attach Icon is find"
        # click_attach_icon.click()
        # select_gallery = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='//android.widget.TextView[@text="گالری"]'
        # )
        # assert select_gallery.is_displayed(), "gallery is find"
        # select_gallery.click()
        #
        # # permission_gallery = driver.find_element(
        # #     by=AppiumBy.XPATH,
        # #     value='//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]'
        # # )
        # # assert permission_gallery.is_displayed()
        # # permission_gallery.click()
        # #
        # # allow_permission = driver.find_element(
        # #     by=AppiumBy.XPATH,
        # #     value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_all_button"]'
        # # )
        # # assert allow_permission.is_displayed()
        # # allow_permission.click()
        #
        # image_name = "Photo taken on 29 Jan 2025, 11:08:23 pm"
        #
        # # Use UiScrollable to scroll until the image is found
        # scrollable_gallery = 'new UiScrollable(new UiSelector().resourceId("com.google.android.providers.media.module:id/bottom_sheet")).scrollIntoView(new UiSelector().descriptionContains("{}"))'.format(image_name)
        #
        # # Execute scrolling command
        # driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scrollable_gallery)
        #
        # select_galley = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value=f'//android.widget.FrameLayout[@content-desc="{image_name}"]'
        # )
        # assert select_galley.is_displayed()
        # select_galley.click()
        #
        # select_image = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='//android.widget.Button[@resource-id="com.google.android.providers.media.module:id/button_add"]'
        # )
        # assert select_image.is_displayed()
        # select_image.click()
        #
        # # close_galley= driver.find_element(
        # #     by=AppiumBy.XPATH,
        # #     value='//android.widget.ImageButton[@content-desc="Cancel"]'
        # # )
        # # assert close_galley.is_displayed()
        # # close_galley.click()
        #
        # send_image = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='//android.view.View[@content-desc="send"]'
        # )
        # assert send_image.is_displayed()
        # send_image.click()

        click_attach_icon = driver.find_element(
            by=AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]'
        )
        assert click_attach_icon.is_displayed(), "attach Icon is find"
        click_attach_icon.click()
        select_gallery = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.TextView[@text="گالری"]'
        )
        assert select_gallery.is_displayed(), "gallery is find"
        select_gallery.click()

        try:
            allow_all_permission = driver.find_element(
                by=AppiumBy.XPATH,
                value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_all_button"]'
            )
            if allow_all_permission.is_displayed():
                allow_all_permission.click()
                print("✅ Permission 'Allow All' clicked.")
            else:
                print("⚠️ Permission dialog is not displayed.")
        except NoSuchElementException:
            print("❌ No permission dialog found, skipping...")

        select_album = driver.find_element(
            by= AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.widget.Button'
        )
        assert select_album.is_displayed()
        select_album.click()

        select_favorites = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//android.widget.TextView[@text="Favorites"]'
        )
        assert select_favorites.is_displayed()
        select_favorites.click()

        time.sleep(3)
        scrollable_container = driver.find_element(
            by=AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[4]'
        )

        image_name = "Photo taken on 27 Feb 2024 09:52"
        max_attempts = 5
        attempts = 0
        found = False

        while attempts < max_attempts and not found:
            try:
                # جستجوی مستقیم برای عنصر مورد نظر در سطح فرزند دوم (child of child)
                element = driver.find_element(
                    by=AppiumBy.XPATH,
                    value=f'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[@content-desc="{image_name}"]'
                )
                print("Element found!")
                element.click()
                found = True  # خروج از حلقه پس از یافتن و کلیک
            except:
                # اسکرول در صورت عدم یافتن عنصر
                size = scrollable_container.size
                location = scrollable_container.location
                start_x = location['x'] + size['width'] / 2
                start_y = location['y'] + size['height'] * 0.5
                end_y = location['y'] + size['height'] * 0.2
                driver.swipe(start_x, start_y, start_x, end_y, 420)
                print("Scrolling...")
                attempts += 1

        if found:
            print("عکس مورد نظر با موفقیت انتخاب شد.")
        else:
            print("عکس پس از تلاش‌های مجاز یافت نشد.")

        done_button = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.TextView[@text="Done"]'
        )
        assert done_button.is_displayed()
        done_button.click()

        #confrim image cropper
        confirm_image = driver.find_element(
            by= AppiumBy.XPATH,
            value= '//android.widget.TextView[@text="تایید"]'
        )
        assert confirm_image.is_displayed()
        confirm_image.click()

        send_image = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="send"]'
        )
        assert send_image.is_displayed()
        send_image.click()

    @it("select document and send to history")
    def test_select_document_and_send_to_history(self, driver):
        attach_file_icon =  driver.find_element(
            by=AppiumBy.XPATH,
            value= "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]"
        )
        assert attach_file_icon.is_displayed(), "file attach icon is find"
        attach_file_icon.click()

        select_file_action = driver.find_element(
            by= AppiumBy.XPATH,
            value='//android.widget.TextView[@text="فایل"]'
        )
        assert select_file_action.is_displayed(), "file Icon is displayed"
        select_file_action.click()

        select_file_document = driver.find_element(
            by=AppiumBy.XPATH,
            value= '//android.widget.Button[@text="Documents"]'
        )
        assert select_file_document.is_displayed(), "documents is find in phone files tabs"
        select_file_document.click()

        document_name = "آزمون istqb-PDF.PDF"

        scrollable_document = 'new UiScrollable(new UiSelector().resourceId("com.google.android.documentsui:id/drawer_layout")).scrollIntoView(new UiSelector().descriptionContains("{}"))'.format(document_name)
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scrollable_document)

        pdf_file = driver.find_element(
            by=AppiumBy.XPATH,
            value=f'//android.widget.TextView[@resource-id="android:id/title" and @text="{document_name}"]'
        )

        pdf_file.click()

        send_document = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="send"]'
        )
        assert send_document.is_displayed(), 'pdf is find'
        send_document.click()

    @it("select video and send to history")
    def test_select_video_and_send_to_history(self, driver):
        attach_video_icon =  driver.find_element(
            by=AppiumBy.XPATH,
            value= "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]"
        )
        assert attach_video_icon.is_displayed(), "file attach icon is find"
        attach_video_icon.click()

        select_video_action = driver.find_element(
            by= AppiumBy.XPATH,
            value='//android.widget.TextView[@text="فایل"]'
        )
        assert select_video_action.is_displayed(), "file Icon is displayed"
        select_video_action.click()

        select_file_video = driver.find_element(
            by=AppiumBy.XPATH,
            value= '//android.widget.Button[@text="Videos"]'
        )
        assert select_file_video.is_displayed(), "video is find in phone files tabs"
        select_file_video.click()

        video_name = 'نوروز 1404-MP4.MP4'

        # Use UiScrollable to scroll until the video is found
        scrollable_video = 'new UiScrollable(new UiSelector().resourceId("com.google.android.documentsui:id/dir_list")).scrollIntoView(new UiSelector().descriptionContains("{}"))'.format(video_name)
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scrollable_video)


        video_file = driver.find_element(
            by=AppiumBy.XPATH,
            value=f'//android.widget.TextView[@resource-id="android:id/title" and @text="{video_name}"]'
        )
        assert video_file.is_displayed(), 'video file is find'
        video_file.click()

        send_video = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="send"]'
        )
        assert send_video.is_displayed(), 'video is find'
        send_video.click()

    @it("send voice to history")
    def test_send_voice_to_history(self,driver):
        click_mic = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="Mic"]'
        )
        assert click_mic.is_displayed(), 'mic icon is find'
        click_mic.click()

        # allow_mic_permission = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='//android.widget.TextView[@text="تایید"]'
        # )
        # assert allow_mic_permission.is_displayed() , 'permission is find'
        # allow_mic_permission.click()
        #
        # permission_allow_foreground  = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'
        # )
        # assert permission_allow_foreground.is_displayed() , 'permission_allow_foreground is find'
        # permission_allow_foreground.click()

        stop_voice = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="send"]'
        )
        assert stop_voice.is_displayed(), 'send_voice is find'
        time.sleep(5)
        stop_voice.click()

        send_voice = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="send"]'
        )
        assert send_voice.is_displayed(), 'send_voice is find'
        send_voice.click()

    @it('back to history')
    def test_back_to_history(self,driver):
        back_button = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="Menu"]'
        )
        assert back_button.is_displayed(), 'back to history find'
        back_button.click()


















