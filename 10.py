import sys
#unix $ wc -l hightemp.txt

data = open("hightemp.txt","r",encoding="utf-8")
print(data.readline())

print(len(data.readline()))
#wc hightemp.txt