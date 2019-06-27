with open("hightemp.txt", mode='r', encoding="utf-8")as hight:
    lines = hight.readlines()
    lines.sort(key =lambda line: float(line.split("\t")[2]))
    #print(lines)
    for i in lines:
        print(i)