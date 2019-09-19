from xml.dom import minidom
import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))

doc = minidom.parse(f'{dir_path}/russia.svg')
path_ids = [path.getAttribute('id') for path in doc.getElementsByTagName('path')]
path_titles = [path.getAttribute('title') for path in doc.getElementsByTagName('path')]
path_d = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
doc.unlink()

regions = {}

for key, val in zip(path_ids, path_titles):
    regions[key]={'name':val, 'person': 'null', 'place': 'null', 'animal':'null', 'resource': 'null'}
for key, d in zip(path_ids, path_d):
    regions[key].update({'d': d})

with open(f'{dir_path}/regions.json', 'w', encoding="utf-8") as file:
    json.dump(regions ,file, indent=4, ensure_ascii=False)