import urllib.request


s = urllib.request.urlopen('http://www.baidu.com')
print(s)
d = s.read()
print(d)
# urllib.request.urlopen('www.baidu.com')
