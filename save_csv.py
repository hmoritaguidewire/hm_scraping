import csv

file_name = 'C:\\tmp\\top_cities.csv'

with open(file_name, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['rank', 'city', 'population'])
    writer.writerows([
        [1, '上海', 24150000],
        [2, 'カラチ', 23550000],
        [3, '北京', 21510000],
        [4, '天津', 214720000],
        [5, 'イスタンブール', 14602000],
    ])

