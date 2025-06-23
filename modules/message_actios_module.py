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

    def find_child_text_with_scroll(self, message_text,max_swipes=1, retry_on_top=True):
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

            # found = False
            scrolled_once = False

            while True:
                for i in range(max_swipes):
                    try:
                        # 2. به دنبال TextView با متن مورد نظر بگرد
                        element = self.driver.find_element(
                            by=AppiumBy.XPATH,
                            value=f'//android.widget.TextView[@text="{message_text}"]'
                        )
                        time.sleep(5)
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
                    # 📌 اگر پیام پیدا نشد، متن رو ارسال کن
                    print("⚠️ پیام پیدا نشد. در حال ارسال پیام...")
                    return None

        except NoSuchElementException as e:
            print("❌ المنت scrollable پیدا نشد! لطفاً xpath صحیح را چک کنید.")
            return None
    # def edit(self, action_name,origin_message,edit_message_text):
    #
    #     time.sleep(3)
    #     click_element(self.driver,AppiumBy.XPATH,f'//android.widget.TextView[@text="{action_name}"]')
    #     send_keys_to_element(self.driver,AppiumBy.XPATH,f'//android.widget.EditText[@text="{origin_message}"]',f'{edit_message_text}')
    #     click_element(self.driver,AppiumBy.XPATH,'//android.view.View[@content-desc="send"]')

    def edit(self, action_name, origin_message, edit_message_text):
        time.sleep(2)

        # اول بررسی کن پیام موجود هست یا نه (بدون کلیک)
        message_element = self.find_child_text_with_scroll(origin_message)

        if message_element:
            try:
                # حالا روش کلیک کن تا بتونی Action name رو ببینی
                message_element.click()
                time.sleep(1)

                # تلاش برای پیدا کردن Action name
                click_element(self.driver, AppiumBy.XPATH, f'//android.widget.TextView[@text="{action_name}"]')

            except NoSuchElementException:
                # پیام بود ولی Action name پیدا نشد → باید پیام جدید بفرستی
                print("⚠️ پیام پیدا شد ولی Action name موجود نیست. ارسال پیام جدید...")
                send_keys_to_element(self.driver,AppiumBy.XPATH,'//android.widget.EditText[@text="اینجا بنویسید…"]',origin_message)
                click_element(self.driver, AppiumBy.XPATH, '//android.view.View[@content-desc="send"]')
                time.sleep(2)

                # دوباره تلاش کن
                self.edit(action_name, origin_message, edit_message_text)
                return

        else:
            # پیام پیدا نشد → ارسال پیام جدید
            print("🔴 پیام پیدا نشد. ارسال پیام جدید...")
            send_keys_to_element(self.driver,AppiumBy.XPATH,'//android.widget.EditText[@text="اینجا بنویسید…"]',origin_message)
            click_element(self.driver, AppiumBy.XPATH, '//android.view.View[@content-desc="send"]')
            time.sleep(2)

            # دوباره تلاش کن برای ویرایش
            self.edit(action_name, origin_message, edit_message_text)
            return

        # ✅ اگر به اینجا رسیدی یعنی پیام هست و Action name هم پیدا شده
        print("✏️ در حال ویرایش پیام...")
        send_keys_to_element( self.driver,AppiumBy.XPATH,f'//android.widget.EditText[@text="{origin_message}"]',edit_message_text)
        click_element(self.driver, AppiumBy.XPATH, '//android.view.View[@content-desc="send"]')


    def delete(self,edit_message_text,action_name,delete_for_all,delete_for_me,confirm):
        message_element = self.find_child_text_with_scroll(edit_message_text)
        if message_element:
            message_element.click()
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
        else:
            send_keys_to_element(self.driver,AppiumBy.XPATH,'//android.widget.EditText[@text="اینجا بنویسید…"]',edit_message_text)
            click_element(self.driver, AppiumBy.XPATH, '//android.view.View[@content-desc="send"]')
            self.delete(edit_message_text,action_name,delete_for_all,delete_for_me,confirm)


    def forward(self,message,action_name):
        message_element = self.find_child_text_with_scroll(message)
        if message_element:
            message_element.click()
            if action_name:
                click_element(self.driver,AppiumBy.XPATH,f'//android.widget.TextView[@text="{action_name}"]')
                #کلیک روی آیکن سرچ برای پیدا کردن ترد موردنظر برای انجام اکشن فوروارد
                click_element(self.driver,AppiumBy.XPATH,'//android.view.View[@content-desc="Search"]')
                send_keys_to_element(self.driver,AppiumBy.XPATH,'//android.widget.EditText','گروه قدیم خودم')
                click_element(self.driver,AppiumBy.XPATH,'//android.widget.TextView[@text="گروه قدیم خودم"]')
                click_element(self.driver,AppiumBy.XPATH,'//android.view.View[@content-desc="send"]')
                self.find_child_text_with_scroll(message)


            else:
                print("message can not forward")
        else:
            send_keys_to_element(self.driver,AppiumBy.XPATH,'//android.widget.EditText[@text="اینجا بنویسید…"]',message)
            click_element(self.driver, AppiumBy.XPATH, '//android.view.View[@content-desc="send"]')
            self.forward(message,action_name)

    # def copy(self):
    # def select(self):

    # def reply_private(self,message,action_name,):
        #find message
        self.find_child_text_with_scroll('test')
        #check the message is not mine to make it possible for reply private
