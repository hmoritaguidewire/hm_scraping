import sys
import os
import requests
import lxml.html
from bs4 import BeautifulSoup
import urllib.request

#url = 'https://mynichinoken.jp/mynichinoken/index.php'
url = 'https://mynichinoken.jp/mynichinoken/login/mns0101_01.php'
student_url = 'https://mynichinoken.jp/mynichinoken/student/index.php'
session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0'}
data = {'id':'N1207585','passwd':'keigo0604'}
session.post(url,headers=headers, data=data)
s = session.get(student_url)
print(s.content)
root = lxml.html.fromstring(s.content)
print(root)

#html = urllib.request.urlopen(url).read()
#print(html)
#soup = BeautifulSoup(html, 'lxml')
#print(soup)
#for field in soup.find_all(name='input'):
#    print(field)
#    n = field.get('name')
#    print(n)
