# coding: utf-8

import sys

N = int(sys.argv[1])  #引数(表示する行数）を取得してint型に変換
with open("hightemp.txt",encoding='utf-8') as f:
    lines = f.readlines()  #リスト型で全体を読み込む


for line in lines[-N:]:  # 末尾からN行目までを読み込む。
    print(line)
           
