import os
import json

# if not os.path.exists("data/rawdata.json"):
#     #text =[Preprocessing(line).split() for line in f]
#     text = ['easi', 'know', 'want', 'stay']
#     print(type(text))
#     with open('data/rawdata.json', 'w') as f:
#         json.dump(text, f)
#
#     with open("data/rawdata.json", 'r') as f:
#         texts = print(json.load(f))
#     f.close()

text = ['easi', 'know', 'want', 'stay']
print(type(text))
with open('rawdata.json', 'w') as f:
    json.dump(text, f)

with open("rawdata.json", 'r') as f:
    texts = json.load(f)
    print(texts)
f.close()