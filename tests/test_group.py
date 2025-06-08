import pytest

from conftests import login, driver
from modules.group_module import GroupPage

@pytest.mark.usefixtures("driver","login") # اجرای لاگین قبل از هر تست
class TestGroup:
    def test_create_and_delete_group(self, driver):
        group_page = GroupPage(driver)
        group_page.create_group("ایجاد گروه تستی از اپ اندروید", ["الهام test", "آزیتا تست"])
        group_page.delete_participant("آزیتا تست")
        group_page.add_participant("آزیتا تست")
        group_page.delete_group()