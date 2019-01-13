# coding: utf-8
# サ変接続の名詞をすべて抽出せよ．
# 品詞細分類1がサ変接続のものを探す。

from janome.tokenizer import Tokenizer
import janome

#ファイルを整形する。
# 形態素はタブ区切り、品詞等の分類はカンマ区切りなので以下の形式に整形したファイルを生成する。


with open ('neko.txt.janome-01','r',encoding='utf-8') as f:
    text = f.readlines()

lst_janome=[]
for line in text:
    lst_janome.append(
        { 'surface': line.split('\t')[0], # 表層形
          'pos'    : line.split('\t')[1].split(',')[0], # 品詞
          'pos1'   : line.split('\t')[1].split(',')[1], # 品詞細分類1
          'base'   : line.split('\t')[1].split(',')[6]   # 基本形
        })


"""
lst_janomeには以下のようなリストデータが生成される

{'surface': '一', 'pos': '名詞', 'pos1': '数', 'base': '一'}
{'surface': '吾輩', 'pos': '名詞', 'pos1': '代名詞', 'base': '吾輩'}
{'surface': 'は', 'pos': '助詞', 'pos1': '係助詞', 'base': 'は'}
{'surface': '猫', 'pos': '名詞', 'pos1': '一般', 'base': '猫'}
{'surface': 'で', 'pos': '助動詞', 'pos1': '*', 'base': 'だ'}
{'surface': 'ある', 'pos': '助動詞', 'pos1': '*', 'base': 'ある'}

"""

#品詞細分類1がサ変接続の値だけを取得(pos1='サ変接続')

result = []
for row in lst_janome:
    if row['pos1']=='サ変接続':
        result.append(row['base'])


#10件だけ表示
print(result[:10:])

"""

実行結果

['見当', '記憶', '話', '装飾', '突起', '運転', '記憶', '分別', '決心', '我慢']

"""