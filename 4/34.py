# coding: utf-8
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．

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

# i番目のbaseが'の'の前後の要素[i-1, i+1]のposの値が両方'名詞'の3要素を抜き出して結合する。
result = []
for i,row in enumerate(lst_janome):
    if row['base']=='の':
        if lst_janome[i-1]['pos'] =='名詞' and lst_janome[i+1]['pos']=='名詞':
            result.append(lst_janome[i-1]['base'] + row['base'] + lst_janome[i+1]['base'])


#10件だけ表示
print(result[:10:])
print(len(result))
"""

実行結果

['彼の掌', '掌の上', '書生の顔', 'はずの顔', '顔の真中', '穴の中', '書生の掌', '掌の裏', '何の事', '肝心 の母親']
6043

"""