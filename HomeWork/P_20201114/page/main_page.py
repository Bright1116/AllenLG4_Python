#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 主页
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from HomeWork.P_20201114.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver
    # 首页-通讯录
    _contact_list = (MobileBy.XPATH, "//*[@text='通讯录']")
    _search_button = (MobileBy.XPATH, "//android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView")

    def goto_contact_list(self):
        """
        进入到通讯录
        """
        # 点击【通讯录】

        self.find(*self._contact_list).click()
        from HomeWork.P_20201114.page.contact_list_page import ContactListPage
        return ContactListPage(self.driver)

    def search_contact(self):
        """
        搜索联系人
        :return:
        """
        self.find(*self._contact_list).click()
        self.find(*self._search_button).click()
        sleep(2)
        from HomeWork.P_20201114.page.search_page import SearchPage
        return SearchPage(self.driver)
