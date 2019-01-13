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
    file_line = re.search("(File|ファイル):(.*?)\|", line)
    if file_line is not None:
        print(file_line.group(2))


"""
【正規表現の概要】

"(File|ファイル):(.*?)\|"
^で始まり$で終わる。
(File|ファイル) : File or ファイルに該当する。
(.*?): 任意の文字列と最短一致
\| : |で終わる。

"""

