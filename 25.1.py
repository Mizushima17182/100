# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
# 基礎情報
import json, gzip, re

jdata = "jawiki-country.json.gz"
string = ""
def uk():
    with gzip.open(jdata,'rt',encoding= "utf-8") as gjdata:
        for line in gjdata:
            jdict = json.loads(line)
            if jdict['title'] == 'イギリス':
                return jdict['text']

pattern= re.compile(r'^\{\{基礎情報.*?$(.*?)^\}\}$',re.MULTILINE+re.VERBOSE+re.DOTALL)
contents = pattern.findall(uk())
print(contents)
pattern = re.compile(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))',re.MULTILINE+re.VERBOSE+re.DOTALL)

filds=pattern.findall(contents[0])
print(filds)
result ={}
keys_test = []
#for fild in filds:
 #   result[fild[0]]

for fild in filds:
    result[fild[0]]=fild[1]
    keys_test.append(fild[0])

print(result)
print("こっから")
for item in sorted(result.items(),key=lambda fild: keys_test.index(fild[0])):
    print(item)