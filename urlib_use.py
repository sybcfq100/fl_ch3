
'''import urllib.request

response = urllib.request.urlopen('https://python.org')
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
'''

'''
import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding = 'utf8')
response = urllib.request.urlopen('https://httpbin.org/post', data = data)
print(response.read())
'''

from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
        }
dict = {
    'name' : 'Germey'
    }
    
data = bytes(parse.urlencode(dict), encoding ='utf8')
req = request.Request(url=url, data = data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
