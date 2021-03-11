#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2021/3/9 07:34
# FileName: my_logger.py

import os
import logging

from HomeWork.p_20201201.enterprise_wechat_practice.config.get_path import logger_dir
from HomeWork.p_20201201.enterprise_wechat_practice.utils.read_config import conf


class MyLogger(logging.Logger):

    def __init__(self, file=None):
        # 设置输出级别、输出渠道、输出日志格式
        super().__init__(conf.get("log", "name"), conf.get("log", "level"))

        # 日志格式
        self.msg = None
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s [第%(lineno)d行] 日志详情 ==== %(message)s'
        formatter = logging.Formatter(fmt)

        # 控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            # 文件渠道
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


# 是否需要写入文件
if conf.getboolean("log", "file_output"):
    FilePath = os.path.join(logger_dir, conf.get("log", "file_name"))
else:
    FilePath = None

logger = MyLogger(FilePath)

if __name__ == '__main__':
    # mlogger = MyLogger(config.get("log", "name"), file="auto_test_logger.txt")
    logger.info("测试，我自己封装的日志类！！！！")
