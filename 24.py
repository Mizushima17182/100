#24. ファイル参照の抽出
#記事から参照されているメディアファイルをすべて抜き出せ．
#例：ファイル:PalaceOfWestminsterAtNight.jpg|[[ウェストミンスター宮殿]]

#.jpg以降を取り除きたい
import json,gzip,re

jdata = "jawiki-country.json.gz"
def uk():
    with gzip.open(jdata,'rt',encoding= "utf-8") as gjdata:
        for line in gjdata:
            jdict = json.loads(line)
            if jdict['title'] == 'イギリス':
                return jdict['text']
pata = re.compile(r'^ファイル:(.*)(?:\|.*)$',re.MULTILINE + re.VERBOSE)
resu =pata.findall(uk())

for line in resu:
    print(line)
