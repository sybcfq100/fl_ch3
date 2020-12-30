# -*- coding: utf-8 -*-
"""
@Time        : 14/12/2020
@Author      : sybcf
@File        : strkeydict0
@Description : 

class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return  self[str(key)]

    def get(selfself, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

def __contains__(self, key):
    return key in self.keys() or str(key) in self.keys()
"""
from urllib import request, parse


url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla / 4.0 (compatible; MSIE 5.5; Widows NT)', \
    'Host': 'httpbin.org'
}
dict = {'name': 'Germey'}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data =data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))