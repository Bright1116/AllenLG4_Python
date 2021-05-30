#!/usr/bin/env python

# Author  : Allen Bright
# Time    : 2021/5/28 6:53
# FileName: enterprise_wechat.py
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "10",  # "10" 、"7.1.2"
    "deviceName": "huawei",
    "appPackage": "com.tencent.wework",  # com.lemon.lemonban , com.eg.android.AlipayGphone
    "appActivity": ".launch.LaunchSplashActivity",
    # com.lemon.lemonban.activity.WelcomeActivity , com.eg.android.AlipayGphone.AlipayLogin
    "noReset": True
}

# 跟appium建立连接，然后再把启动参数发过去。
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 点击【通讯录】按钮
loc_addressList_button = (MobileBy.XPATH, "//*[@text='通讯录']")
WebDriverWait(driver, 30).until(ec.visibility_of_element_located(loc_addressList_button))
driver.find_element(*loc_addressList_button).click()

# 点击【添加成员】
loc_add_member = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                '.scrollable(true).instance(0))'
                                                '.scrollIntoView(new UiSelector()'
                                                '.text("添加成员").instance(0));')
WebDriverWait(driver, 30).until(ec.visibility_of_element_located(loc_add_member))
driver.find_element(*loc_add_member).click()
