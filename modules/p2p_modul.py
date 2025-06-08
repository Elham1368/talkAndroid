from utils.utils import find_element, click_element, send_keys_to_element, scroll_until_element_found,actionBuilder
from appium.webdriver.common.appiumby import AppiumBy
import time

class P2P:
    def __init__(self, driver):
        self.driver = driver
    def test_open_menu_add_contact(self,menu_icon_xpath ):

        #click on menu
        click_element(self.driver,AppiumBy.XPATH,menu_icon_xpath)

        #click on add contact
        click_element(self.driver,AppiumBy.XPATH,'//android.widget.TextView[@text="افزودن مخاطب جدید"]')

        #check add contact modal is opened
        add_contact_modal = find_element(self.driver,AppiumBy.XPATH,'//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View/android.view.View[2]')
        assert add_contact_modal.is_displayed(),'add contact modal find'

    def test_create_contact(self,name,family,phone_number):

        #fill contact name
        send_keys_to_element(self.driver,AppiumBy.XPATH,'//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]',name)

        #fill contact family
        send_keys_to_element(self.driver,AppiumBy.XPATH,'//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]',family)

        #fill contact mobile number
        send_keys_to_element(self.driver,AppiumBy.XPATH,'//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[3]',phone_number)

        #click on add contact افزودن
        click_element(self.driver,AppiumBy.XPATH,'//android.widget.TextView[@text="افزودن"]')

    def test_check_contact_add(self,name,family,menu_icon_path,contact_list,search_icon):
        time.sleep(5)
        #click on menu
        click_element(self.driver,AppiumBy.XPATH,menu_icon_path)

        #click contacts list
        time.sleep(5)
        click_element(self.driver,AppiumBy.XPATH,contact_list)

        #click search icon
        click_element(self.driver,AppiumBy.XPATH,search_icon)

        #write the name added to list
        send_keys_to_element(self.driver,AppiumBy.XPATH,'//android.widget.EditText',name)

        #check the result name and family is equal to the contact added to list
        find_element(self.driver,AppiumBy.XPATH,f'//android.widget.TextView[@text="{name} {family} "]')

    def test_create_history_contact(self,name,family,text):
        time.sleep(5)
        #click on contact result
        click_element(self.driver,AppiumBy.XPATH,f'//android.widget.TextView[@text="{name} {family} "]')
        #send a simple message to history and create thread
        send_keys_to_element(self.driver,AppiumBy.XPATH,'//android.widget.EditText[@text="اینجا بنویسید…"]',text)
        click_element(self.driver,AppiumBy.XPATH,'//android.view.View[@content-desc="send"]')

    def test_check_single_thread_is_created(self,single_thread_name):
        #back from history to search list
        click_element(self.driver,AppiumBy.XPATH,'//android.view.View[@content-desc="Menu"]')

        #back from search list to contact list
        click_element(self.driver,AppiumBy.XPATH,'(//android.view.View[@content-desc="Back"])[1]')

        #back to thread list from contact
        click_element(self.driver,AppiumBy.XPATH,'//android.view.View[@content-desc="Back"]')

        time.sleep(4)
        #check the new single thread is exist in list or not
        scrollable_container = self.driver.find_element(
            by=AppiumBy.XPATH,
            value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]')
        # Scroll until the element is found
        max_attempts = 10
        attempts = 0

        while attempts < max_attempts:
            try:
                # Find the element by text using XPath and Perform actions on the found element
                click_element(self.driver,AppiumBy.XPATH,f'//android.widget.TextView[@text="{single_thread_name}"]')
                break
            except:
                # Scroll down if the element is not found
                size = scrollable_container.size
                location = scrollable_container.location
                start_x = location['x'] + size['width'] / 2
                start_y = location['y'] + size['height'] * 0.8  # Start from 80% of the container height
                end_y = location['y'] + size['height'] * 0.2  # End at 20% of the container height
                self.driver.swipe(start_x, start_y, start_x, end_y, 500)
                print("Scrolling...")
                attempts += 1

        if attempts == max_attempts:
            print("Element not found after maximum scroll attempts.")

    def test_delete_contact_history(self):
        #click header for opening thread info
        click_element(self.driver,AppiumBy.XPATH,'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]')

        #delete contact by click on delete icon
        click_element(self.driver,AppiumBy.XPATH,'//android.view.View[@content-desc="Delete"]')

        #confirm delete contact by click on delete icon
        click_element(self.driver,AppiumBy.XPATH,'//android.widget.TextView[@text="حذف"]')

        #delete chat by click on ... and delete thread
        click_element(self.driver,AppiumBy.XPATH,'//android.widget.ImageView[@content-desc="Cam"]')

        #select delete chat in ...
        click_element(self.driver,AppiumBy.XPATH,'//android.widget.TextView[@text="حذف گفتگو"]')

        #confirm delete chat history
        click_element(self.driver,AppiumBy.XPATH,'//android.widget.TextView[@text="حذف"]')
