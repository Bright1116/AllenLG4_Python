#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2021/1/24 16:08
# FileName: edit_contact_info.py
from appium.webdriver.common.mobileby import MobileBy

from HomeWork.P_20201117.page.base_page import BasePage


class EditContactPage(BasePage):
    def del_contact(self, contact_name):
        self.find_by_scroll("删除成员").click()
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        ele_contacts_after_del = self.finds(MobileBy.XPATH, f"//*[@text='{contact_name}']")
        after_num = len(ele_contacts_after_del)
        return after_num
