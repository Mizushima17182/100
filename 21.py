
import json
import gzip
import re

jdata = "jawiki-country.json.gz"
def uk():
    with gzip.open(jdata,'rt',encoding= "utf-8_sig") as gjdata:
        for line in gjdata:
            jdict = json.loads(line)
            if jdict['title'] == 'イギリス':
                return jdict['text']
pata = re.compile(r'^(.*\[\[Category:.*\]\].*)$', re.MULTILINE + re.VERBOSE)#←が必要
resu =pata.findall(uk())

for line in resu:
    print(line)
'''
for line in jdict:
    jdict = json.loads(line)
    if jdict[] == 'イギリス':
        print(jdict["text"])
        break
'''
#r'.*\[\[Category.*\]\]$'