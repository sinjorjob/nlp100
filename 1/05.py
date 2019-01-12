# coding: utf-8

input = "I am an NLPer"

def ngram(input, n):
    # 最終Index位置を取得
    last = len(input) - n + 1
    ret = []
    #0～lastに対してn個の要素を取得
    for i in range(0, last):
        ret.append(input[i:i+n])
    return ret


print("=====================================================================================")
print('変換対象str={}'.format(input))
print("=====================================================================================")
print("2文字まで考慮する文字n-gram")
print(ngram(input, 2))              # 2文字まで考慮する n-gram
print("=====================================================================================")
print("2単語まで考慮する単語n-gram")
input = input.split()
print(ngram(input, 2))           # 2単語まで考慮する単語 n-gram        