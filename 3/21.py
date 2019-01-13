# coding: utf-8

import json

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
    if "Category" in line:
        print(line)

"""
実行結果例

[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国]]
[[Category:海洋国家]]
[[Category:君主国]]
[[Category:島国|くれいとふりてん]]
[[Category:1801年に設立された州・地域]]

"""

