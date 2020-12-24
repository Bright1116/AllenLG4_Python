#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2020/12/23 6:35
# FileName: test_contact.py
from HomeWork.P_20201107.pageobjects.index_page import IndexPage


class TestContact:
    def setup(self):
        self.index = IndexPage()

    def test_add_contact(self):
        name = "Allen"
        account = "Allen_1877"
        phone_number = "15800454682"
        e_mail = "allen@qq.com"
        position = "开发经理"
        add_member_page = self.index.click_add_member()
        add_member_page.add_member(name, account, phone_number, e_mail, position)
        result = add_member_page.get_member(name)
        assert result
