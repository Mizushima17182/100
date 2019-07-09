import json,gzip
jdata = "jawiki-country.json.gz"
with gzip.open(jdata, "rt", encoding="utf-8")as jdata:
    for line in jdata:
        jdict = json.loads(line)
        if jdict['title'] == 'イギリス':
            print(jdict["text"])
            break