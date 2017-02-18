import json

cities = [
    {'rank': 1, 'city': '上海', 'population': 24150000},
    {'rank': 2, 'city': 'カラチ','population':  23550000},
    {'rank': 3, 'city': '北京', 'population': 21510000},
    {'rank': 4, 'city': '天津', 'population': 214720000},
    {'rank': 5, 'city': 'イスタンブール', 'population': 14602000}
]

print(json.dumps(cities, ensure_ascii=False, indent=2))
file_name = 'C:\\tmp\\top_cities.json'
with open(file_name, 'w', encoding='utf-8-sig') as f:
    print(json.dump(cities, f, ensure_ascii=False, indent=2))
