# -*- coding: utf-8 -*-
import json
from urllib import quote

import requests
from hashlib import sha256
from config import BM_HOST, AGENT_NO, AGENT_KEY


class BasaltmatrixRequest(object):
    def __init__(self, api_url, params, files=None):
        self.url = BM_HOST.format(url=api_url)
        self.params = params
        self.signature = self.__data_sign()
        self.headers = {
            "agent-no": AGENT_NO,
            "signature": self.signature
        }
        self.files = files

        print self.url
        print json.dumps(self.params, ensure_ascii=False, indent=2)
        print json.dumps(self.headers, ensure_ascii=False, indent=2)

    def get(self):
        r = requests.get(self.url, params=self.params, headers=self.headers, verify=False)
        print r.content
        return r

    def post(self):
        r = requests.post(self.url, data=self.params, headers=self.headers, files=self.files, verify=False)
        print r.content
        return r

    def put(self):
        r = requests.put(self.url, data=self.params, headers=self.headers, files=self.files, verify=False)
        print r.content
        return r

    def delete(self):
        import urllib
        r = requests.delete(self.url + '?' + urllib.urlencode(self.params), headers=self.headers, verify=False)
        print r.content
        return r

    def __format_code(self, x):
        """ 处理编码问题, 兼容unicode, int和 float
        """
        if isinstance(x, unicode):
            return quote(x.encode("utf-8"), safe="")
        elif isinstance(x, (float, int)):
            return str(x)
        else:
            return quote(x, safe="")

    def __data_sign(self):

        # 按照key的拼音排序成key=value形式
        signature_str = "&".join((
            "=".join(map(self.__format_code, i)) for i in sorted(self.params.items())
        ))
        # 用 utf-8 编码
        signature_str = signature_str.encode("utf-8")
        signature_str += AGENT_KEY
        signature = sha256(signature_str).hexdigest()
        return signature
