import sys
import os
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import urllib.request

url = 'https://mynichinoken.jp/mynichinoken/index.php'
#url = 'https://www.google.co.jp/'
#browser = RoboBrowser(parser='html.parser')
#browser.open(url)  # open()メソッドでGoogleのトップページを開く。

html = urllib.request.urlopen(url).read()
print(html)
soup = BeautifulSoup(html, 'lxml')
print(soup)