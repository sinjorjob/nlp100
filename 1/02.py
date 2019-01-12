# coding: utf-8

str1 ="パトカー"
str2 ="タクシー"
result = ""

for i,j in zip(str1,str2):
    result = result + i + j


print('変換前str1={}'.format(str1))
print('変換前str2={}'.format(str2))
print('変換後={}'.format(result))
