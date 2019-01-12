# coding: utf-8

import sys
import math

N = int(sys.argv[1])  #引数(分割する行数）を取得してint型に変換
with open("hightemp.txt",encoding='utf-8') as f:
    lines = f.readlines()  #リスト型で全体を読み込む
    num_of_line =  int((len(lines)/N))


if (len(lines)/N) != 0:  #割り切れない場合は分割ファイル数を＋１する。
    for i in range(N+1):
        with open("split%s.txt" % str(i), "w") as w:
            w.writelines(lines[num_of_line * i: num_of_line * (i + 1)])

else:
    for i in range(N):
        with open("split%s.txt" % str(i), "w") as w:
            w.writelines(lines[num_of_line * i: num_of_line * (i + 1)])










            
