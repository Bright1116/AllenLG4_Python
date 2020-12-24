#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2020/12/23 23:20
# FileName: base_page.py

# 基类，用来完成一些初始化操作，存放最基本的方法，比如实例化driver，find...
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver
        if self._base_url != "":
            self.driver.get(self._base_url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def wait_for_click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))
