#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 编辑成员页面
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from HomeWork.P_20201114.page.base_page import BasePage

'''
编辑联系人页面
'''


class ContactAddPage(BasePage):
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver

    def edit_contact(self, name, gender, phone_num):
        """
        编辑成员信息
        """
        self.find(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
            name)
        self.find(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()

        self.find(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone_num)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        from HomeWork.P_20201114.page.member_invite_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)

