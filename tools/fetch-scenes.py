#!/usr/bin/env python3
"""
Télécharge une image de scène (16:9, sans texte) pour chaque film de CINÉLUX depuis TMDB
et la range dans img/scene/<id>.jpg. L'appli les utilise automatiquement sur l'écran de la salle.

Usage :
    TMDB_KEY=votre_clé python3 tools/fetch-scenes.py

La clé est gratuite : themoviedb.org > Paramètres > API > Demander une clé (usage personnel).
Les deux formats marchent : la clé courte « API Key » ou le long « Jeton d'accès (Bearer) ».
"""
import json, os, sys, urllib.error, urllib.parse, urllib.request

FILMS = [  # id (celui de l'appli), titre de recherche, année
    ("drive", "Drive", 2011), ("br2049", "Blade Runner 2049", 2017), ("oppenheimer", "Oppenheimer", 2023),
    ("whiplash", "Whiplash", 2014), ("dune", "Dune", 2021), ("parasite", "Parasite", 2019),
    ("interstellar", "Interstellar", 2014), ("madmax", "Mad Max: Fury Road", 2015),
    ("amelie", "Le Fabuleux Destin d'Amélie Poulain", 2001),
    ("portrait", "Portrait de la jeune fille en feu", 2019),
]
KEY = os.environ.get("TMDB_KEY", "").strip()
if not KEY:
    sys.exit("Manque la clé : TMDB_KEY=... python3 tools/fetch-scenes.py   (voir l'aide en haut du fichier)")
if KEY.upper() in ("VOTRE_CLE", "VOTRE_CLÉ", "XXX", "CLE", "CLÉ") or "VOTRE" in KEY.upper():
    sys.exit("« %s » est l'exemple de l'aide, pas une vraie clé.\n"
             "Remplacez-le par votre clé TMDB (themoviedb.org > Paramètres > API)." % KEY)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "img", "scene")
os.makedirs(OUT, exist_ok=True)

def api(path, **params):
    headers = {"User-Agent": "cinelux-prototype/1.0", "Accept": "application/json"}
    if len(KEY) > 60:
        headers["Authorization"] = "Bearer " + KEY
    else:
        params["api_key"] = KEY
    url = "https://api.themoviedb.org/3" + path + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=20) as r:
        return json.load(r)

credits = []
for fid, title, year in FILMS:
    dest = os.path.join(OUT, fid + ".jpg")
    try:
        hits = api("/search/movie", query=title, year=year, language="fr-FR").get("results", [])
        if not hits:
            hits = api("/search/movie", query=title, language="fr-FR").get("results", [])
        if not hits:
            print(f"✗ {fid}: film introuvable"); continue
        movie = hits[0]
        imgs = api(f"/movie/{movie['id']}/images", include_image_language="null").get("backdrops", [])
        imgs = [i for i in imgs if not i.get("iso_639_1") and i.get("width", 0) >= 1280] or \
               [i for i in api(f"/movie/{movie['id']}/images").get("backdrops", []) if i.get("width", 0) >= 1280]
        if not imgs:
            print(f"✗ {fid}: aucune image de scène exploitable"); continue
        best = max(imgs, key=lambda i: (i.get("vote_average", 0), i.get("vote_count", 0)))
        url = "https://image.tmdb.org/t/p/w1280" + best["file_path"]
        req = urllib.request.Request(url, headers={"User-Agent": "cinelux-prototype/1.0"})
        with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as f:
            f.write(r.read())
        print(f"✓ {fid}: {movie.get('title')} ({best['width']}×{best['height']})")
        credits.append(f"{fid}: {movie.get('title')} – image TMDB {best['file_path']}")
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            sys.exit("\n✗ TMDB refuse la clé (erreur %d). Vérifiez qu'elle est complète, sans espace ni guillemet,\n"
                     "  et que vous utilisez bien la « Clé d'API » (ou le « Jeton d'accès »)." % e.code)
        print(f"✗ {fid}: HTTP {e.code}")
    except Exception as e:
        print(f"✗ {fid}: {e}")

with open(os.path.join(OUT, "CREDITS.txt"), "w", encoding="utf8") as f:
    f.write("Images fournies par TMDB (https://www.themoviedb.org). "
            "This product uses the TMDB API but is not endorsed or certified by TMDB.\n\n" + "\n".join(credits) + "\n")
ok = len(credits)
if ok:
    print(f"\nTerminé : {ok}/{len(FILMS)} images récupérées. Rechargez CINÉLUX (Cmd+Maj+R).")
else:
    print("\nAucune image récupérée : rien n'a été modifié.")
