# coding: utf-8


with open("hightemp.txt", encoding="utf-8") as f:
    lines = f.readlines()  #1行ごとの文字列のリストとして一括で読み込む

print('行数＝{}'.format(len(lines)))
