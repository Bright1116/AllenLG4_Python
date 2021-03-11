#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2021/3/9 07:05
# FileName: get_path.py

import os

base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# print(base_dir)

ini_file = os.path.join(base_dir, r'config\api_test.ini')
# print(ini_file)

# 测试用例的路径
case_dir = os.path.join(base_dir, 'testcases')
# print(case_dir)

# # 测试报告的路径
# testReport_dir = os.path.join(base_dir, r'OutPut\TestReport')
# # print(testReport_dir)

# 日志文件路径
logger_dir = os.path.join(base_dir, r'output\logs')
# print(logger_dir)

