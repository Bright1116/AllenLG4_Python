#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from app.page.contact_add_page import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from HomeWork.P_20201114.page.base_page import BasePage
from HomeWork.P_20201114.page.contact_add_page import ContactAddPage


class MemberInviteMenuPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def add_member_manual(self):
        # 点击【手动输入添加】
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        return ContactAddPage(self.driver)

    def verify_toast(self):
        # result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        result = self.get_toast_text()
        return result
