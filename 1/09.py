# coding: utf-8

import random

str ="I couldn't believe that I could actually understand what I was reading :\
 the phenomenal power of the human mind ."


str1 = str.split()

result = []


for word in str1:
    if len(word) > 4:

        first = word[0:1]  #先頭文字を取得
        last = word[-1]    #最後尾の文字を取得
        word_list = list(word) #shuffleを利用するために中間文字列をリスト型に変換
        middle = word_list[1:-1] #上記以外の文字を取得
        random.shuffle(middle)   #シャッフル
        word = first + "".join(middle) + last  #文字の結合
        
    else:
        pass
    
    result.append(word)


print('対象文字={}'.format(str1))
print('変換結果={}'.format(result))
