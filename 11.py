import sys
'''11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，
もしくはexpandコマンドを用いよ．'''
data = open("hightemp.txt","r",encoding="utf-8")
#print(data.read())
tdata =data.read()
rdata = tdata.replace("\t"," ")#\tはタブ文字
print(rdata)

#sed s/\t/\s