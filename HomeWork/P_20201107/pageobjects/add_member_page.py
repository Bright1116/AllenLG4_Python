#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2020/12/21 7:07
# FileName: add_member_page.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from HomeWork.P_20201107.pageobjects.base_page import BasePage
from HomeWork.P_20201107.pageloctors.loc_add_member_page import LocAddMemberPage


class AddMemberPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def add_member(self, name, account, phone_number, e_mail, position):
        # name = "Allen"
        # account = "Allen_1877"
        # phone_number = "15800454681"
        # time.sleep(3)
        # input name
        self.find(LocAddMemberPage.user_name).send_keys(name)
        # input account
        self.find(LocAddMemberPage.account).send_keys(account)
        # input phone_number
        self.find(LocAddMemberPage.phone_number).send_keys(phone_number)
        # 输入邮箱
        self.find(LocAddMemberPage.e_mail).send_keys(e_mail)
        # 输入职务
        self.find(LocAddMemberPage.job_position).send_keys(position)
        # click save
        # 如果页面上相同属性的元素有多个，那么通过find_element定位到的元素是第一次出现的元素
        self.find(LocAddMemberPage.save_button).click()
        return True

    def get_member(self, value):
        locator = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(locator)
        # find_elements方法，返回的是元素列表[element1, element2, ...]
        titles_total = []
        while True:
            elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            titles = [element.get_attribute("title") for element in elements]
            if value in titles:
                return True
            titles_total.extend(titles)

            page: str = self.find(LocAddMemberPage.next_page_button).text
            num, total = page.split("/", 1)
            # print(num, total)

            if int(num) == int(total):
                return False
            else:
                self.find(LocAddMemberPage.page_number).click()

