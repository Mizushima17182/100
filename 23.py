# セクション構造　== == 1,=== === 2
import json, gzip, re

jdata = "jawiki-country.json.gz"


def uk():
    with gzip.open(jdata, 'rt', encoding="utf-8") as gjdata:
        for line in gjdata:
            jdict = json.loads(line)
            if jdict['title'] == 'イギリス':
                return jdict['text']


pattern = re.compile(r'^(\=+.*\=+).*$', re.MULTILINE + re.VERBOSE)
resu = pattern.findall(uk())

for line in resu:
    numcount = str(line.count('=') // 2 - 1)
    line = line.strip("=")
    print(line + '\t' + numcount)
