# coding: utf-8

str1 = "paraparaparadise"
str2 = "paragraph"


def ngram(input, n):
    # 最終Index位置を取得
    last = len(input) - n + 1
    ret = []
    #0～lastに対してn個の要素を取得
    for i in range(0, last):
        ret.append(input[i:i+n])
    return ret

"""
ngram(str1,2)だと重複した要素を含むのでset（）をかますことで重複を排除する。
['pa', 'ar', 'ra', 'ap', 'pa', 'ar', 'ra', 'ap', 'pa', 'ar', 'ra', 'ad', 'di', 'is', 'se']

set(ngram(str1,2)) 
{'ap', 'pa', 'ar', 'ad', 'di', 'se', 'is', 'ra'}
"""
X = set(ngram(str1, 2))
Y = set(ngram(str2, 2))

print('和集合={}'.format(X.union(Y)))
print('積集合={}'.format(X.intersection(Y)))
print('差集合={}'.format(X.difference(Y)))



    