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
        # shelve模块， python自带的对象持久化存储
        # cookies = [
        #     {'domain': '.qq.com', 'expiry': 1608163211, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688853958536934'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': '8yeyxkWY_GIxxBTRHCm-DrKCro05tibpH1Ut-IIJ-CkWAwY-dGDXG8yZW2xzfjmwnuNNCBRgASkCN3zdxovptJeWglWCpEI40N6SvvGb9k4STUKqs5uPu-YmjpuGe2jAeL00iW9XVaDb7Nt1uhKaUj9oIsRnrosc0y5svQjgGLyqxKYjPvcTbVTf_MWg7ecrcLi58_HCq5M-Zhrns9AabCmks7t8bXt2AN-PFnm7XXz0pihwCjXTMQjMWbwAtpKUp01poqIZvlQFKBHHahzsNg'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688853958536934'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '3604857015411711'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1608163807, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '6i9aaso'},
        #     {'domain': '.qq.com', 'expiry': 1608249563, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.709143343.1607960219'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1639496218, 'httpOnly': False,
        #      'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True,
        #      'value': '1607850679,1607960219'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1610755173, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970325103085258'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
        #      'secure': True, 'value': '2223724544'},
        #     {'domain': '.qq.com', 'expiry': 1609244274, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': True,
        #      'value': '000100007a988d44fbe5bd1734c3353a2e943970284f99d420418552bf9372f676bd91333116c18ff246b18d'},
        #     {'domain': '.qq.com', 'expiry': 1609244274, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': True,
        #      'value': 'o1126983364'},
        #     {'domain': '.qq.com', 'expiry': 1671235163, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.1737553657.1582007476'},
        #     {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
        #      'value': '985c3d1d0fc214eb4f3b12adb5e6594e10d037c7b328dc5d2dedcc6e87126b1a'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a3922132'},
        #     {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
        #      'value': 'LlAYmgOXGe'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': True, 'value': '1382088990'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'z3ET5Y7aJp0Ypgogmzu0MYBIdrek7x1eEoVV0KdXfP-xqayw6jC-SiJmtZv5eYiR'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1636151163, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': True, 'value': '0'},
        #     {'domain': '.qq.com', 'expiry': 1920775414, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
        #      'secure': True, 'value': '0_61d7b1664a58d'}]
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
