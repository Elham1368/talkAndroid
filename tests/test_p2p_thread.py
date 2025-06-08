from symtable import Class

import pytest
from conftests import login, driver
from modules.p2p_modul import P2P

@pytest.mark.usefixtures("driver","login") # اجرای لاگین قبل از هر تست
class TestPToPThread:
    def test_create_and_delete_p2p_thread(self, driver):
        p2p = P2P(driver)
        p2p.test_open_menu_add_contact('//android.widget.Button')
        p2p.test_create_contact('الهام ایرانسل','2','09371521106')
        p2p.test_check_contact_add('الهام ایرانسل','2','//android.widget.Button','//android.widget.TextView[@text="مخاطبین"]','//android.view.View[@content-desc="Search"]')
        p2p.test_create_history_contact("الهام ایرانسل","2","این یک پیام تستی برای اتومیشن اندروید است ")
        p2p.test_check_single_thread_is_created('الهام ایرانسل 2')
        p2p.test_delete_contact_history()