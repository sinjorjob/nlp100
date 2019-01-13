# coding: utf-8
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

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

continuous_word = []  #名詞が連続したWordのIndex番号をリスト形式で格納
pre_word = [] # 一つ前に一致したもの

for i, item  in enumerate(lst_janome):
    if item['pos']=='名詞':
        temp = []
        temp.append(i)  # 取得した情報が名詞ならIndex値（場所）を記録しておく
        j = i + 1
        while lst_janome[j]['pos'] == "名詞": # 次の要素が名詞である限りtempにIndex値を記録し続ける。
            temp.append(j)   #要素のIndex情報を追記する。
            j += 1
    
        wordlen = len(temp) # 現在チェックしている連続名詞が何連続かをチェック
        flag = False # 連続した名詞としてcontinuous_wordリストに追加するか否かのflag
        if wordlen >= 2: # 2連続以上ならcontinuous_wordへ追加する。
            flag = True
            for i in temp:
                 if i in pre_word: # pre_wordには、一つ前に抽出した単語が入っていて3連続以上した場合pre_wordで抽出したものと内容が
                              # 被ってしまうことがあるので、その場合はflagをFalseにしてcontinuos_wordへの追加を除外。
                    flag = False
                    break # 1つでも被っているものがあれば、for loopから抜ける。
            
        if flag is True: # flagがTrueのときのみcontinuous_wordに追加する
            continuous_word.append(temp) 
            
        pre_word = temp    # pre_wordに現在しらべているIndex情報をセット



# これで continuos_wordには1以上の連続した名詞のlst_janomeのIndex情報がリスト形式で格納される。
# continuos_wordを使ってlst_janomeから単語情報を抽出する。

result = []
for item in continuous_word:
    temp = []
    for i in item:
        temp.append(lst_janome[i]["surface"])
    
    if len("".join(temp)) > 1:
        result.append("".join(temp))    
      
#10件だけ表示
print(result[1:20])

