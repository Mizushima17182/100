'''15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．'''
with open("hightemp.txt",mode='r',encoding="utf-8")as hight:
    gyo = int(input())
    resu = ""
    data = hight.readlines()
    c = len(data)
    print(c)
   # print(hight.readlines())
    for line in data:
       # print(line)
        if c <= gyo:
           print(line,end='')
           c -= 1
        else:
            c -= 1