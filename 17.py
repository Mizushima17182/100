'''17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）
を求めよ．確認にはsort, uniqコマンドを用いよ．'''
with open("hightemp.txt",mode='r',encoding="utf-8")as hight:
    resu = ""
    c = 0
    #data = hight.readline()
   # print(data)
    for line in hight.readlines():
        #print(line)
        line = line.split()
        #print(line[0])
        if line[0] not in resu:
            resu = resu + str(line[0]) +"\n"
            c += 1
            #print(resu)

print(resu,c)
