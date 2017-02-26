import sys
import os
import requests
import lxml.html
from bs4 import BeautifulSoup
from lxml.cssselect import CSSSelector
import urllib.request

#url = 'https://mynichinoken.jp/mynichinoken/index.php'
url = 'https://mynichinoken.jp/mynichinoken/login/mns0101_01.php'
student_url = 'https://mynichinoken.jp/mynichinoken/student/index.php'
curri_te_url = 'https://mynichinoken.jp/mynichinoken/student/m04/mns0401_02f.php?exam_date=20170219&exam_knd=N&yesr_val=2017&subject=K&odr=&type=&crct=&saiten=2'

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0'}
data = {'id':'N1207585','passwd':'keigo0604'}
session.post(url,headers=headers, data=data)

s = session.get(curri_te_url)
print(s.content)
root = lxml.html.fromstring(s.content)
#for td in root.cssselect('body > table > tbody > tr > td > table > tbody > tr > td'):
for td in root.cssselect('body > table > tbody > tr > td > table'):
  print(td)
  for t in td:
      print(t.text)
  print("----")

  print(td)
  for t in td:
      print(t.text)

