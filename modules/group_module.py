from utils.utils import find_element, click_element, send_keys_to_element, scroll_until_element_found,actionBuilder
from appium.webdriver.common.appiumby import AppiumBy
import time

class GroupPage:
    def __init__(self, driver):
        self.driver = driver

    def create_group(self, group_name, participants):
        """Create a new group with the given name and participants."""
        # Open menu and navigate to "Create New Group"
        click_element(self.driver, AppiumBy.XPATH, '//android.view.View[@content-desc="Toggle drawer"]')
        click_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ایجاد گروه جدید")')

        # Search and select participants
        for participant in participants:
            click_element(self.driver, AppiumBy.XPATH, '//android.view.View[@content-desc="Search"]')
            time.sleep(3)
            send_keys_to_element(self.driver, AppiumBy.XPATH, '//android.widget.EditText', participant)
            click_element(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{participant}")')

        # Go to the next step and define the group name
        click_element(self.driver, AppiumBy.XPATH, '//android.widget.TextView[@text="بعدی"]')
        send_keys_to_element(self.driver, AppiumBy.XPATH, '//android.widget.EditText', group_name)
        click_element(self.driver, AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[4]')
        #send simple message to history
        click_input = click_element(self.driver,AppiumBy.XPATH,'//android.widget.EditText[@text="اینجا بنویسید…"]')
        time.sleep(2)
        print("+++++++++++++++++++")
        # click_input = self.driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='//android.widget.EditText[@text="اینجا بنویسید…"]')
        # assert click_input.is_displayed(), "input for typing message is find a"
        # click_input.click()
        send_keys_to_element(self.driver,AppiumBy.XPATH,'//android.widget.EditText[@text="اینجا بنویسید…"]',"این یک پیام تستی برای اتومیشن اندروید است ")
        # send_text_message = self.driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='//android.view.View[@content-desc="send"]'
        # )
        send_text_message = click_element(self.driver,AppiumBy.XPATH,'//android.view.View[@content-desc="send"]')
        # assert send_text_message.is_displayed(), "send icon is find"
        # send_text_message.click()
        time.sleep(3)

    def delete_participant(self, participant_name):
        """Delete a participant from the group."""
        click_element(self.driver,AppiumBy.XPATH,'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]')
        participant = find_element(self.driver, AppiumBy.XPATH, f'//android.widget.TextView[@text="{participant_name}"]', timeout=5)
        actionBuilder(self.driver,participant)
        click_element(self.driver, AppiumBy.XPATH, '//android.widget.TextView[@text="حذف از گروه"]')
        click_element(self.driver, AppiumBy.XPATH, '//android.widget.TextView[@text="تایید"]')

    def add_participant(self, participant_name):
        """Add a participant to the group."""
        click_element(self.driver, AppiumBy.XPATH, '//android.widget.TextView[@text="افزودن اعضا"]')
        click_element(self.driver, AppiumBy.XPATH, '//android.view.View[@content-desc="Search"]')
        send_keys_to_element(self.driver, AppiumBy.XPATH, '//android.widget.EditText', participant_name)
        click_element(self.driver, AppiumBy.XPATH, f'//android.widget.TextView[@text="{participant_name}"]')
        click_element(self.driver, AppiumBy.XPATH, '//android.widget.TextView[@text="افزودن"]')
        click_element(self.driver, AppiumBy.XPATH, '//android.widget.TextView[@text="تایید"]')

    def delete_group(self):
        """Delete the current group."""
        click_element(self.driver, AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Cam"]')
        click_element(self.driver, AppiumBy.XPATH, '//android.widget.TextView[@text="حذف گروه"]')
        click_element(self.driver, AppiumBy.XPATH, '//android.widget.TextView[@text="حذف"]')
