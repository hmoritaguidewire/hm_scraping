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

test_dates = [20170219, 20170305]
print(Subject.M.to_japanese())
for test_date, subj in itertools.product(test_dates, Subject):
    curri_te_url = 'https://mynichinoken.jp/mynichinoken/student/m04/mns0401_02f.php?exam_date=' + str(test_date) + '&exam_knd=N&yesr_val=2017&subject=' + subj.name + '&odr=&type=&crct=&saiten=2'
    print(curri_te_url)