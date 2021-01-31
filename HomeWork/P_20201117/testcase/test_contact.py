#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from HomeWork.P_20201117.page.app import App
from HomeWork.P_20201117.page.base_page import load_data


class TestWX:
    test_data = load_data("../testdata/test_data.yaml")['data']

    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    @pytest.mark.parametrize('testData', test_data)
    def test_add_contact(self, testData):
        result = self.main.goto_contact_list(). \
            add_member().add_member_manual(). \
            edit_contact(testData[0], testData[1], testData[2]).verify_toast()
        assert '添加成功' == result

    @pytest.mark.parametrize('testData', test_data)
    def test_del_contact(self, testData):
        before_contact_object = self.main.search_contact().input_search_contact(testData[0])
        before_contact_num = before_contact_object[1]
        after_contact_num = before_contact_object[0].access_edit_contact().del_contact(testData[0])
        assert after_contact_num == before_contact_num - 1

    def teardown_class(self):
        self.app.stop()
