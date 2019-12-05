import sys, MeCab, re

# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
# 表層形　基本形(原型)　品詞　品詞細分類

with open("neko.txt.mecab", "rt", encoding="utf-8")as mecab_txt:
    txt_neko = mecab_txt
    nekolist = []
    cou = 0
    for tline in txt_neko.readlines():  # 一行ずつ読み込み
        # print(tline)
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
        #cou = cou + 1
        #if cou == 10:
            #break
#テキストデータに書き出しておく
path_tneko = "nekolist.txt"
with open(path_tneko,mode="w",encoding="utf-8")as nekotxt:
    nekotxt.write(str(nekolist))

#print(nekodict,nekolist)
for i in nekolist:
    print(i)