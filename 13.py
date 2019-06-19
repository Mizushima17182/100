with open("col1.txt",encoding="utf-8")as col1,\
        open("col2.txt",encoding="utf-8")as col2,\
        open("marg.txt","w",encoding="utf-8")as marg:
    col1 = col1.readlines()
    col2 = col2.readlines()
    print(col1,col2)
    for a,b in zip(col1,col2):
        a = a.replace("\n","")
        b = b.replace("\n","")
        resu = a + " " +b
        print(resu)
        marg.write(resu+"\n")

