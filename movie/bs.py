from bs4 import BeautifulSoup
import requests
import time
import re


def dicout(dic):
	for key in dic:
		print(key, '  >  ', dic[key])
		print()


def write(filename, con):
	with open(filename, 'w') as f:
		f.write(con)


def req_bs(url):
	'''获取网页 bs处理'''
	res = requests.get(url)
	con = res.content.decode('gbk')
	soup = BeautifulSoup(con, 'html.parser')
	return soup


'''获取子链接'''


def get_dlink(url):
	soup = req_bs(url)
	atags = soup.findAll('a')
	# print(atags)
	px = dict()
	for a in atags:  # not 'html' in a.get('href') and not 'php' in a.get('href') and len(a.get('href')) > 5
		x = str(a).split(']')[-1]
		if a.get('href')[0] == ('f' or 'm'):
			px[x] = a.get('href')
	dicout(px)


if __name__ == '__main__':
	url = 'http://www.dy2018.com'
	soup = req_bs(url)
	# m = r'*com^/'
	# a = 'com/123'
	# print(re.match(m, a))
	# exit(0)
	# 获取第一层链接
	atags = soup.findAll('a')
	# print(atags)
	p1 = dict()
	for a in atags:
		h = a.get('href')
		if 'html' in h:
			if h[0] == '/':
				p1[a.string] = url + h
			elif h[:4] == 'http':
				p1[a.string] = h
			else:
				p1[a.string] = url + '/' + h

	# get_dlink('http://www.dy2018.com/i/98668.html')
	for k in p1:
		print(p1[k])
		get_dlink(p1[k])
		# time.sleep(1)
		break
