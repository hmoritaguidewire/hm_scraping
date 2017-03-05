import re
score = '【　70点　】 '
score_non = '<span class="sgo1"><br>誤答(×)47点<br>無答(レ)33点</span>'

score_r = re.compile('(\d+)点')
result = score_r.findall(score)
print(result)
result_non = score_r.findall(score_non)
print(result_non)
