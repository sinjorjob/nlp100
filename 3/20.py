# coding: utf-8

import json

with open("jawiki-country.json",encoding='utf-8') as f:
    article_json = f.readline()  #1行読み込み
    while article_json:
        article_dict = json.loads(article_json)  #辞書型でロード
        if "イギリス" in article_dict["title"]:
            print(article_dict["text"])

        article_json = f.readline()    #次の要素をロード
