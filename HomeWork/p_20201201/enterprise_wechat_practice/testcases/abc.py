#!/usr/bin/env python

# Author  : Allen Bright
# Time    : 2021/3/11 6:39
# FileName: abc.py
from pprint import pprint

import requests

url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?access_token=-GN-b8y6P3kGxanxebU6hwIgC0icmhM_Qc4sCTC0xFJDbnpGVg2qK-1Qk3eP1V3Cxl5cbgeEMj1-eysIxNDJskQZtl79XvnvYkWWfGS6b5VseB5AJNBM4oU5WkascgCnYVpNA3e97j07H09RsIfOoBhRO9jcMAkWh7vw8kEqGhk_tAnzJOrwCEmsJ_b81m3ljJbP_Axor2ACWCNsPHptnA"

# payload = "{\r\n    \"group_id\": [\"etyobcDwAAPZO1sv3PtVUzFEE62fgSiA\"],\r\n    \"tag_id\": []\r\n}"
# payload = {'group_id': ['etyobcDwAAPZO1sv3PtVUzFEE62fgSiA'], 'tag_id': []}
payload = {'group_id': ['etyobcDwAAPZO1sv3PtVUzFEE62fgSiA'], 'tag_id': []}
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, json=payload)

pprint(response.json())
