'''16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，
入力のファイルを行単位でN分割せよ
'''
import math

with open("hightemp.txt",mode='r',encoding="utf-8")as hight:
    n = int(input())
    resu = ""
    data = hight.readlines()
    c = len(data)
    bun = math.ceil(c/n)
    print(bun)
    cou = 1
    cou2 = 0
    lines = ""
    for line in data:
        print(lines, str(cou) + "回目")
        if cou <= bun:
           lines = lines + line
           cou += 1
        if bun+1 == cou:
            open("N" + str(cou2) + ".txt", "w", encoding="utf-8").write(lines)
            cou2 += 1
            cou = 1
            lines = ""
    print(cou2)
