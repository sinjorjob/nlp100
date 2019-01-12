# coding: utf-8


with open("hightemp.txt", encoding="utf-8") as f:
    lines = f.readlines()


    """ x.split()[2]で3列目の情報を取得
    lambda関数とsortedを組み合わせて3列目でソート。
    reverse=Trueで降順指定。
    """

    for line in sorted(lines, key=lambda x: x.split()[2],reverse=True):
        print(line)






