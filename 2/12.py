# coding: utf-8



with open("hightemp.txt", encoding="utf-8") as f:
    lines = f.readlines()

    for row in lines:
        contents = row.split('\t')  #改行で分割
        col1 = contents[0]   #1列目の値を取得
        col2 = contents[1]   #2列目の値を取得

        with open("col1.txt", "a") as f1:
            f1.write("{}\n".format(col1))  #col1を追記で書き込む

        with open("col2.txt", "a") as f2:
            f2.write("{}\n".format(col2))  #col2を追記で書き込む
            
