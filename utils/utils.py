from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
import time

# def find_element(driver, by, value, timeout=5):
#     """Find an element with a timeout."""
#     return WebDriverWait(driver, timeout).until(
#         EC.presence_of_element_located((by, value))
#     )
#
# def click_element(driver, by, value, timeout=5):
#     """Click on an element after finding it."""
#     element = find_element(driver, by, value, timeout)
#     element.click()

def find_element(driver, by, value, timeout=5):
    """
    Find an element with a fixed sleep timeout.
    """
    time.sleep(timeout)
    try:
        element = driver.find_element(by, value)
        assert element.is_displayed(), f"{value} is find"
        return element
    except NoSuchElementException:
        raise Exception(f"Element not found: {value}")

def click_element(driver, by, value, timeout=5):
    """
    Click on an element after finding it with a fixed sleep timeout.
    """
    time.sleep(timeout)  # منتظر بمانید به مدت مشخص شده (به ثانیه)
    try:
        element = driver.find_element(by, value)
        element.click()
    except NoSuchElementException:
        raise Exception(f"Element not clickable: {value}")

def send_keys_to_element(driver, by, value, text, timeout=5):
    """Send keys to an input element."""
    element = find_element(driver, by, value, timeout)
    element.clear()
    element.send_keys(text)

def is_element_displayed(driver, by, value, timeout=5):
    """Check if an element is displayed."""
    try:
        element = find_element(driver, by, value, timeout)
        return element.is_displayed()
    except (NoSuchElementException, TimeoutException):
        return False

def scroll_until_element_found(driver, container_by, container_value, target_text, max_attempts=10):
    """Scroll until the target element is found."""
    container = find_element(driver, container_by, container_value)
    size = container.size
    location = container.location
    start_x = location['x'] + size['width'] / 2
    start_y = location['y'] + size['height'] * 0.5
    end_y = location['y'] + size['height'] * 0.2

    attempts = 0
    while attempts < max_attempts:
        try:
            element = driver.find_element(AppiumBy.XPATH, f'//*[@text="{target_text}"]')
            return element
        except NoSuchElementException:
            driver.swipe(start_x, start_y, start_x, end_y, 500)
            attempts += 1
    raise NoSuchElementException(f"Element with text '{target_text}' not found after {max_attempts} attempts.")

def actionBuilder(driver,participant):
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