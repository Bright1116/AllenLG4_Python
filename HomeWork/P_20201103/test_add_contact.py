#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2020/12/17 7:21
# FileName: test_add_contact.py
import os
import shelve
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

"""
启动命令：chrome --remote-debugging-port=9222
"""
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# 批量导入通讯录excel文件
test_data_import_excel = os.path.join(base_dir, r'P_20201103\address_book_batch_import.xlsx')


class TestWechat:
    def setup_method(self, method):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        # pass
        self.driver.quit()

    # # @pytest.mark.skip
    # def test_case_one(self):
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     self.driver.find_element(By.ID, "menu_contacts").click()
    #
    # # @pytest.mark.skip
    # def test_cookie(self):
    #     cookies = self.driver.get_cookies()
    #     print(cookies)

    def test_import_contacts(self):
        # # shelve模块， python自带的对象持久化存储
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688853958536934'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'chd7-H5RbdD0YhJRXltW6P9AQnuT8cBS8UqBiA1DdmvYekKcSvpRMW5f54tSce8XFWtC2B-pAdiGEpdP783M6c7qlHRwrA65Mq_Z7U8Dy3VCQXc3z3djTZie5dE1wS90VSvnoC8mzVobv5uo_xmnibUapK5f0V8eWX3O2dz0NooA3ZADpHteASN0RWQKKLcBxUIfl-vh8mhYtm464gIybbP08w-vnns-rdqBDF1iGkcyZCwlAufBMpjutFzc3Z5k9VFms8GQPT9Opyi1Mob7rA'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688853958536934'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970325103085258'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'z3ET5Y7aJp0Ypgogmzu0MUgtk6OuqkTaUgCJBM2fbK5HEzxPBp6po2Ab3DinCBEh'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a7227375'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '4087939184364667'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1608414559, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '53b7jon'},
        #     {'domain': '.qq.com', 'expiry': 1608469579, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.240224087.1608383026'},
        #     {'domain': '.qq.com', 'expiry': 1671455179, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.1512077492.1608383026'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1639919023, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': False, 'value': '1953913876'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1639919050, 'httpOnly': False,
        #      'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608383051'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1610976093, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'},
        #     {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
        #      'value': '8d712880c3d70a6b937f0c94ae1afc891337c20c3a7e4d3c111934135e7e6042'},
        #     {'domain': '.qq.com', 'expiry': 2147483650, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
        #      'value': '2tBYyiOnT8'},
        #     {'domain': '.qq.com', 'expiry': 1608384150, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
        #      'secure': False, 'value': '5402440704'}]
        db = shelve.open('cookies')
        # db['cookie'] = cookies  # 把cookies加入到shelve数据库
        cookies = db['cookie']
        db.close()

        # 打开无痕新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 加入cookie
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # print(cookies)

        # 刷新当前页面，获取登录状态
        self.driver.refresh()
        time.sleep(5)
        # 点击导入联系人
        self.driver.find_element(By.XPATH, "// span[text() = '导入通讯录']").click()
        # 上传文件，选择文件的完整路径上传
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(test_data_import_excel)
        self.driver.find_element(By.LINK_TEXT, "导入").click()
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "完成").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='搜索成员、部门']").send_keys("张三")
        time.sleep(5)

        # 判断导入是否成功
        result = self.driver.find_element(By.XPATH,
                                          "//span[@class='member_colRight_operationBar_dep']/following-sibling::a[1]").text
        assert "禁用" == result
        time.sleep(10)
