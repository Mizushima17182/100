import MeCab

neko = "neko.txt"
with open(neko, 'rt', encoding="utf-8")as nekotxt:
    wagahai = nekotxt.read()
    print(wagahai)
    me = MeCab.Tagger("-oshasen")
    pri = me.parse(wagahai)
    print(pri)

    path_t = 'neko.txt.mecab'

    with open(path_t, mode='w',encoding="utf-8")as text_wagahai:
        text_wagahai.write(pri)
# やっぱりencoding="utf-8　ないとエラーが出る"