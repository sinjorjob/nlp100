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


lines = get_json_data("イギリス").split("\n")  #改行で分割してリスト型変数へ格納
for line in lines:
    category_line = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", line)
    if category_line is not None:
        print(category_line.group(1))

"""
category_line.group(0) ではマッチした文字列全体
category_line.group(1) では最初にマッチした部分文字列
"""


