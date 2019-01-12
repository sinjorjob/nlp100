# coding: utf-8

import sys
from collections import defaultdict


count_dict = defaultdict(int)


with open("hightemp.txt", encoding="utf-8") as f:

    line = f.readline()  #1行読み込む。

    while line:
        count_dict[line.split()[0]] += 1   #1列目の値をsplitで取得してcount_dictのカウントを＋１する。
        line = f.readline()  #次の行を読み込む。


    """ NO18と同様にlambda関数とsortedを組み合わせてcount_dictの値でソート。
    reverse=Trueで降順指定。
    x[1]で辞書の値を指定。
    """
for k, v in sorted(count_dict.items(), key=lambda x: x[1], reverse=True):
    print(k,v)     


 