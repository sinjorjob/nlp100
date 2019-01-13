# coding: utf-8

import json
import re


def get_json_data(word):
    
    with open("jawiki-country.json",encoding='utf-8') as f:
        article_json = f.readline()  #1行読み込み
        while article_json:
            article_dict = json.loads(article_json)  #辞書型でロード
            if article_dict["title"] == word:
                return article_dict["text"]
            else:
                article_json = f.readline()    #次の要素をロード
        
    return ""


temp_dict = {}
lines = get_json_data("イギリス").split("\n")  #改行で分割してリスト型変数へ格納
for line in lines:
    temp_line = re.search("^(.*?)\s=\s(.*)", line, re.S)
    if temp_line is not None:
        temp_dict[temp_line.group(1)] = re.sub("'{2,5}", "", temp_line.group(2))


for k, v in sorted(temp_dict.items(), key=lambda x: x[1]):
    print(k, v)

