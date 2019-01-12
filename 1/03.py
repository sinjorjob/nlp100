# coding: utf-8

str1 ="Now I need a drink, alcoholic of course, after the heavy\
 lectures involving quantum mechanics."

str2 = str1.replace('.',"")
str2 = str2.replace(',',"")
str2 = str2.split()

"""strにはリスト形式で単語が格納されている状態
['Now', 'I', 'need', 'a', 'drink', 'alcoholic', 'of' ・・・・]
"""

#文字数はstrの要素毎にlen(str[i])でカウントすればいい。
result = []
for word in str2:
    result.append(len(word))
    

print('変換前str={}'.format(str1))
print('変換後str={}'.format(str2))
print('単語数のリスト={}'.format(result))

