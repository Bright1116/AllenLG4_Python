#!/usr/bin/env python
# -*- coding: utf-8 -*-
from HomeWork.P_20201114.page.app import App


class TestWX:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def test_add_contact(self):
        name = "Alice"
        gender = "女"
        phone_num = "16621701147"

        result = self.main.goto_contact_list(). \
            add_member().add_member_manual(). \
            edit_contact(name, gender, phone_num).verify_toast()
        assert '添加成功' == result

    def test_del_contact(self):
        name = "Alice"
        before_contact_object = self.main.search_contact().input_search_contact(name)
        before_contact_num = before_contact_object[1]
        after_contact_num = before_contact_object[0].access_edit_contact().del_contact(name)
        assert after_contact_num == before_contact_num - 1

    def teardown_class(self):
        self.app.stop()
