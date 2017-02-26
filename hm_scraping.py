import sys
import os
import requests
import lxml.html
import chardet
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
root = lxml.html.fromstring(s.content)

#for td in root.cssselect('body > table > tbody > tr > td > table > tbody > tr > td'):

tables = root.cssselect('html > body > table')
score_table = tables[2]
score_tables = score_table.cssselect('tbody > tr > td > table')
print(lxml.html.tostring(score_tables[1],encoding='unicode'))
trs = score_tables[1].cssselect('tr')
for tr in trs:
    tds = tr.cssselect('td')
    for td in tds:
        print(td.text)
        print(td.find('font').text)

