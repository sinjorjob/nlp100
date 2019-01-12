# coding: utf-8


with open("hightemp.txt", encoding="utf-8") as f:
    lines = f.readlines()


    col1_list=[]
    for row in lines:
        contents = row.split('\t')  #改行で分割
        col1 = contents[0]   #1列目の値を取得
        col1_list.append(col1)  #リストに1列目の情報を追記

result = set(col1_list)   #setで重複を排除

for i in result:
    print(i)




