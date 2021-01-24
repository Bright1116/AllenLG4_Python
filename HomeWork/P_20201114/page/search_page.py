#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2021/1/24 15:41
# FileName: search_page.py
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from HomeWork.P_20201114.page.base_page import BasePage


class SearchPage(BasePage):
    def input_search_contact(self, contact_name):
        self.find(MobileBy.XPATH, "//*[@text='搜索']").send_keys(contact_name)
        sleep(2)
        ele_contacts = self.finds(MobileBy.XPATH, f"//*[@text='{contact_name}']")
        before_num = len(ele_contacts)
        if before_num < 2:
            print("没有可删除的人员")
            return
        ele_contacts[1].click()
        from HomeWork.P_20201114.page.person_info_page import PersonInfoPage
        return PersonInfoPage(self.driver), before_num
