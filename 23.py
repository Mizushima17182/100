#セクション構造　== == 1,=== === 2
import json,gzip,re

jdata = "jawiki-country.json.gz"
def uk():
    with gzip.open(jdata,'rt',encoding= "utf-8") as gjdata:
        for line in gjdata:
            jdict = json.loads(line)
            if jdict['title'] == 'イギリス':
                return jdict['text']
pata = re.compile(r'^(\=+.*\=+).*$',re.MULTILINE + re.VERBOSE)
resu =pata.findall(uk())

for line in resu:
    print(line+str(round(line.count('=')//2-1)))