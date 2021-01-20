#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2021/1/20 7:47
# FileName: test_contact.py

import logging
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWX:
    def setup(self):
        caps = {"platformName": "Android",
                "deviceName": "hogwarts",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": "True"}
        # 最重要的代码，建立客户端与服务端的连接
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_contact(self):
        logging.basicConfig(level=logging.INFO)
        name = "hogwarts_00003"
        gender = "男"
        phone_num = "13812121214"
        # 点击【通讯录】

        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击【添加成员】

        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        # 点击【手动输入添加】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
            name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone_num)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").text
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert result == "添加成功"
        # sleep(2)
        # print(self.driver.page_source)

    def test_del_contact(self):
        name = "hogwarts_00003"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq_").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView").click()
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ffq").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(name)
        sleep(2)
        ele_contacts = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        before_num = len(ele_contacts)
        if before_num < 2:
            print("没有可删除的人员")
            return
        ele_contacts[1].click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ie0").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        # self.driver.find_element(MobileBy.XPATH, f"//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        sleep(2)
        ele_contacts_after_del = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        after_num = len(ele_contacts_after_del)
        assert after_num == before_num - 1
