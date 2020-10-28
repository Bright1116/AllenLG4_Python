#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2020/10/29 5:55
# FileName: mian.py

import pytest

if __name__ == '__main__':
    pytest.main(["-s", "-v",
                 "--alluredir=output/allure_reports"])
