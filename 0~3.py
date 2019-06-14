#00
a = "stressed"

print (a[::-1])
#01
b = "パタトクカシーー"
print(b[::2])
print(b[1::2])
#03
c = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
d = []
f = []
g = 0
c = c.replace(",","")
c = c.replace(".","")
c = c.split()
d = d
#print(c)
for e in c:
     d.append(len(e))

print(d)