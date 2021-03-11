#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2021/3/9 07:32
# FileName: read_config.py

from configparser import ConfigParser

from HomeWork.p_20201201.enterprise_wechat_practice.config.get_path import ini_file


class ReadConfig(ConfigParser):

    def __init__(self, path):
        super().__init__()
        self.read(path, encoding="utf-8")


conf = ReadConfig(ini_file)

if __name__ == '__main__':
    print(conf.get("log", "name"))
