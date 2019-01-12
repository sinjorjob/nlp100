# coding: utf-8


with open("col1.txt", "r") as f1:
    lines_1 = f1.readlines()    #リスト形式で全体を読み込む
    with open("col2.txt", "r") as f2:
       lines_2 = f2.readlines()   #リスト形式で全体を読み込む

       result = []
       for row1, row2 in zip(lines_1, lines_2):  #2つのファイルを1要素ずつ取り出す
           row = row1.strip() +"\t" + row2       #col1は改行コードを削除し、Tabコードを追記してro2と結合
           result.append(row) 


with open("col12.txt", "a") as f:
    for row in result:
        f.write(row)  #col12を追記で書き込む




            
