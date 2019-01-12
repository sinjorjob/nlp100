# coding: utf-8

# 出典: Wikipedia 英語版 "Atbash" より
str = "My favorite programming language is pythno."


#  if~elseは「ret += chr(219-ord(char)) if char.islower() else char」としてもよい。
def cipher(input):
    ret = ""
    for char in input:
        if char.islower():
            ret += chr(219 - ord(char))
        else:
            ret += char
    return ret

print('暗号化前={}'.format(str))
str = cipher(str)
print('暗号化後={}'.format(str))
str = cipher(str)
print('複合化後={}'.format(str))
