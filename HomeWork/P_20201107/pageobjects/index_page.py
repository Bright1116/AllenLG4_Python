#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2020/12/19 22:33
# FileName: index_page.py
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from HomeWork.P_20201107.pageloctors.loc_index_page import LocIndexPage
from HomeWork.P_20201107.pageobjects.add_member_page import AddMemberPage
from HomeWork.P_20201107.pageobjects.base_page import BasePage


# 主页


"""
启动命令：chrome --remote-debugging-port=9222
"""


class IndexPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    # def __init__(self):
    #     option = Options()
    #     option.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(5)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    # def goto_login(self):
    #     # click login
    #     self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
    #     # 进入到登录页面
    #     return LoginPage(self.driver)
    #
    # def goto_register(self):
    #     # click register
    #     self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
    #     # 进入注册页
    #     return RegisterPage(self.driver)

    def click_add_member(self):
        # time.sleep(3)
        self.find(LocIndexPage.add_member_button).click()
        return AddMemberPage(self.driver)
