#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2021/2/25 7:59
# FileName: rewrite_xueqiu.py

import json

from mitmproxy import http


def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 拿到响应数据，转化成为python对象
        resp_data = json.loads(flow.response.content)
        # 修改对应的字段值
        resp_data["data"]["items"][1]["quote"]["name"] *= 2
        resp_data["data"]["items"][2]["quote"]["name"] = ''
        # 把修改后的数据，转为字符串，赋值给原始响应数据
        flow.response.text = json.dumps(resp_data)
