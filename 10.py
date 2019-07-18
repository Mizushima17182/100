import sys
hight = sys.argv
print(hight)
file = open("hightemp.txt","r",encoding="utf-8")
print(file.readline())

print(len(file.readline()))
#wc -1 hightemp.txt

# ========
# コメント
# ========
# L3: openはデータというよりもファイルオブジェクト的なものになるので、変数名はfileのほうが良いと思う
# L1: argvを使おう（以降のファイル全部）
# wc -l hightemp.txt かな