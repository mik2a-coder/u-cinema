#!/usr/bin/env python3
"""Fabrique CINELUX-autonome.html : un seul fichier avec affiches, portraits, scènes et polices intégrés.
Usage : python3 tools/build-autonome.py   (depuis le dossier CINELUX)"""
import base64, os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
os.chdir(ROOT)
MIME = {'jpg': 'image/jpeg', 'png': 'image/png', 'woff2': 'font/woff2'}
def uri(p):
    return f"data:{MIME[p.rsplit('.',1)[1].lower()]};base64," + base64.b64encode(open(p, 'rb').read()).decode()
s = open('index.html', encoding='utf8').read()
# affiches
m = re.search(r"const IMGS=\{(.*?)\};", s, flags=re.S)
paths = dict(re.findall(r"""["']?(\w+)["']?\s*:\s*["'](img/[^"']+)["']""", m.group(1)))
s = s.replace(m.group(0), "const IMGS={" + ",".join(f"{k}:'{uri(v)}'" for k, v in paths.items()) + "};", 1)
# portraits et photos de personnes (PIMG)
mp = re.search(r"const PIMG=\{.*?\};", s, flags=re.S)
dirs = re.findall(r'"(img/people/[^"]+\.jpg)"', mp.group(0))
s = s.replace(mp.group(0), re.sub(r'"(img/people/[^"]+\.jpg)"', lambda mm: '"' + uri(mm.group(1)) + '"', mp.group(0)), 1)
# scènes (si présentes)
scenes = sorted(f[:-4] for f in os.listdir('img/scene') if f.endswith('.jpg')) if os.path.isdir('img/scene') else []
s = s.replace("function dirPhoto(f)", "const SCENEDATA={" + ",".join(f"{k}:'{uri('img/scene/'+k+'.jpg')}'" for k in scenes) + "};\nfunction dirPhoto(f)", 1)
s = s.replace('src="img/scene/${f.id}.jpg"', 'src="${SCENEDATA[f.id]||\'img/scene/\'+f.id+\'.jpg\'}"')
# polices
css = open('fonts/fonts.css', encoding='utf8').read()
css = re.sub(r"url\(([^)]+\.woff2)\)", lambda mm: "url(" + uri('fonts/' + mm.group(1)) + ")", css)
s = s.replace('<link rel="stylesheet" href="fonts/fonts.css">', "<style>" + css + "</style>", 1)
import re as _re
s = _re.sub(r'<link rel="(manifest|icon|apple-touch-icon)"[^>]*>\n', '', s)
open('CINELUX-autonome.html', 'w', encoding='utf8').write(s)
print(f"CINELUX-autonome.html : {len(s)//1024} Ko — {len(paths)} affiches, {len(dirs)} portraits, {len(scenes)} scènes")
