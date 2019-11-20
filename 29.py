import json, gzip, re, requests

jsondata = 'jawiki-country.json.gz'


def uk():
    with gzip.open(jsondata, 'rt', encoding="utf-8")as gdata:
        for gline in gdata:
            linej = json.loads(gline)
            if linej['title'] == 'イギリス':
                return linej['text']


# print( uk())
# 正規表現　基礎情報抜き出し

pattern = re.compile(r'^\{\{基礎情報.*?$(.*?)^\}\}$', re.MULTILINE + re.VERBOSE + re.DOTALL)
resu1 = pattern.findall(uk())
# (.+?)(?:(?=\n\|)| (?=\n$))
# print(resu1)　
ukimageurl = re.compile(r'国旗画像\s=\s*(.+)\n')
resu2 = ukimageurl.findall(resu1[0])
imageurl = resu2[0]
print("呼び出す画像　"+imageurl)

S = requests.Session()

URL = "https://www.mediawiki.org/w/api.php"
# "" : "" ,
PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "File:Flag of the United Kingdom.svg",
    "prop": "imageinfo",
    "iiprop": "url"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

print(PAGES)
for a in PAGES:
    print(a)
#　print(PAGES)
for k,v in PAGES.items():
    print(v["imageinfo"])

#print(v["imageinfo"],[0],["url"])

# print(v["title"] + "is upload by User:" + v["imageinfo"[0]["user"]])
