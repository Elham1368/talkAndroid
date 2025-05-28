from tabnanny import check

from utils.utils import find_element, click_element, send_keys_to_element, scroll_until_element_found,actionBuilder
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time

class SendMessageActions:
    def __init__(self, driver):
        self.driver = driver

    def open_single_thread(self,thread_name):
        print("Hiiiiiiiiiiiiiiiiiiiiii")
        # Scroll until the element is found
        max_attempts = 10
        attempts = 0

        while attempts < max_attempts:
            try:
                time.sleep(5)
                # Find the element by text using XPath
                click_element(self.driver,AppiumBy.XPATH,f'//android.widget.TextView[@text="{thread_name}"]')
                # element = self.driver.find_element( by=AppiumBy.XPATH,value=f'//*[@text="{thread_name}"]')
                print("Element found!")
                # element.click()  # Perform actions on the found element
                break
            except:
                # Scroll down if the element is not found
                time.sleep(5)
                scrollable_container = self.driver.find_element(
                    by=AppiumBy.XPATH,
                    value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]')
                print(scrollable_container,"is finddddddddddddddd")
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

    def find_child_text_with_scroll(self, message_text,max_swipes=10, retry_on_top=True):
        time.sleep(5)

        #داخل المنت scrollable اسکرول کن و به دنبال TextView با متن خاص بگرد
        # XPATH المنت scrollable
        scrollable_xpath = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]'

        try:
            # 1. المنت scrollable رو پیدا کن
            scrollable_element = self.driver.find_element(by=AppiumBy.XPATH, value=scrollable_xpath)
            print("✅ المنت scrollable پیدا شد.")

            location = scrollable_element.location
            size = scrollable_element.size

            start_x = location['x'] + size['width'] / 2
            start_y = location['y'] + size['height'] * 0.8  # پایین صفحه
            end_y = location['y'] + size['height'] * 0.2    # بالای صفحه

            found = False
            scrolled_once = False

            while not found:
                for i in range(max_swipes):
                    try:
                        # 2. به دنبال TextView با متن مورد نظر بگرد
                        element = self.driver.find_element(
                            by=AppiumBy.XPATH,
                            value=f'//android.widget.TextView[@text="{message_text}"]'
                        )
                        time.sleep(5)
                        element.click()
                        return element
                    except NoSuchElementException:
                        # 3. اگر پیدا نشد، swipe کن
                        self.driver.swipe(start_x, end_y, start_x, start_y, 500)
                        time.sleep(1)
                        scrolled_once = True

                if scrolled_once and retry_on_top:
                    # swipe up به سمت بالا
                    for _ in range(max_swipes):
                        self.driver.swipe(start_x, start_y, start_x, end_y, 500)
                        time.sleep(1)
                    scrolled_once = False
                    retry_on_top = False  # فقط یکبار به بالا برگرد
                else:
                    return False

        except NoSuchElementException as e:
            print("❌ المنت scrollable پیدا نشد! لطفاً xpath صحیح را چک کنید.")

    def edit(self, action_name,origin_message,edit_message_text):
        time.sleep(3)
        click_element(self.driver,AppiumBy.XPATH,f'//android.widget.TextView[@text="{action_name}"]')
        send_keys_to_element(self.driver,AppiumBy.XPATH,f'//android.widget.EditText[@text="{origin_message}"]',f'{edit_message_text}')
        click_element(self.driver,AppiumBy.XPATH,'//android.view.View[@content-desc="send"]')

    def delete_for_me(self,edit_message_text,action_name,delete_for_all,delete_for_me,confirm):
        self.find_child_text_with_scroll(edit_message_text,15)
        if action_name:
            click_element(self.driver,AppiumBy.XPATH,f'//android.widget.TextView[@text="{action_name}"]')
        else:
            print("message is not editable")

        if delete_for_all:
            click_element(self.driver,AppiumBy.XPATH,f'//android.widget.TextView[@text="{delete_for_all}"]')
            click_element(self.driver,AppiumBy.XPATH,f'//android.widget.TextView[@text="{confirm}"]')
        else:
            click_element(self.driver,AppiumBy.XPATH,f'//android.widget.TextView[@text="{delete_for_me}"]')
            click_element(self.driver,AppiumBy.XPATH,f'//android.widget.TextView[@text="{confirm}"]')


    # def forward(self):
    # def copy(self):
    # def select(self):