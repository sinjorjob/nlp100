# coding: utf-8

str1 ="Hi He Lied Because Boron Could Not Oxidize Fluorine. \
New Nations Might Also Sign Peace Security Clause. Arthur King Can."

str2 = str1.replace('.',"")
str2 = str2.split()

dict = {}
target = [1, 5, 6, 7, 8, 9, 15, 16, 19]


"""
変数.idnex('要素')で指定した要素がリストの何番目の要素かを返す。
element[:1]で要素の先頭から1文字だけを抽出
dictにはKeyとして取り出した1文字を、値に取り出したIndex番号+1をセット（リストのIndexは０からはじまるため。
"""
for element in str2:
    if str2.index(element) in target:
        dict[element[:1]] = str2.index(element) + 1
    else:
        dict[element[:2]] =str2.index(element) + 1



print("=====================================================================================")
print('変換前str={}'.format(str1))
print("=====================================================================================")
print('単語抽出後str={}'.format(str2))
print("=====================================================================================")
print('処理結果={}'.format(dict))

