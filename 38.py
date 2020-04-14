import sys, MeCab, re,collections
import matplotlib.pyplot as plt,numpy as np
#38. ヒストグラム
#単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

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

numlis = list(basedic.values())
#ヒストグラム
from matplotlib import rcParams
plt.hist(numlis,bins=10,range = (1,10))
plt.show()