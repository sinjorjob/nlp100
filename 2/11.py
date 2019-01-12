# coding: utf-8


with open("hightemp.txt", encoding="utf-8") as f:
    contents = f.read()  #指定されたファイルを文字列として一括で読み込む．
    result = contents.replace("\t", "")

print('変換前')
print(contents)
print("=======================================================================")
print('変換後')
print(result)


