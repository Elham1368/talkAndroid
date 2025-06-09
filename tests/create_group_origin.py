import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from selenium.common.exceptions import NoSuchElementException


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

@describe("create group thread")
class TestCreateGroupThread:
    @it("click menu and create new group")
    def test_click_menu_create_new_group(self,driver):
        time.sleep(5)

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
        time.sleep(2)

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

        # select_second_participant = driver.find_element(
        #     by = AppiumBy.XPATH,
        #     value= '//android.widget.TextView[@text="آزیتا تست"]'
        # )
        select_second_participant = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("آزیتا تست")'))
        )
        assert select_second_participant.is_displayed(), ' find آزیتا تست'
        time.sleep(2)
        select_second_participant.click()

        #click on next to go for define name for group
        next_icon = driver.find_element(
            by = AppiumBy.XPATH,
            value = '//android.widget.TextView[@text="بعدی"]'
        )
        assert next_icon.is_displayed(),'next icon find'
        time.sleep(2)
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
        # time.sleep(2)
        # image_icon = driver.find_element(
        #     by = AppiumBy.XPATH,
        #     value= '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View'
        # )
        # assert image_icon.is_displayed(),'image icon find'
        # image_icon.click()
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
        # select_image = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]'
        # )
        # assert select_image.is_displayed(),'select image find'
        # time.sleep(2)
        # select_image.click()
        #
        # #confirm selected image
        # confirm_image = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]'
        # )
        # assert confirm_image.is_displayed(),'confirm image find'
        # confirm_image.click()

        #click on created group button and jump to history
        time.sleep(10)
        create_group_button =  driver.find_element(
            by = AppiumBy.XPATH,
            value = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[4]'
        )
        assert create_group_button.is_displayed(),'create group find'
        create_group_button.click()

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

    @it("delete participant from group")
    def test_delete_participant_from_group(self,driver):
        #click on header to go to thread info
        click_header = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]'
        )
        assert click_header.is_displayed(),'click header find'
        click_header.click()

        #long press on an specific participant set admin ...
        participant = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//android.widget.TextView[@text="آزیتا تست"]'
        )
        actions = ActionBuilder(driver)
        # Get the element's location
        participant_location = participant.location

        # Add the pointer input to the ActionBuilder
        actions.add_pointer_input(interaction.POINTER_TOUCH, "touch")

        # Define the long press action
        (
            actions.pointer_action  # Access the pointer_action from the ActionBuilder
            .move_to_location(participant_location['x'], participant_location['y'])  # Move to element's location
            .pointer_down()  # Start pressing
            .pause(2)  # Wait for 2 seconds (simulate long press)
            .pointer_up()  # Release the press
        )

        # Perform the action
        actions.perform()

        #select delete participant from component
        delete_participant = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//android.widget.TextView[@text="حذف از گروه"]'
        )
        assert delete_participant.is_displayed(), 'delete from group find'
        delete_participant.click()

        #confirm delete participant
        confirm_delete = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//android.widget.TextView[@text="تایید"]'
        )
        assert confirm_delete.is_displayed(),'confirm is done'
        confirm_delete.click()
        #check participant is not exist or not displayed

        try:
            element = driver.find_element(
                by = AppiumBy.XPATH,
                value= '//android.widget.TextView[@text="آزیتا تست"]'
            )
            # If the element exists, check if it is not displayed
            assert not element.is_displayed(), "Element is displayed but should not be"
        except NoSuchElementException:
            # If the element does not exist, the assertion passes
            assert True, "Element does not exist as expected"

    @it("add participant to group")
    def test_add_participant_to_group(self,driver):
        time.sleep(3)
        #click on add participant  in thread info
        add_participant = driver.find_element(
            by = AppiumBy.XPATH,
            value='//android.widget.TextView[@text="افزودن اعضا"]'
        )
        assert add_participant.is_displayed(),"افزودن اعضا find"
        add_participant.click()

        #opening contact list and search a contact
        search_icon = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//android.view.View[@content-desc="Search"]'
        )
        assert search_icon.is_displayed(),'search icon find'
        search_icon.click()

        #find and select search input
        search_input = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//android.widget.EditText'
        )
        assert search_input.is_displayed(),'search input find'
        search_input.send_keys('آزیتا تست')
        time.sleep(3)

        #select آزیتا تست from search result
        new_participant = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//android.widget.TextView[@text="آزیتا تست"]'
        )
        assert new_participant.is_displayed(),'آزیتا تست find'
        new_participant.click()

        #click on add button
        add_button = driver.find_element(
            by = AppiumBy.XPATH,
            value = '//android.widget.TextView[@text="افزودن"]'
        )
        assert add_button.is_displayed(),'آفزودن find'
        add_button.click()

        #confirm from history feature without select any time
        from_history_confirm = driver.find_element(
            by = AppiumBy.XPATH,
            value = '//android.widget.TextView[@text="تایید"]'
        )
        assert from_history_confirm.is_displayed(), 'from_history_confirm find'
        from_history_confirm.click()

        #check contact added to group participants
        try:
            new_contact = driver.find_element(
                by = AppiumBy.XPATH,
                value= '//android.widget.TextView[@text="آزیتا تست"]'
            )
            # If the element exists, check if it is  displayed
            assert  new_contact.is_displayed(), "Element is displayed but should not be"
        except NoSuchElementException:
        # If the element does not exist, the assertion passes
            assert False, "Element does not exist as expected"

    @it("check group on thread list")
    def test_check_group_thread_list(self,driver):
        time.sleep(3)
        #back from thread info to history
        back_to_history = driver.find_element(
            by= AppiumBy.XPATH,
            value='//android.view.View[@content-desc="Menu"]'
        )
        assert back_to_history.is_displayed(),'close_keyboard find'
        back_to_history.click()

        #back from new history to thread list
        time.sleep(3)
        back_to_thread_list = driver.find_element(
            by= AppiumBy.XPATH,
            value='//android.view.View[@content-desc="Menu"]'
        )
        assert back_to_thread_list.is_displayed(),'back to thread list find'
        back_to_thread_list.click()

        driver.background_app(7)

        #check the new group is displaying in thread list
        time.sleep(3)
        scrollable_container = driver.find_element(
            by=AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]')
        group_thread_name= 'گروه تستی اندروید برای اتومیشن'
        # Scroll until the element is found
        max_attempts = 10
        attempts = 0

        while attempts < max_attempts:
            try:
                # Find the element by text using XPath
                element = driver.find_element(
                    by=AppiumBy.XPATH,
                    value=f'//*[@text="{group_thread_name}"]')
                print("Element found!")
                #going to history
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

    @it("delete the new group history")
    def test_delete_new_group(self,driver):
        time.sleep(3)
        #click header for opening thread info
        history_header = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]'
        )
        assert history_header.is_displayed(),'history header find'
        history_header.click()

        #click on ... to find delete group
        more_icon = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//android.widget.ImageView[@content-desc="Cam"]'
        )
        assert more_icon.is_displayed(),'delete contact icon find'
        more_icon.click()

        #select delete group
        delete_group = driver.find_element(
            by= AppiumBy.XPATH,
            value= '//android.widget.TextView[@text="حذف گروه"]'
        )
        assert delete_group.is_displayed(), ' delete group find'
        delete_group.click()

        #confirm delete group
        confirm_delete_group = driver.find_element(
            by = AppiumBy.XPATH,
            value= '//android.widget.TextView[@text="حذف"]'
        )
        assert confirm_delete_group.is_displayed(), ' delete group find'
        confirm_delete_group.click()