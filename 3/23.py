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
    selection_line = re.search("^(=+)\s*(.*?)\s*(=+)$", line)
    if selection_line is not None:
        print(selection_line.group(0), len(selection_line.group(1)) - 1)


"""
【正規表現の概要】

^(=+)\s*(.*?)\s*(=+)$
^で始まり$で終わる。
(=+) : =が1回以上
\s* : 空白が0回以上
(.*?): 任意の文字列と最短一致

【実行例】

==国名== 1
==歴史== 1
==地理== 1
===気候=== 2
==政治== 1
==外交と軍事== 1
==地方行政区分== 1
===主要都市=== 2
==科学技術== 1
==経済== 1
===鉱業=== 2
===農業=== 2
===貿易=== 2
===通貨=== 2
===企業=== 2
"""

