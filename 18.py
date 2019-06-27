'''18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ
（注意: 各行の内容は変更せずに並び替えよ）
'''
import sys
#data = sys.argv
#print(data)

with open("hightemp.txt",mode='r',encoding="utf-8")as hight:
        slist = {}
        line = []
        adata = hight.readline()
        data = hight.readlines()
        print(data)

        for sp in data:
            key = sp.split()[0]
            slist[key] = slist.get(key,0)+1
        print(slist)
        ssort = sorted(slist.items(),key=lambda x:x[1],reverse=True)
        print(ssort)

      #  a = sorted(data,key=lambda x:int(x.split()[2]),):
        '''print(data)
        for line in data:
            #print(line)
            linesp = line.split()
            slist.append(linesp[2])
        print(slist)
        slist.sort()'''