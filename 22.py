import json,gzip,re

jdata = "jawiki-country.json.gz"
def uk():
    with gzip.open(jdata,'rt',encoding= "utf-8_sig") as gjdata:
        for line in gjdata:
            jdict = json.loads(line)
            if jdict['title'] == 'イギリス':
                return jdict['text']
#21のpata = re.compile(r'^(.*\[\[Category:.*\]\].*)$', re.MULTILINE + re.VERBOSE)#←が必要
#自分(r'^.*\[\[Category:(.*)(\|.*)?\]\].*$'　|が取り除けない
pata = re.compile(r'^.*\[\[Category:(.*?)(?:\|.*)?\]\].*$', re.MULTILINE + re.VERBOSE)#←が必要
resu =pata.findall(uk())
#pata2 = re.compile(r'^:\d*$')


for line in resu:
    print(line)
