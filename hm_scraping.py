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
#curri_te_url = 'https://mynichinoken.jp/mynichinoken/student/m04/mns0401_02f.php?exam_date=20170219&exam_knd=N&yesr_val=2017&subject=K&odr=&type=&crct=&saiten=2'
curri_te_url = 'https://mynichinoken.jp/mynichinoken/student/m04/mns0401_02f.php?exam_date=20170219&exam_knd=N&yesr_val=2017&subject=M&odr=&type=&crct=&saiten=2'

def main():
  session = requests.Session()
  headers = {'User-Agent': 'Mozilla/5.0'}
  data = {'id':'N1207585','passwd':'keigo0604'}
  session.post(url,headers=headers, data=data)

  s = session.get(curri_te_url)
  root = lxml.html.fromstring(s.content)

  # Fetch summary table
  score_summary_table = root.cssselect('html > body > table')[1]
  extract_summary_score(score_summary_table)

  # Fetch score table
  score_table = root.cssselect('html > body > table')[2]
  each_score_tables = score_table.cssselect('tbody > tr > td > table')
  trs = each_score_tables[1].cssselect('tr')
  for tr in trs:
    extract_score(tr)

def extract_summary_score(score_summary_table):
    score_summary_tr = score_summary_table.cssselect('tbody > tr')[5]
    score_summary_td = score_summary_tr.cssselect('td')[0]
    print(lxml.html.tostring(score_summary_td, encoding='unicode'))
    for span in score_summary_td.cssselect('span'):
        print(lxml.html.tostring(span, encoding='unicode'))
    total = score_summary_td.findall('span')[0].text
    total_wrong_answer = lxml.html.tostring(score_summary_td.findall('span')[1], encoding='unicode')
    print(total,total_wrong_answer )
    c = score_summary_td.findall('span')[1].getchildren


def extract_score(tr):
    tds = tr.cssselect('td')
    if(tds[0].text != None):
      question_num = tds[0].text
      question_ctx = tds[1].text
      answer = tds[2].cssselect('font > b')[0].text
      correct_answer_per = tds[4].cssselect('font')[0].text
      wrong_answer_per = tds[5].cssselect('font')[0].text
      none_answer_per = tds[6].cssselect('font')[0].text


      print(question_num, question_ctx, answer, correct_answer_per,wrong_answer_per,none_answer_per )
#    for td in tds:
#      print(lxml.html.tostring(td, encoding='unicode'))



if __name__ == '__main__':
    main()