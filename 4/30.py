# coding: utf-8

from janome.tokenizer import Tokenizer
import janome


t = Tokenizer()

with open("neko.txt",encoding='utf-8') as f:
    for line in f:
        """
        形態素解析を実行
        streamをTrueとするとストリーミングモードとなり、リストではなくジェネレーターを返す。
        リスト全体を保持する必要がなくTokenを逐次的に処理する場合に使う。
        """
        for token in t.tokenize(line, stream=True):
            with open ('neko.txt.janome-01','a',encoding='utf-8') as f:
                f.write(str(token) + '\n')  #改行コードを付けて追記


"""
以下のように形態素解析されたデータファイルが生成される。


一	名詞,数,*,*,*,*,一,イチ,イチ
吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ
は	助詞,係助詞,*,*,*,*,は,ハ,ワ
猫	名詞,一般,*,*,*,*,猫,ネコ,ネコ
で	助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ
ある	助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル
。	記号,句点,*,*,*,*,。,。,。

"""              


