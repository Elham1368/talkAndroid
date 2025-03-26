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
        "appium:newCommandTimeout": 600000,
        "appium:noReset": True,

        # "app":apk_path,
    }
    appium_server_url = 'http://127.0.0.1:4723'  #Appium Server Address
    driver = None

    driver = webdriver.Remote(appium_server_url,
                              options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver


# Test cases
# @describe("Login Feature")
# class TestLogin:
#     @it("should allow the user to write phone number to mobile input element")
#     def test_write_phone_number(self, driver):
#         driver.implicitly_wait(15)
#         phone_input = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText')
#         assert phone_input.is_displayed(), "Phone input element is displayed"
#
#         phone_number = "9157069965"  # Example phone number
#         phone_input.send_keys(phone_number)
#     @it("should allow the user to send phone number")
#     def test_send_phone_number(self, driver):
#         driver.implicitly_wait(15)
#
#         # Click the "Continue" button
#         continue_button = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]'
#         )
#         assert continue_button.is_displayed(), "Continue button is  displayed"
#         continue_button.click()
#     @it("allow permission for autofill")
#     def test_allow_permission_autofill(self, driver):
#         # Click the "Allow" button for permissions
#         allow_button = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//android.widget.Button[@resource-id="com.google.android.gms:id/positive_button"]'
#         )
#         assert allow_button.is_displayed(), "Allow button is displayed"
#         allow_button.click()
#     @it("allow permission for notification")
#     def test_allow_permission_notification(self, driver):
#         driver.implicitly_wait(15)
#         permission_talk_notif = driver.find_element(
#             by=AppiumBy.XPATH ,
#             value='//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]')
#         assert permission_talk_notif.is_displayed(), "permission talk notif is displayed"
#         permission_talk_notif.click()
#         permission_notif_system = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
#         assert permission_notif_system.is_displayed(), "permission notif system is displayed"
#         permission_notif_system.click()

# @describe("create single thread")
# class TestCreateSingleThread:
#     @it("open menu and add contact")
#     def test_open_menu_add_contact(self, driver):
#         #click on menu
#         toggle_menu = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//android.view.View[@content-desc="Toggle drawer"]'
#         )
#         assert toggle_menu.is_displayed(), 'toggle menu find'
#         toggle_menu.click()
#         #click on add contact
#         add_contact=driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//android.widget.TextView[@text="افزودن مخاطب جدید"]'
#         )
#         assert add_contact.is_displayed(),'add contact find'
#         add_contact.click()
#         #check add contact modal is opened
#         add_contact_modal = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View/android.view.View[2]'
#
#         )
#         assert add_contact_modal.is_displayed(),'add contact modal find'
#     @it("create contact")
#     def test_create_contact(self, driver):
#         name = 'elham'
#         family = 'تست 2'
#         phone_number = '09371521106'
#         #fill contact name
#         contact_name = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]'
#         )
#         assert contact_name.is_displayed(), 'contact name find'
#         contact_name.click()
#         contact_name.send_keys(name)
#         # #fill contact family
#         contact_family = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//android.widget.ScrollView/android.widget.EditText[2]'
#         )
#         assert contact_family.is_displayed(),'contact family find'
#         contact_family.click()
#         contact_family.send_keys(family)
#         #fill contact mobile number
#         contact_phone = driver.find_element(
#             by=AppiumBy.XPATH,
#             value= '//android.widget.ScrollView/android.widget.EditText[3]'
#         )
#         assert contact_phone.is_displayed()
#         contact_phone.send_keys(phone_number)
#         #click on add contact افزودن
#         add_button = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//android.widget.TextView[@text="افزودن"]'
#         )
#         assert add_button.is_displayed(),'add button find'
#         add_button.click()
#     @it("check contact is added or not")
#     def test_check_contact_add(self,driver):
#         time.sleep(5)
#         name = 'elham '
#         family = 'تست 2'
#         #click on menu
#         toggle_menu = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//android.view.View[@content-desc="Toggle drawer"]'
#         )
#         assert toggle_menu.is_displayed(), 'toggle menu find'
#         toggle_menu.click()
#
#         #click contacts list
#         time.sleep(5)
#         contacts_list = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//android.widget.TextView[@text="مخاطبین"]'
#         )
#         assert contacts_list.is_displayed(),'contact list find'
#         contacts_list.click()
#
#         #click search icon
#         search_icon = driver.find_element(
#             by=AppiumBy.XPATH,
#             value= '//android.view.View[@content-desc="Search"]'
#         )
#         assert search_icon.is_displayed(),'searchIcon find'
#         search_icon.click()
#
#         #write the name added to list
#         search_input = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//android.widget.EditText'
#         )
#         assert search_input.is_displayed(),'search input find'
#         search_input.send_keys(name,family)
#         #check the result name and family is equal to the contact added to list
#         contact_result = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//android.widget.TextView[@text="elham تست 2"]'
#         )
#         assert contact_result.is_displayed(),'new contact find'
#         #get total result as parent and find the expected result as children on it
#     @it("create history with contact")
#     def test_create_history_contact(self,driver):
#         time.sleep(5)
#         #click on contact result
#         contact_result = driver.find_element(
#             by=AppiumBy.XPATH,
#             value= '//android.widget.TextView[@text="elham تست 2"]'
#         )
#         contact_result.click()
#
#         #send a simple message to history and create thread
#         click_input = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//android.widget.EditText[@text="اینجا بنویسید…"]')
#         assert click_input.is_displayed(), "input for typing message is find a"
#         click_input.click()
#         click_input.send_keys("این یک پیام تستی برای اتومیشن اندروید است ")
#         send_text_message = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//android.view.View[@content-desc="send"]'
#         )
#         assert send_text_message.is_displayed(), "send icon is find"
#         time.sleep(3)
#         send_text_message.click()
#     @it("check single thread is created")
#     def test_check_single_thread_is_created(self,driver):
#         #back to thread list
#         from_history_to_search= driver.find_element(
#             by=AppiumBy.XPATH,
#             value= '//android.view.View[@content-desc="Menu"]'
#         )
#         from_history_to_search.click()
#         from_search_to_contact_list = driver.find_element(
#             by=AppiumBy.XPATH,
#             value= '//android.view.View[@content-desc="Menu"]'
#         )
#         from_search_to_contact_list.click()
#         from_contact_to_thread_list = driver.find_element(
#             by=AppiumBy.XPATH,
#             value= '//android.view.View[@content-desc="Menu"]'
#         )
#         from_contact_to_thread_list.click()
#
#         #check the new single thread is exist in list or not
#         scrollable_container = driver.find_element(
#             by=AppiumBy.XPATH,
#             value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]')
#         single_thread_name= 'elham تست 2'
#         # Scroll until the element is found
#         max_attempts = 10
#         attempts = 0
#
#         while attempts < max_attempts:
#             try:
#                 # Find the element by text using XPath
#                 element = driver.find_element(
#                     by=AppiumBy.XPATH,
#                     value=f'//*[@text="{single_thread_name}"]')
#                 print("Element found!")
#                 element.click()  # Perform actions on the found element
#                 break
#             except:
#                 # Scroll down if the element is not found
#                 size = scrollable_container.size
#                 location = scrollable_container.location
#                 start_x = location['x'] + size['width'] / 2
#                 start_y = location['y'] + size['height'] * 0.8  # Start from 80% of the container height
#                 end_y = location['y'] + size['height'] * 0.2  # End at 20% of the container height
#                 driver.swipe(start_x, start_y, start_x, end_y, 500)
#                 print("Scrolling...")
#                 attempts += 1
#
#         if attempts == max_attempts:
#             print("Element not found after maximum scroll attempts.")
#     @it("delete contact and history")
#     def test_delete_contact_history(self,driver):
#         #click header for opening thread info
#         history_header = driver.find_element(
#             by = AppiumBy.XPATH,
#             value= '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]'
#         )
#         assert history_header.is_displayed(),'history header find'
#         history_header.click()
#
#         #delete contact by click on delete icon
#         delete_contact = driver.find_element(
#             by = AppiumBy.XPATH,
#             value= '//android.view.View[@content-desc="Delete"]'
#         )
#         assert delete_contact.is_displayed(),'delete contact icon find'
#         delete_contact.click()
#
#         confirm_delete_contact = driver.find_element(
#             by = AppiumBy.XPATH,
#             value = '//android.widget.TextView[@text="حذف"]'
#         )
#         assert confirm_delete_contact.is_displayed(),'confirm delete dialog find'
#         confirm_delete_contact.click()
#
#         #delete chat by click on ... and delete thread
#         click_more = driver.find_element(
#             by = AppiumBy.XPATH,
#             value = '//android.widget.ImageView[@content-desc="Cam"]'
#         )
#         assert click_more.is_displayed(),'... icon find'
#         click_more.click()
#
#         #select delete chat in ...
#         delete_chat = driver.find_element(
#             by = AppiumBy.XPATH,
#             value = '//android.widget.TextView[@text="حذف گفتگو"]'
#         )
#         assert delete_chat.is_displayed(),'delete chat find'
#         delete_chat.click()
#
#         #confirm delete chat history
#         confirm_delete_chat = driver.find_element(
#             by = AppiumBy.XPATH,
#             value = '//android.widget.TextView[@text="حذف"]'
#         )
#         assert confirm_delete_chat.is_displayed(),'confirm delete chat dialog find'
#         confirm_delete_chat.click()

@describe("create group thread")
class TestCreateGroupThread:
    @it("click menu and create new group")
    def test_click_menu_create_new_group(self,driver):
        time.sleep(5)
        print("Script is running!")
        #click on menu
        toggle_menu = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="Toggle drawer"]'
        )
        assert toggle_menu.is_displayed(), 'toggle menu find'
        toggle_menu.click()

        #click on create new group
        create_new_group = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("ایجاد گروه جدید")'))
        )
        assert create_new_group.is_displayed(),'create new group find'
        create_new_group.click()

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
        search_input.send_keys('الهام Test😶')

        #click on expected search result
        time.sleep(2)
        select_first_participant = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("الهام Test😶")'))
        )
        assert select_first_participant.is_displayed(), ' find الهام Test😶'
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
        select_second_participant = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("آزیتا تست")'))
        )
        assert select_second_participant.is_displayed(), ' find آزیتا تست'
        time.sleep(2)
        select_second_participant.click()

        #click on next to go for define name for group
        time.sleep(2)
        next_icon = driver.find_element(
            by = AppiumBy.XPATH,
            value = '//android.widget.TextView[@text="بعدی"]'
        )
        assert next_icon.is_displayed(),'next icon find'
        next_icon.click()

        #define name for group
        group_name = 'گروه تستی اندروید برای اتومیشن'
        group_name_input = driver.find_element(
            by = AppiumBy.XPATH,
            value = '//android.widget.EditText'
        )
        assert group_name_input.is_displayed(),'group name input find'
        group_name_input.click()
        group_name_input.send_keys(group_name)

        #click image icon
        time.sleep(2)
        image_icon = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View'
        )
        assert image_icon.is_displayed(),'image icon find'
        image_icon.click()
        #scroll and select an specific image
        image_name = "Photo taken on 29 Jan 2025, 11:08:23 pm"

        # Use UiScrollable to scroll until the image is found
        scrollable_gallery = '''
            new UiScrollable(new UiSelector().resourceId("com.google.android.providers.media.module:id/bottom_sheet"))
                .setAsVerticalList()
                .scrollToBeginning(10)
                .scrollBackward()
                .scrollIntoView(new UiSelector().descriptionContains("{}"))
            '''.format(image_name)

        # Execute scrolling command
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=scrollable_gallery)

        select_image = driver.find_element(
            by=AppiumBy.XPATH,
            value=f'//android.widget.FrameLayout[@content-desc="{image_name}"]'
        )
        assert select_image.is_displayed()
        select_image.click()
















