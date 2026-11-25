# Holt die Videos aus Melanies YouTube-Playlists (IDs in videos.json) und aktualisiert videos.json.
import json, re, urllib.request, xml.etree.ElementTree as ET, os
NS={"a":"http://www.w3.org/2005/Atom","yt":"http://www.youtube.com/xml/schemas/2015"}
FLAGS={"🇩🇪":"DE","🇬🇧":"EN","🇺🇸":"US","🇪🇸":"ES","🇩🇰":"DK","🇫🇷":"FR","🇮🇹":"IT","🇳🇱":"NL","🇦🇹":"AT","🇨🇭":"CH","🇵🇱":"PL","🇹🇷":"TR"}
def get(url):
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req,timeout=30) as r: return r.read()
def clean(t):
    lang=None
    for f,c in FLAGS.items():
        if f in t: lang=c; t=t.replace(f,"")
    t=re.sub(r"#\S+","",t); t=re.sub(r"[\U0001F300-\U0001FAFF☀-➿]","",t)
    return re.sub(r"\s+"," ",t).strip(" -|·"), lang
def thumb(vid, tall):
    os.makedirs("assets/yt",exist_ok=True)
    for ext in ("webp","jpg"):
        if os.path.exists(f"assets/yt/{vid}.{ext}"): return f"assets/yt/{vid}.{ext}"
    for name in (["oardefault.jpg","hqdefault.jpg"] if tall else ["maxresdefault.jpg","hqdefault.jpg"]):
        try:
            b=get(f"https://i.ytimg.com/vi/{vid}/{name}")
            if len(b)>2000:
                open(f"assets/yt/{vid}.jpg","wb").write(b); return f"assets/yt/{vid}.jpg"
        except Exception: pass
    return f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"
data=json.load(open("videos.json",encoding="utf-8"))
for key in ("shorts","videos","weitere"):
    pid=(data.get("playlists",{}).get(key) or "").strip()
    m=re.search(r"list=([\w-]+)",pid)
    if m: pid=m.group(1)
    if not pid: continue
    try:
        root=ET.fromstring(get(f"https://www.youtube.com/feeds/videos.xml?playlist_id={pid}"))
    except Exception as ex:
        print(f"{key}: Playlist nicht lesbar ({ex}), Liste bleibt unveraendert"); continue
    items=[]
    for en in root.findall("a:entry",NS):
        vid=en.find("yt:videoId",NS).text; titel,lang=clean(en.find("a:title",NS).text or "")
        d={"id":vid,"titel":titel or "Video","bild":thumb(vid,key=="shorts")}
        if lang: d["sprache"]=lang
        items.append(d)
    data[key]=items; print(f"{key}: {len(items)} Videos")
for key in ("shorts","videos","weitere"):
    for v in data.get(key,[]):
        if not v.get("bild","").startswith("http") and not os.path.exists(v.get("bild","")):
            v["bild"]=thumb(v["id"],key=="shorts")
json.dump(data,open("videos.json","w",encoding="utf-8"),ensure_ascii=False,indent=2); open("videos.json","a").write("\n")
