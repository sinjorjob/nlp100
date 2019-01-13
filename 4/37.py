# coding: utf-8
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

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

lst_words = [] 
lst_count = []

"""
result[0:10]の結果
[{'の': 9194},
 {'。': 7486},
 {'て': 6865},
 {'、': 6772},
 {'は': 6420},
 {'に': 6239},
 {'を': 6067},
 {'と': 5505},
 {'が': 5336},
 {'た': 3988}]

 """


for i in result[0:10]:
    # resultから不要な文字列[ { ' } ]と空白を排除して単語とカウント値に分割 
    key, cnt = str(i).strip('{').strip('}').replace("'","").replace(" ","").split(':')
    lst_words.append(key)
    lst_count.append(int(cnt))   #グラフ化するためにint型に変換


#グラフ描画
import matplotlib.pyplot as plt
import japanize_matplotlib

fig, ax = plt.subplots()
fig.suptitle("出現頻度が高い10語とその出現頻度")
x = lst_words
y = lst_count
ax.bar(x,y)
plt.show()




