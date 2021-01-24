#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2021/1/24 15:54
# FileName: person_info_page.py
from appium.webdriver.common.mobileby import MobileBy

from HomeWork.P_20201114.page.base_page import BasePage


class PersonInfoPage(BasePage):
    def access_edit_contact(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/ie0").click()
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        from HomeWork.P_20201114.page.edit_contact_info import EditContactPage
        return EditContactPage(self.driver)
