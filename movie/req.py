import requests
import os
import random
import time
import requests_cache
from bs4 import BeautifulSoup


requests_cache.install_cache('demo_cache')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 '
                         'Firefox/57.0'}

response = requests.get("http://www.dy2018.com/html/gndy/dyzz/index.html")  # , headers=headers
html_doc = response.content.decode('gbk')
# print(html_doc)
with open('m.txt','w') as f:
	f.write(html_doc)

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup)
links = []
for a in soup.select('.ulink'):  # 类查找
	# print(type(a))
	href = 'http://www.dy2018.com' + a['href']
	title = a.string
	links.append(href)
# print(href, title)

for link in links:
	response = requests.get(link, headers=headers)
	html_doc = response.content.decode('gbk')
	# print(html_doc)
	soup = BeautifulSoup(html_doc, 'html.parser')
	print(soup)
	ftp_element = soup.select('#Zoom table a')  # id查找+标签
	print(ftp_element)
	download_link = ftp_element[1]['href']
	# print(download_link)
	time.sleep(random.randint(1, 2))
	print()
