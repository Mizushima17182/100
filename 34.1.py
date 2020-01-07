import sys, MeCab, re
# 34. 「AのB」 
#2つの名詞が「の」で連結されている名詞句を抽出せよ．
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
# 表層形　基本形(原型)　品詞　品詞細分類

# 動詞の表層形をすべて抽出せよ．
# 表層形　基本形(原型)　品詞　品詞細分類
# lisdic{'surface': '吾輩', 'base': '吾輩', 'pos': '名詞', 'pos1': '代名詞'}
with open(r"C:\pythonr\100p\neko.txt.mecab", "rt", encoding="utf-8")as mecab_txt:
    txt_neko = mecab_txt
    nekolist = []
    cou = 0
    for tline in txt_neko.readlines():  # 一行ずつ読み込み
        #print(tline)
        stline = re.split(",|\t", tline)  # 単語ずつ切る
        #print("一行", stline)
        nekodict = {"surface":"","base":"","pos":"","pos1":""}
        coukey = 0
        for stword in stline:  # 人単語ずつ読み込む
            #print("一単語", stword)
            if coukey == 0:  # 一つ目は表層形へ
                nekodict["surface"] =  stword
                coukey = coukey + 1
            elif coukey == 1:  # 二つ目は品詞
                nekodict ["pos"] = stword
                coukey = coukey + 1
            elif coukey == 2:  # 三つめは品詞詳細分類
                nekodict["pos1"] = stword
                coukey = coukey + 1
            elif coukey == 7:  # 7つめの原形は基本形
                nekodict["base"]= stword
                coukey = coukey + 1
            else:
                coukey = coukey + 1
        nekolist.append(nekodict)
        cou = cou + 1
        #if cou == 10:
            #break
#こっから34　itemsでkeyとvalueとって、posが動詞だった場合にsurfaceをkeyとしたvalueを取り出す
cou = 0
pata = ".+の.+"
ABlist = []
result = ""
for i in nekolist:
    for dick,dicv in i.items():
            #print(dick,dicv)
            if dicv == "名詞"  : #名詞を取り出して、「AのB」を正規表現で探す
                #print(i["base"]) #i["surfacfe"],i
                result=re.search(pata, i["base"])
                if result is not None:
                    ABlist.append(result.group())
                    
                    print(result.group(),i)
                    

