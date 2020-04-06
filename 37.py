import sys, MeCab, re,collections
import matplotlib.pyplot as plt,numpy as np
#37. 頻度上位10語
#出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

# 動詞の表層形をすべて抽出せよ．
# 表層形　基本形(原型)　品詞　品詞細分類
# lisdic{'surface': '吾輩', 'base': '吾輩', 'pos': '名詞', 'pos1': '代名詞'}
with open(r"C:\pythonr\100p\tangolist3.txt", "rt", encoding="utf-8")as tangotxt:
    tango = tangotxt.read()
    tangolist = tango.split(",")

#print(tangolist)
baselist = []
result = ""

#簡単な方法 counter　
from collections import Counter
cou = 0
coubaselist = Counter(tangolist)
left = []
height = []
for coubacemost in coubaselist.most_common(10):
    for i in coubacemost:
        if cou == 0:
            left.append(i)
            cou = 1
        else:
            height.append(i)
            cou = 0

#グラフ
from matplotlib import rcParams
plt.bar(left,height)
plt.xlabel('頻出単語')
#print(left)
plt.show()