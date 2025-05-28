import pytest
from configs.appium_config import initialize_driver
from modules.login_module import LoginPage

@pytest.fixture
def driver():
    """
    Fixture to provide a driver instance for tests.
    """
    driver = initialize_driver()
    yield driver
    if driver:
        driver.quit()

@pytest.fixture
def login(driver):
    """
    Fixture to perform login before running tests.
    """
    login_page = LoginPage()
    login_page.test_write_phone_number(driver)
    login_page.test_send_phone_number(driver)
    login_page.test_allow_permission_autofill(driver)
    login_page.test_allow_permission_notification(driver)