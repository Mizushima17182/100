import sys, MeCab, re,collections
import matplotlib.pyplot as plt,numpy as np
#37. 頻度上位10語
#出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

# 動詞の表層形をすべて抽出せよ．
# 表層形　基本形(原型)　品詞　品詞細分類
# lisdic{'surface': '吾輩', 'base': '吾輩', 'pos': '名詞', 'pos1': '代名詞'}
with open(r"C:\pythonr\100p\basetlist.txt", "rt", encoding="utf-8")as tangotxt:
    tango = tangotxt.read()
    tangolist = tango.split(",")

#print(tangolist)
baselist = []
result = ""
basedic = {}
for i in tangolist:
    if i in basedic:
        basedic[i] = basedic[i] + 1
    else:
        basedic[i] = 0
print(sorted(basedic.items(), key = lambda x:x[1],reverse=True)[0:18])


