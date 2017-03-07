import sys
import os
import requests
import lxml.html
from bs4 import BeautifulSoup
from lxml.cssselect import CSSSelector
import urllib.request
import re
import xlwt
from enum import Enum
import itertools

class Subject(Enum):
    K = 0 # 国語
    M = 1 # 算数
    R = 2 # 理科
    S = 3 # 社会

    def to_japanese(self):
        japanese = ['国語', '算数', '理科', '社会']
        return japanese[self.value]

#url = 'https://mynichinoken.jp/mynichinoken/index.php'
url = 'https://mynichinoken.jp/mynichinoken/login/mns0101_01.php'
student_url = 'https://mynichinoken.jp/mynichinoken/student/index.php'
xls_file = 'C:\\tmp\\sample.xls'

test_dates = [20170305]

def main():
  session = requests.Session()
  headers = {'User-Agent': 'Mozilla/5.0'}
  data = {'id':'N1207585','passwd':'keigo0604'}
  session.post(url,headers=headers, data=data)

  book = xlwt.Workbook()

  for test_date, subj in itertools.product(test_dates, Subject):
    curri_te_url = 'https://mynichinoken.jp/mynichinoken/student/m04/mns0401_02f.php?exam_date=' + str(test_date) + '&exam_knd=N&yesr_val=2017&subject=' + subj.name + '&odr=&type=&crct=&saiten=2'
    print(curri_te_url)
    sheet_name = str(test_date) + '-' + subj.to_japanese()
    print('Create sheet..' + sheet_name)
    sheet = book.add_sheet(sheet_name)

    sheet.write(0, 0, test_date)
    sheet.write(0, 1, subj.to_japanese())
    sheet.write(0, 2, curri_te_url)

    s = session.get(curri_te_url)
    root = lxml.html.fromstring(s.content)

    # Fetch summary table
    score_summary_table = root.cssselect('html > body > table')[1]
    summary_score, summary_wrong_score, summary_noanswer = extract_summary_score(score_summary_table)
    print(summary_score, summary_wrong_score, summary_noanswer)

    sheet.write(2, 0, summary_score)
    sheet.write(2, 1, summary_wrong_score)
    sheet.write(2, 2, summary_noanswer)

    # Fetch score table
    score_table = root.cssselect('html > body > table')[2]
    each_score_tables = score_table.cssselect('tbody > tr > td > table')
    trs = each_score_tables[1].cssselect('tr')
    answers = []
    for tr in trs:
      question_num, question_ctx, answer, correct_answer_per, wrong_answer_per, none_answer_per = extract_score(tr)
      print(question_num, question_ctx, answer, correct_answer_per,wrong_answer_per,none_answer_per)
      answers.append([question_num, question_ctx, answer, correct_answer_per, wrong_answer_per, none_answer_per])

    for i in range(len(answers)):
        sheet.write(i+3, 0, answers[i][0])
        sheet.write(i+3, 1, answers[i][1])
        sheet.write(i+3, 2, answers[i][2])
        sheet.write(i+3, 3, answers[i][3])
        sheet.write(i+3, 4, answers[i][4])
        sheet.write(i+3, 5, answers[i][5])

    book.save(xls_file)

def extract_summary_score(score_summary_table):
    score_summary_tr = score_summary_table.cssselect('tbody > tr')[5]
    score_summary_td = score_summary_tr.cssselect('td')[0]
    print(lxml.html.tostring(score_summary_td, encoding='unicode'))

    score_r = re.compile('(\d+)点')
    summary_scores = score_summary_td.cssselect('span')
    # <span class="ore">【　70点　】</span> -> 70
    summary_score = score_r.findall(summary_scores[0].text)[0]

    # <span class="sgo1"><br>誤答(×)47点<br>無答(レ)33点</span> -> 47
    wrong_and_noanswer = lxml.html.tostring(summary_scores[1], encoding='unicode')
    summary_wrong_score = score_r.findall(wrong_and_noanswer)[0]

    # <span class="sgo1"><br>誤答(×)47点<br>無答(レ)33点</span> -> 35
    summary_noanswer = score_r.findall(wrong_and_noanswer)[1]

    return [summary_score, summary_wrong_score, summary_noanswer]

def extract_score(tr):
    tds = tr.cssselect('td')
    if(tds[0].text != None):
      question_num = tds[0].text
      question_ctx = tds[1].text
      answer = tds[2].cssselect('font > b')[0].text
      correct_answer_per = tds[4].cssselect('font')[0].text
      wrong_answer_per = tds[5].cssselect('font')[0].text
      none_answer_per = tds[6].cssselect('font')[0].text
      return [question_num, question_ctx, answer, correct_answer_per,wrong_answer_per,none_answer_per]
    else:
      return['','','','','','']


if __name__ == '__main__':
    main()