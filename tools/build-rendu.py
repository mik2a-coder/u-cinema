#!/usr/bin/env python3
"""Assemble le dossier à rendre : RENDU-U-CINEMA.pdf (via Chrome sans interface).
Usage : python3 tools/build-rendu.py   (depuis le dossier du projet)"""
import re,html,os,subprocess,base64,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def inline(t):
    t=html.escape(t,quote=False).replace('&lt;br&gt;','<br>')
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

def read(f):return open(f,encoding='utf-8').read()
def img(f):
    return 'data:image/jpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode()

def gallery(prefix,caps):
    cells=[]
    for f in sorted(x for x in os.listdir('rendu/captures') if x.startswith(prefix)):
        k=f[len(prefix):-4].lstrip('_')
        cells.append(f'<figure><img src="{img("rendu/captures/"+f)}"><figcaption>{caps.get(k,k)}</figcaption></figure>')
    return '<div class="gal">'+''.join(cells)+'</div>'
CAP={'01-accueil':'Accueil','02-fiche':'Fiche film','03-seance':'Séance','04-places':'Places','05-commande':'Commande','06-petite-faim':'Petite faim','07-paiement-refuse':'Imprévu : paiement refusé','08-billet':'Billet','09-compte':'Compte','06-compte':'Compte'}

sections=[
 ('Barème',md(read('BAREME.md'),2)),
 ('Brief et persona',md(read('BRIEF-PERSONA.md'),2)),
 ('Parcours utilisateur',md(read('PARCOURS.md'),2)+'<h3>Les écrans du parcours (téléphone)</h3>'+gallery('mobile',CAP)),
 ('Prototype mobile et grand écran','<p>Prototype en ligne : <a href="https://mik2a-coder.github.io/u-cinema/">https://mik2a-coder.github.io/u-cinema/</a></p><h3>Téléphone (390 px)</h3>'+gallery('mobile',CAP)+'<h3>Grand écran (1280 px)</h3>'+gallery('bureau',CAP)),
 ('Design system (variables et composants)',md(read('DESIGN.md'),2)),
 ('Tests et version améliorée',md(read('TESTS.md'),2)),
 ('Checklist de test (3 participants)',md(read('CHECKLIST-TESTS.md'),2)),
 ('Journal',md(read('JOURNAL.md'),2)),
 ('Annexe : grille « Peaufiner » et notes de conception',md(read('V2-NOTES.md'),2)),
 ('Annexe : conformité (RGPD, consommation, accessibilité)',md(read('CONFORMITE.md'),2)),
]
toc=''.join(f'<li><a href="#s{i}">{t}</a></li>' for i,(t,_) in enumerate(sections))
body=''.join(f'<section id="s{i}"><div class="sh">{i+1}</div>'+h.replace('<h2>','<h2 class="first">',1)+'</section>' if False else f'<section id="s{i}"><p class="kick">Partie {i+1}</p><h1>{t}</h1>{h}</section>' for i,(t,h) in enumerate(sections))
css='''
@page{size:A4;margin:16mm 14mm}
*{box-sizing:border-box}body{font:10.5pt/1.5 -apple-system,"Inter","Helvetica Neue",Arial,sans-serif;color:#1b160c}
h2,h3{page-break-after:avoid}h1{font-size:22pt;line-height:1.1;margin:0 0 8mm;letter-spacing:-.01em}h2{font-size:14pt;margin:8mm 0 3mm;border-bottom:1px solid #d9cfb8;padding-bottom:1.5mm}h3{font-size:11.5pt;margin:6mm 0 2mm}h4{font-size:10.5pt;margin:4mm 0 1mm}
.kick{font-size:8.5pt;letter-spacing:.16em;text-transform:uppercase;color:#8a5a00;margin:0 0 2mm;font-weight:700}
section{page-break-before:always}p{margin:0 0 3mm}ul,ol{margin:0 0 3mm 5mm;padding-left:4mm}li{margin-bottom:1mm}
table{width:100%;border-collapse:collapse;margin:3mm 0 5mm;font-size:8.8pt;page-break-inside:auto}tr{page-break-inside:avoid}th{background:#1e1810;color:#f4e4b6;text-align:left;padding:1.6mm 2mm}td{border-bottom:1px solid #e2d9c4;padding:1.6mm 2mm;vertical-align:top}
code{font:8.6pt "SF Mono",Menlo,monospace;background:#f1ead9;padding:.2mm 1mm;border-radius:1mm}pre{font:8.4pt/1.35 "SF Mono",Menlo,monospace;background:#f6f1e3;padding:3mm;border-radius:2mm;white-space:pre-wrap}
blockquote{margin:0 0 4mm;padding:2.5mm 4mm;border-left:3px solid #e4b243;background:#faf5e6;color:#4a3f27}a{color:#7a5206}hr{border:0;border-top:1px solid #d9cfb8;margin:5mm 0}
.cover{page-break-after:always;min-height:240mm;display:flex;flex-direction:column;justify-content:center}.cover h1{font-size:44pt;margin:0 0 4mm}.cover .sub{font-size:14pt;color:#5f5642;margin-bottom:12mm}.cover .meta{font-size:10.5pt;line-height:1.8}
.cover img{width:46mm;margin-bottom:8mm}.toc{page-break-after:always}.toc li{font-size:12pt;margin-bottom:2.5mm}
.gal{display:flex;flex-wrap:wrap;gap:4mm}.gal figure{margin:0;width:calc(33.3% - 3mm);page-break-inside:avoid}.gal img{width:100%;border:1px solid #d9cfb8;border-radius:2mm}.gal figcaption{font-size:8pt;color:#5f5642;margin-top:1mm}
'''
logo=img('img/logo-mark3.png').replace('image/jpeg','image/png')
doc=f'''<!doctype html><html lang="fr"><meta charset="utf-8"><title>U CINEMÀ — Dossier de rendu</title><style>{css}</style><body>
<div class="cover"><img src="{logo}"><h1>U CINEMÀ</h1><div class="sub">Prototype d'application de réservation de cinéma — mobile et grand écran</div>
<div class="meta"><strong>Exercice</strong> : « le meilleur prototype possible » (Prototyper en 2026 · Livrer)<br><strong>Auteur</strong> : Mika<br><strong>Date</strong> : 18 novembre 2026<br><strong>Prototype</strong> : <a href="https://mik2a-coder.github.io/u-cinema/">https://mik2a-coder.github.io/u-cinema/</a><br><strong>Code et documents</strong> : <a href="https://github.com/mik2a-coder/u-cinema">https://github.com/mik2a-coder/u-cinema</a><br><br>Ce dossier contient : barème, brief et persona, parcours, prototype (captures), design system, tests, journal, annexes.</div></div>
<div class="toc"><h1>Sommaire</h1><ol>{toc}</ol></div>{body}</body></html>'''
open('rendu/dossier.html','w',encoding='utf-8').write(doc)
chrome='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
subprocess.run([chrome,'--headless=new','--disable-gpu','--no-pdf-header-footer','--print-to-pdf=RENDU-U-CINEMA.pdf','file://'+os.path.abspath('rendu/dossier.html')],check=True,capture_output=True)
print('RENDU-U-CINEMA.pdf',os.path.getsize('RENDU-U-CINEMA.pdf')//1024,'Ko')

# Checklist seule : portrait 3:4 (tablette reMarkable), contraste fort, grandes cases d'écriture
chk_css=css.replace('@page{size:A4;margin:16mm 14mm}','@page{size:180mm 240mm;margin:8mm}').replace('font:10.5pt/1.5','font:9pt/1.3').replace('font-size:8.8pt','font-size:8.2pt').replace('background:#1e1810;color:#f4e4b6','background:#e6e6e6;color:#000;border-bottom:1.5px solid #000').replace('blockquote{','blockquote{border-left-color:#000;background:#f3f3f3;').replace('td{border-bottom:1px solid #e2d9c4','td{border-bottom:1px solid #777')
extra='h1{font-size:17pt;margin-bottom:4mm}h2{page-break-after:avoid;font-size:12pt;margin:5mm 0 2mm;border-bottom:1.5px solid #000}table{table-layout:fixed}td{height:10mm;vertical-align:middle}.sc th:first-child,.sc td:first-child{width:9%}.sc th:nth-child(2),.sc td:nth-child(2){width:49%}.sc th:nth-child(n+3),.sc td:nth-child(n+3){width:14%;text-align:center}.pt th:first-child,.pt td:first-child{width:40%}.pt th:nth-child(n+2):nth-child(-n+4),.pt td:nth-child(n+2):nth-child(-n+4){width:10%;text-align:center}.pt th:last-child,.pt td:last-child{width:30%}table:not(.sc):not(.pt) th:first-child{width:9%}a{color:#000}section{page-break-before:avoid}'
chk=f'''<!doctype html><html lang="fr"><meta charset="utf-8"><title>Checklist de test</title><style>{chk_css}{extra}</style><body>{md(read('CHECKLIST-TESTS.md'),1)}</body></html>'''
open('rendu/checklist.html','w',encoding='utf-8').write(chk)
subprocess.run([chrome,'--headless=new','--disable-gpu','--no-pdf-header-footer','--print-to-pdf=CHECKLIST-TEST-3-PERSONNES.pdf','file://'+os.path.abspath('rendu/checklist.html')],check=True,capture_output=True)
print('CHECKLIST-TEST-3-PERSONNES.pdf',os.path.getsize('CHECKLIST-TEST-3-PERSONNES.pdf')//1024,'Ko')
