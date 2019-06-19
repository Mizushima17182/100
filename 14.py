'''先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．'''
with open("hightemp.txt",encoding="utf-8")as hight:
    gyo = int(input())
    resu = ""
    c = 0
    b = hight.readlines()
    print(b)
    for line in b :
            if c != gyo:
                resu = line
                c += 1
                print(resu,end='')
            else:
                break
#print(resu)

