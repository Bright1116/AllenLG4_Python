#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2020/12/24 7:41
# FileName: loc_add_member_page.py
from selenium.webdriver.common.by import By


class LocAddMemberPage:
    user_name = (By.ID, "username")
    account = (By.ID, "memberAdd_acctid")
    phone_number = (By.ID, "memberAdd_phone")
    e_mail = (By.ID, "memberAdd_mail")
    job_position = (By.ID, "memberAdd_title")
    save_button = (By.XPATH, "(//a[@class='qui_btn ww_btn js_btn_save'])[1]")
    checkbox_button = (By.CSS_SELECTOR, ".ww_checkbox")
    next_page_button = (By.CSS_SELECTOR, ".ww_pageNav_info_text")
    page_number = (By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal")
