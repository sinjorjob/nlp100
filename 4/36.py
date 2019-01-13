# coding: utf-8
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

from janome.tokenizer import Tokenizer
import janome
from collections import defaultdict

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

count_dict = defaultdict(int)


for row in lst_janome:
    count_dict[row['surface']] += 1   #該当単語のcount_dictのカウントを＋１する。
    

    """ 
    lambda関数とsortedを組み合わせてcount_dictの値でソート。
    reverse=Trueで降順指定。
    x[1]で辞書の値を指定。
    """

result = []
for k, v in sorted(count_dict.items(), key=lambda x: x[1], reverse=True):
    result.append({k:v})

print(result[:10:])


#======================================================================================
#もう1つの方法（collectionオブジェクトを使うと楽）
#======================================================================================

import collections

lst_tmp = []
for janome in lst_janome:
    lst_tmp.append(janome['surface'])  #単語リストを生成

words_frq = collections.Counter(lst_tmp).most_common()  

print(words_frq[0:10]) #10件表示

"""
counterの例

 Counter('abracadabra').most_common(3)  
　→　[('a', 5), ('r', 2), ('b', 2)]

最も多い n 要素を、カウントが多いものから少ないものまで順に並べたリストを返します。 
n が省略されるか None であれば、 most_common() はカウンタの すべての 要素を返します。
等しいカウントの要素は任意に並べられます:
"""
