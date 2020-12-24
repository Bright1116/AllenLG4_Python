#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2020/12/24 7:34
# FileName: loc_index_page.py

# 首页添加成员
from selenium.webdriver.common.by import By


class LocIndexPage:
    add_member_button = (By.XPATH, "//a[@node-type='addmember']")
