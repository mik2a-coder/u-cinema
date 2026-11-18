#!/usr/bin/env python3
"""Assemble le dossier à rendre : RENDU-U-CINEMA.pdf (via Chrome sans interface).
Usage : python3 tools/build-rendu.py   (depuis le dossier du projet)"""
import re,html,os,subprocess,base64,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def inline(t):
    t=html.escape(t,quote=False).replace('&lt;br&gt;','<br>')
    t=re.sub(r'`(#[0-9A-Fa-f]{6})`',lambda m:f'<span class="swc" style="background:{m.group(1)}"></span><code>{m.group(1)}</code>',t)
    t=re.sub(r'`([^`]+)`',r'<code>\1</code>',t)
    t=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',t)
    t=re.sub(r'(?<![*\w])\*([^*\n]+)\*(?![*\w])',r'<em>\1</em>',t)
    t=re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',r'<img alt="\1" src="\2">',t)
    t=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',t)
    t=re.sub(r'(?<!["=>])(https?://[^\s<)]+)',r'<a href="\1">\1</a>',t)
    return t

def md(src,base=1):
    out=[];lines=src.split('\n');i=0
    def hd(n):return min(6,n+base-1)
    while i<len(lines):
        l=lines[i]
        if l.startswith('```'):
            j=i+1;buf=[]
            while j<len(lines) and not lines[j].startswith('```'):buf.append(lines[j]);j+=1
            out.append('<pre>'+html.escape('\n'.join(buf))+'</pre>');i=j+1;continue
        m=re.match(r'^(#{1,4}) (.*)',l)
        if m:out.append(f'<h{hd(len(m.group(1)))}>{inline(m.group(2))}</h{hd(len(m.group(1)))}>');i+=1;continue
        if l.strip()=='---':out.append('<hr>');i+=1;continue
        if l.startswith('>'):
            buf=[]
            while i<len(lines) and lines[i].startswith('>'):buf.append(lines[i][1:].strip());i+=1
            out.append('<blockquote>'+inline(' '.join(buf))+'</blockquote>');continue
        if l.startswith('|') and i+1<len(lines) and re.match(r'^\|[\s:|-]+\|$',lines[i+1].strip()):
            hdr=[c.strip() for c in l.strip().strip('|').split('|')];i+=2;rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]);i+=1
            cls=' class="sc"' if hdr and hdr[0]=='#' and 'P1' in hdr else ' class="pt"' if hdr and hdr[0].startswith('Écran') else ''
            out.append(f'<table{cls}><thead><tr>'+''.join(f'<th>{inline(c)}</th>' for c in hdr)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{inline(c)}</td>' for c in r)+'</tr>' for r in rows)+'</tbody></table>');continue
        if re.match(r'^\s*[-*] ',l) or re.match(r'^\s*\d+\. ',l):
            ordered=bool(re.match(r'^\s*\d+\. ',l));items=[]
            while i<len(lines) and (re.match(r'^\s*[-*] ',lines[i]) or re.match(r'^\s*\d+\. ',lines[i])):
                items.append(re.sub(r'^\s*([-*]|\d+\.) ','',lines[i]));i+=1
            tag='ol' if ordered else 'ul'
            out.append(f'<{tag}>'+''.join(f'<li>{inline(x)}</li>' for x in items)+f'</{tag}>');continue
        if l.strip()=='':i+=1;continue
        buf=[l];i+=1
        while i<len(lines) and lines[i].strip() and not re.match(r'^(#|>|\||```|---|\s*[-*] |\s*\d+\. )',lines[i]):buf.append(lines[i]);i+=1
        out.append('<p>'+inline(' '.join(buf))+'</p>')
    return '\n'.join(out)


def clean(t):
    import re as _r
    t=t.replace(' ; cela réduit le critère « peu de couleurs » de la grille Peaufiner','')
    t=t.replace('grille « Peaufiner »','revue de conception')
    t=_r.sub(r'^.*(Notes : grille Peaufiner|Lisibilité, cohérence \(grille).*$','',t,flags=_r.M)
    t=_r.sub(r'Peaufiner : ','',t)
    return t
def sans_notes(t):
    """Retire du dossier remis les notes de notation (points, statuts, auto-évaluation)."""
    import re as _r
    lines=t.split('\n');out=[];skip=False
    for l in lines:
        if l.startswith('| # | Critère'):skip=True
        if skip:
            if l.startswith('|'):continue
            skip=False
        if l.startswith('> Auto-évaluation'):continue
        out.append(l)
    t='\n'.join(out)
    t=_r.sub(r' — \d+ points?','',t)
    t=_r.sub(r'[^\n.;]*(grille « Peaufiner »|grille Peaufiner|Peaufiner :)[^\n]*','',t) if False else t
    t=t.replace('(19 points, plus un)','').replace('Réponse à la page « Barème »','Critères et preuves')
    t=_r.sub(r' Le point n.est acquis qu.une fois[^\n]*','',t)
    return t

def read(f):
    f=f if os.path.exists(f) else 'documents/'+f
    return clean(open(f,encoding='utf-8').read())
def _read_raw(f):return open(f,encoding='utf-8').read()
def img(f):
    return 'data:image/jpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode()

def gallery(prefix,caps):
    cells=[]
    for f in sorted(x for x in os.listdir('rendu/captures') if x.startswith(prefix)):
        k=f[len(prefix):-4].lstrip('_')
        cells.append(f'<figure><img src="{img("rendu/captures/"+f)}"><figcaption>{caps.get(k,k)}</figcaption></figure>')
    return '<div class="gal">'+''.join(cells)+'</div>'
CAP={'10-fiche-personne':'Fiche personne','11-assistant':'Assistant : réservation par la conversation','12-recapitulatif':'Récapitulatif avant paiement','13-recompenses':'Compte : avoir et récompenses','01-accueil':'Accueil','02-fiche':'Fiche film','03-seance':'Séance','04-places':'Places','05-commande':'Commande','06-petite-faim':'Petite faim','07-paiement-refuse':'Imprévu : paiement refusé','08-billet':'Billet','09-compte':'Compte','06-compte':'Compte'}

sections=[
 ('Direction artistique et palette',md(read('DIRECTION-ARTISTIQUE.md'),2)),
 ('Critères et preuves',md(sans_notes(read('BAREME.md')),2)),
 ('Brief et persona',md(read('BRIEF-PERSONA.md'),2)),
 ('Idées ajoutées et plus-values',md(read('IDEES.md'),2)),
 ('Politiques d\'achat, d\'annulation et horaires',md(read('POLITIQUES.md'),2)),
 ('Parcours utilisateur',md(read('PARCOURS.md'),2)+'<h3>Les écrans du parcours (téléphone)</h3>'+gallery('mobile',CAP)),
 ('Prototype mobile et grand écran','<p>Prototype en ligne : <a href="https://mik2a-coder.github.io/u-cinema/">https://mik2a-coder.github.io/u-cinema/</a></p><h3>Téléphone (390 px)</h3>'+gallery('mobile',CAP)+'<h3>Grand écran (1280 px)</h3>'+gallery('bureau',CAP)),
 ('Design system (variables et composants)',md(read('DESIGN.md'),2)),
 ('Tests et version améliorée',md(read('TESTS.md'),2)),
 ('Feuille de test (3 personnes, 5 minutes)',md(read('CHECKLIST-TESTS.md'),2)),
 ('Journal',md(read('JOURNAL.md'),2)),
 ('Journal des versions',md(read('VERSIONS.md'),2)),
 ('Annexe : conformité (RGPD, consommation, accessibilité)',md(read('CONFORMITE.md'),2)),
]
toc=''.join(f'<li><a href="#s{i}">{t}</a></li>' for i,(t,_) in enumerate(sections))
body=''.join(f'<section id="s{i}"><div class="sh">{i+1}</div>'+h.replace('<h2>','<h2 class="first">',1)+'</section>' if False else f'<section id="s{i}"><p class="kick">Partie {i+1}</p><h1>{t}</h1>{h}</section>' for i,(t,h) in enumerate(sections))
css='''
@font-face{font-family:"Bebas Neue";src:url(../fonts/BebasNeue-400.woff2) format("woff2")}
@font-face{font-family:"Inter";font-weight:400 700;src:url(../fonts/Inter-400.woff2) format("woff2")}
@page{size:A4;margin:15mm 13mm 16mm;background:#FAF6EB}
:root{--bg:#FAF6EB;--paper:#FDFBF6;--sand:#F6EFDE;--ink:#16120A;--soft:#5F5642;--btn:#1E1810;--cream:#F4E4B6;--gold:#F0C05A;--gold2:#B98322;--goldt:#87611B;--line:#E4D9BF}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html{background:var(--bg)}body{margin:0;background:var(--bg);font:10pt/1.55 "Inter",-apple-system,"Helvetica Neue",Arial,sans-serif;color:var(--ink)}
h1,h2,h3{font-family:"Bebas Neue","Oswald",Impact,sans-serif;font-weight:400;letter-spacing:.04em;color:var(--ink)}
h2,h3,h4{page-break-after:avoid}
h1{font-size:30pt;line-height:1;margin:0 0 7mm}
h1::after{content:"";display:block;width:22mm;height:1.6mm;margin-top:3mm;border-radius:1mm;background:linear-gradient(90deg,var(--gold),var(--gold2))}
h2{font-size:17pt;margin:9mm 0 3mm;padding-bottom:1.5mm;border-bottom:1px solid var(--line)}
h3{font-size:13pt;margin:6mm 0 2mm;color:var(--goldt)}h4{font:700 10pt "Inter",sans-serif;margin:4mm 0 1mm;color:var(--soft)}
.kick{font-size:8pt;letter-spacing:.2em;text-transform:uppercase;color:var(--goldt);margin:0 0 2mm;font-weight:700}
section{page-break-before:always}p{margin:0 0 3mm}ul,ol{margin:0 0 3mm 5mm;padding-left:4mm}li{margin-bottom:1mm}li::marker{color:var(--gold2)}
table{width:100%;border-collapse:separate;border-spacing:0;margin:3mm 0 6mm;font-size:8.6pt;page-break-inside:auto;background:var(--paper);border:1px solid var(--line);border-radius:3mm;overflow:hidden}
tr{page-break-inside:avoid}th{background:var(--btn);color:var(--cream);text-align:left;padding:2mm 2.4mm;font-weight:600;letter-spacing:.02em}
td{border-top:1px solid var(--line);padding:1.9mm 2.4mm;vertical-align:top}tbody tr:nth-child(even) td{background:rgba(246,239,222,.55)}
td strong{color:var(--ink)}
.swc{display:inline-block;width:3.6mm;height:3.6mm;border-radius:1mm;vertical-align:-.7mm;margin-right:1.4mm;border:1px solid rgba(22,18,10,.25)}
code{font:8.2pt "SF Mono",Menlo,monospace;background:var(--sand);padding:.2mm 1.1mm;border-radius:1mm;color:var(--ink)}
pre{font:8pt/1.4 "SF Mono",Menlo,monospace;background:var(--paper);border:1px solid var(--line);padding:3mm;border-radius:3mm;white-space:pre-wrap}
blockquote{margin:0 0 4mm;padding:3mm 4.5mm;border-left:1.2mm solid var(--gold);background:var(--paper);border-radius:0 3mm 3mm 0;color:var(--soft)}
a{color:var(--goldt);text-decoration-color:var(--gold)}hr{border:0;border-top:1px solid var(--line);margin:5mm 0}em{color:var(--soft)}
.cover{page-break-after:always;min-height:262mm;display:flex;flex-direction:column;justify-content:center;position:relative}
.cover img{width:40mm;margin-bottom:9mm}
.cover h1{font-size:84pt;letter-spacing:.07em;margin:0 0 4mm}.cover h1 b{color:#B06F06;font-weight:400}.cover h1::after{display:none}
.cover .sub{font-size:14pt;color:var(--soft);margin-bottom:10mm;max-width:130mm;line-height:1.35}
.cover .pal{display:flex;height:16mm;border-radius:4mm;overflow:hidden;border:1px solid var(--line);margin:0 0 9mm}.cover .pal i{flex:1}
.cover .meta{font-size:10pt;line-height:1.9;background:var(--paper);border:1px solid var(--line);border-radius:4mm;padding:5mm 7mm}
.cover .ver{display:inline-block;margin-bottom:6mm;padding:1.4mm 4mm;border-radius:99px;background:var(--btn);color:var(--cream);font-size:9pt;font-weight:600;letter-spacing:.06em;width:fit-content}
.toc{page-break-after:always}.toc ol{counter-reset:t;list-style:none;margin:0;padding:0}.toc li{counter-increment:t;font-size:12pt;padding:3mm 0;border-bottom:1px solid var(--line);display:flex;gap:4mm;align-items:baseline}.toc li::before{content:counter(t,decimal-leading-zero);font:15pt "Bebas Neue";color:var(--gold2);width:9mm}
.gal{display:flex;flex-wrap:wrap;gap:4mm}.gal figure{margin:0;width:calc(33.3% - 3mm);page-break-inside:avoid}.gal img{width:100%;border:1px solid var(--line);border-radius:2.5mm}.gal figcaption{font-size:8pt;color:var(--soft);margin-top:1mm}
'''
logo=img('img/logo-mark3.png').replace('image/jpeg','image/png')
doc=f'''<!doctype html><html lang="fr"><meta charset="utf-8"><title>U CINEMÀ — Dossier de rendu</title><style>{css}</style><body>
<div class="cover"><img src="{logo}"><div class="ver">VERSION 105 · 18 NOVEMBRE 2026</div><h1><b>U</b> CINEMÀ</h1><div class="sub">Prototype d'application de réservation de cinéma, mobile et grand écran</div>
<div class="pal"><i style="background:#FAF6EB"></i><i style="background:#F6EFDE"></i><i style="background:#16120A"></i><i style="background:#1E1810"></i><i style="background:#F0C05A"></i><i style="background:#B98322"></i><i style="background:#0B0A08"></i></div>
<div class="meta"><strong>Exercice</strong> : « le meilleur prototype possible » (Prototyper en 2026 · Livrer)<br><strong>Auteur</strong> : Mika<br><strong>Prototype</strong> : <a href="https://mik2a-coder.github.io/u-cinema/">https://mik2a-coder.github.io/u-cinema/</a><br><strong>Page d'erreur réseau</strong> : <a href="https://mik2a-coder.github.io/u-cinema/#x:0:off">https://mik2a-coder.github.io/u-cinema/#x:0:off</a><br><strong>Code</strong> : <a href="https://github.com/mik2a-coder/u-cinema">https://github.com/mik2a-coder/u-cinema</a><br><strong>Contenu</strong> : direction artistique et palette, idées ajoutées, politiques d'achat et horaires, critères et preuves, brief et persona, parcours, design system, tests, journal et prompts, journal des versions, annexes</div></div>
<div class="toc"><h1>Sommaire</h1><ol>{toc}</ol></div>{body}</body></html>'''
open('rendu/dossier.html','w',encoding='utf-8').write(doc)
chrome='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
subprocess.run([chrome,'--headless=new','--disable-gpu','--no-pdf-header-footer','--print-to-pdf=A-RENDRE/RENDU-U-CINEMA.pdf','file://'+os.path.abspath('rendu/dossier.html')],check=True,capture_output=True)
print('RENDU-U-CINEMA.pdf',os.path.getsize('A-RENDRE/RENDU-U-CINEMA.pdf')//1024,'Ko')

# Checklist seule : portrait 3:4 (tablette reMarkable), contraste fort, grandes cases d'écriture
chk_css=css.replace('@page{size:A4;margin:16mm 14mm}','@page{size:180mm 240mm;margin:8mm}').replace('font:10.5pt/1.5','font:9pt/1.3').replace('font-size:8.8pt','font-size:8.2pt').replace('background:#1e1810;color:#f4e4b6','background:#e6e6e6;color:#000;border-bottom:1.5px solid #000').replace('blockquote{','blockquote{border-left-color:#000;background:#f3f3f3;').replace('td{border-bottom:1px solid #e2d9c4','td{border-bottom:1px solid #777')
extra='h1{font-size:17pt;margin-bottom:4mm}h2{page-break-after:avoid;font-size:12pt;margin:5mm 0 2mm;border-bottom:1.5px solid #000}table{table-layout:auto;margin:1mm 0 3mm}td{height:9mm;vertical-align:middle;font-size:8.4pt;line-height:1.25}th{padding:1mm 2mm}.sc th:first-child,.sc td:first-child{width:9%}.sc th:nth-child(2),.sc td:nth-child(2){width:49%}.sc th:nth-child(n+3),.sc td:nth-child(n+3){width:14%;text-align:center}.pt th:first-child,.pt td:first-child{width:40%}.pt th:nth-child(n+2):nth-child(-n+4),.pt td:nth-child(n+2):nth-child(-n+4){width:10%;text-align:center}.pt th:last-child,.pt td:last-child{width:30%}table:not(.sc):not(.pt) th:first-child{width:9%}a{color:#000}section{page-break-before:avoid}'
chk=f'''<!doctype html><html lang="fr"><meta charset="utf-8"><title>Checklist de test</title><style>{chk_css}{extra}</style><body>{md(read('CHECKLIST-TESTS.md'),1)}</body></html>'''
open('rendu/checklist.html','w',encoding='utf-8').write(chk)
subprocess.run([chrome,'--headless=new','--disable-gpu','--no-pdf-header-footer','--print-to-pdf=A-RENDRE/CHECKLIST-TEST-3-PERSONNES.pdf','file://'+os.path.abspath('rendu/checklist.html')],check=True,capture_output=True)
print('CHECKLIST-TEST-3-PERSONNES.pdf',os.path.getsize('A-RENDRE/CHECKLIST-TEST-3-PERSONNES.pdf')//1024,'Ko')
