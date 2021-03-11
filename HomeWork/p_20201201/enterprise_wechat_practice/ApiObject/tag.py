import json

import requests

from HomeWork.p_20201201.enterprise_wechat_practice.utils.my_logger import logger

corpid = 'ww0ee834ff046152e5'
corpsecret = '3NfKAwov1WDqFvAa-ne5UMq2WPGXeNx8jfFc4ANUoY0'

proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888',
}


class Tag:

    def __init__(self):
        self.token = ""

    def get_token(self):
        r = requests.get(
            ' https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid': corpid, 'corpsecret': corpsecret}
        )
        logger.info(json.dumps(r.json(), ensure_ascii=False))
        self.token = r.json()['access_token']

    def list(self, p_group_id=None, p_tag_id=None):
        logger.info(self.token)
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={'access_token': self.token},
            json={"group_id": p_group_id, "tag_id": p_tag_id}
        )
        logger.info(f"获取企业标签库接口请求结果：{json.dumps(r.json(), ensure_ascii=False)}")
        return r

    def add(self, group_name, tags):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={'access_token': self.token},
            json={
                'group_name': group_name,
                'tag': tags
            },
            # proxies=proxies,
            verify=False
        )
        logger.info(json.dumps(r.json(), ensure_ascii=False))
        return r

    def delete(self, group_ids, tag_ids):
        if tag_ids is None:
            json_data = {
                'group_id': group_ids
            }
        else:
            json_data = {
                'tag_id': tag_ids,
                'group_id': group_ids
            }

        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.token},
            json=json_data,
            # proxies=proxies,
            verify=False
        )
        logger.info(f"删除企业客户标签接口请求结果：{json.dumps(r.json(), ensure_ascii=False)}")
        return r

    def update(self, tag_id, name, order_id=None):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={'access_token': self.token},
            json={
                "id": tag_id,
                "name": name,
                "order": order_id
            },
            proxies=proxies,
            verify=False
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def clear_all(self):
        r = self.list()
        group_ids = [group['group_id'] for group in r.json()['tag_group']]
        if len(group_ids) > 0:
            self.delete(group_ids, None)
            return self.list()
        else:
            return r
