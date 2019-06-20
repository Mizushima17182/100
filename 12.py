import sys

with open('hightemp.txt',encoding="utf-8")as data,\
     open("col1.txt","w",encoding="utf-8")as c,\
     open("col2.txt","w",encoding="utf-8")as cc:
    a=[]
    for line in data:
            a = line.split("\t")
            c.write(a[0]+"\n")
            cc.write(a[1]+"\n")
print()