import http.cookiejar, urllib.request
'''
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.bilibili.com')
for item in cookie:
    print(item.name+"="+item.value)
'''

'''
filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://bilibili.com')
cookie.save(ignore_discard=True, ignore_expires=True)
'''

'''
from urllib import request, error

try:
    response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
'''

from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)
