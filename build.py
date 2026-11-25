# Erzeugt index.html aus den Inhalten unten. Videos ein-/ausblenden: True/False.
import html
profil = dict(name="Superlifestyle4u", person="Melanie N. Seyfarth", rolle="Unabhängige Super Patch Partnerin",
  instagram="https://www.instagram.com/superlifestyle4u", youtube="https://www.youtube.com/@heilberatung")
haupt = dict(titel="Deine Reise mit Super Patch startet hier", text="Patches ansehen, bestellen oder Partner werden",
  url="https://dein.superpatch.com/", bild="assets/start.webp")
links = [
 ("Veränderung JETZT","Mein Telegram-Kanal mit Infos zur Technologie und vielen Erfahrungsberichten","https://t.me/veraenderungjetzt","assets/telegram.webp"),
 ("Erfahrungen anderer Anwender","Die Facebook-Gruppe: was andere mit Super Patch erlebt haben","https://m.facebook.com/groups/956448215670293/","assets/community.webp"),
 ("Das bin ich","Mein persönliches Facebook-Profil","https://www.facebook.com/share/16iSZDcPRD/","assets/profil.webp"),
 ("Schreib mir auf WhatsApp","Ich bin für dich da","https://wa.me/4915156085551","assets/whatsapp.webp"),
]
shorts = [
 ("hqQiaKcssfo","Moderne Medizin, alte Antworten auf neue Probleme",True),
 ("ID4qA0dTEJg","Black Friday Mega Deal",True),
 ("Ih1LGjGePOM","Vibrotaktile Technologie von Super Patch",True),
 ("hR-Yp6534fc","Sofortige Veränderung",True),
 ("P-tJDqF7eNo","Schmerzen: Die Studie zeigt …",True),
 ("ETkhepRYbS8","Deutliche Stressreduzierung sichtbar",True),
 ("bD5rk8vXZrs","Erfahrungsbericht Freedom und Defend",True),
 ("nkMjXvPpNxM","Testimony Pain",True),
 ("UfXvNrsKk1Y","28. Oktober 2025",True),
 ("yIHLQQKNC4c","Sådan laver du demoen med Jay",False),
]
eigene = [
 ("assets/jay-restore.mp4","assets/jay-restore.webp","Auszeichnung für die RESTORE-Studie","Jay Dhaliwal, Gründer und CEO von Super Patch, über die Auszeichnung von Dr. Jeff Gudin und seinem Team beim Kongress „Business of Pain 2026“ in Miami Beach.",True),
 ("assets/jay-15-jahre.mp4","assets/jay-15-jahre.webp","15 Jahre Entwicklung","Jay Dhaliwal über die 15 Jahre Entwicklungsarbeit hinter dem Patch.",True),
]
videos = [("yP2oXVvSrqc","Wie die Technologie funktioniert","DE",True),("Dt9QMNOUzMY","REM Patch","DE",True),("7biT7ZaT4I8","Lumi Patch","DE",True),("xzSriNDz28s","Rocket Patch","DE",True)]
weitere = [("AbyxyIsGTQU","REM Patch","EN",True),("XaWDJxgb1Q4","Lumi Patch","EN",True),("wzXYRicPb5M","Rocket Patch","US",True),
 ("ml23Q4Ri8j4","REM Patch","ES",True),("9KnTbvGlFtE","Lumi Patch","ES",True),("Qd1TK5hhRqw","Boost Patch","ES",True),
 ("cdijfMQuRvA","Hvordan Freedom Patch fungerer","DK",True),("ZDiafYmS3wg","Hvordan REM Patch fungerer","DK",True),("sqTKP4ETPfA","Sådan laver du demoen med Jay","DK",True)]

e=html.escape
PLAY='<span class="sl-play" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor"><path d="M8 5.5v13a1 1 0 0 0 1.5.86l10.4-6.5a1 1 0 0 0 0-1.72L9.5 4.64A1 1 0 0 0 8 5.5z"/></svg></span>'
def grid(lst):
    return '<div class="sl-videos">'+''.join(f'<button type="button" class="sl-video" data-yt="{i}"><span class="sl-video-thumb"><img src="assets/yt/{i}.webp" alt="" loading="lazy">{PLAY}</span><span class="sl-video-meta"><span class="sl-lang">{l}</span><span class="sl-video-title">{e(t)}</span></span></button>' for i,t,l,z in lst if z)+'</div>'
S=[s for s in shorts if s[2]]; W=[w for w in weitere if w[3]]
body=f'''<div class="sl-ambient" aria-hidden="true"></div>
<main class="sl-col">
<header class="sl-hero"><img src="assets/hero.webp" alt="Melanie N. Seyfarth mit den Super Patch Sorten" class="sl-hero-img"><div class="sl-hero-fade"></div>
<div class="sl-hero-text"><h1 class="sl-name">{e(profil["name"])}</h1><p class="sl-role">{e(profil["person"])} · {e(profil["rolle"])}</p>
<div class="sl-social"><a href="{profil["instagram"]}" target="_blank" rel="noopener noreferrer" aria-label="Instagram" class="sl-social-btn"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg></a>
<a href="{profil["youtube"]}" target="_blank" rel="noopener noreferrer" aria-label="YouTube" class="sl-social-btn"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M21.6 7.2a2.5 2.5 0 0 0-1.76-1.77C18.27 5 12 5 12 5s-6.27 0-7.84.43A2.5 2.5 0 0 0 2.4 7.2 26 26 0 0 0 2 12a26 26 0 0 0 .4 4.8 2.5 2.5 0 0 0 1.76 1.77C5.73 19 12 19 12 19s6.27 0 7.84-.43a2.5 2.5 0 0 0 1.76-1.77A26 26 0 0 0 22 12a26 26 0 0 0-.4-4.8zM10 15V9l5.2 3L10 15z"/></svg></a></div></div></header>
<a href="{haupt["url"]}" target="_blank" rel="noopener noreferrer" class="sl-main-cta"><img src="{haupt["bild"]}" alt="" class="sl-main-cta-img"><span class="sl-main-cta-body"><span class="sl-main-cta-title">{e(haupt["titel"])}</span><span class="sl-main-cta-text">{e(haupt["text"])}</span></span><span class="sl-main-cta-arrow" aria-hidden="true">→</span></a>
<nav class="sl-links" aria-label="Links">{"".join(f'<a href="{u}" target="_blank" rel="noopener noreferrer" class="sl-link"><img src="{b}" alt="" class="sl-link-img"><span class="sl-link-body"><span class="sl-link-title">{e(t)}</span><span class="sl-link-text">{e(x)}</span></span><span class="sl-link-arrow" aria-hidden="true">›</span></a>' for t,x,u,b in links)}</nav>
<section class="sl-section"><h2 class="sl-h2">Kurz erklärt</h2><div class="sl-shorts">{"".join(f'<button type="button" class="sl-short" data-yt="{i}" data-tall="1"><img src="assets/yt/{i}.webp" alt="" loading="lazy" class="sl-short-img">{PLAY}<span class="sl-short-title">{e(t)}</span></button>' for i,t,z in S)}</div></section>
<section class="sl-section"><h2 class="sl-h2">Jay Dhaliwal, Gründer von Super Patch</h2><div class="sl-own">{"".join(f'<button type="button" class="sl-own-card" data-mp4="{d}"><span class="sl-own-thumb"><img src="{v}" alt="" loading="lazy">{PLAY}</span><span class="sl-own-title">{e(t)}</span><span class="sl-own-text">{e(x)}</span></button>' for d,v,t,x,z in eigene if z)}</div></section>
<section class="sl-section"><h2 class="sl-h2">Die Patches im Video</h2>{grid(videos)}
<details class="sl-more"><summary>Videos in anderen Sprachen ({len(W)})</summary>{grid(W)}</details>
<a href="{profil["youtube"]}" target="_blank" rel="noopener noreferrer" class="sl-yt-channel">Alle Videos auf YouTube ansehen</a></section>
<footer class="sl-footer"><a href="impressum.html">Impressum</a><span aria-hidden="true">·</span><a href="datenschutz.html">Datenschutz</a></footer>
</main>
<div class="sl-modal" id="modal" role="dialog" aria-modal="true" hidden><div class="sl-modal-box" id="box"></div><p class="sl-modal-note" id="note">Wiedergabe über YouTube</p></div>
<script>
const m=document.getElementById('modal'),box=document.getElementById('box'),note=document.getElementById('note');
function close(){{m.hidden=true;box.innerHTML='';document.body.style.overflow='';}}
function open(inner,tall,yt){{box.className='sl-modal-box '+(tall?'sl-tall':'sl-wide');box.innerHTML=inner+'<button type="button" class="sl-close" aria-label="Schließen">×</button>';note.hidden=!yt;m.hidden=false;document.body.style.overflow='hidden';box.querySelector('.sl-close').onclick=close;}}
document.querySelectorAll('[data-yt]').forEach(b=>b.addEventListener('click',()=>open('<iframe src="https://www.youtube-nocookie.com/embed/'+b.dataset.yt+'?autoplay=1&rel=0&playsinline=1" title="Video" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>',!!b.dataset.tall,true)));
document.querySelectorAll('[data-mp4]').forEach(b=>b.addEventListener('click',()=>open('<video src="'+b.dataset.mp4+'" controls autoplay playsinline></video>',true,false)));
m.addEventListener('click',ev=>{{if(ev.target===m)close();}});document.addEventListener('keydown',ev=>{{if(ev.key==='Escape'&&!m.hidden)close();}});
</script>'''
def page(title, inner, desc="Super Patch: Infos, Erfahrungsberichte, Videos und Kontakt zu Melanie.", extra=""):
    return f'''<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><meta name="author" content="Melanie N. Seyfarth">{extra}
<meta property="og:title" content="Superlifestyle4u · Melanie N. Seyfarth"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website"><meta property="og:image" content="https://rseyfarth.github.io/superlifestyle4u/assets/og.jpg"><meta property="og:url" content="https://rseyfarth.github.io/superlifestyle4u/"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/avatar.png"><link rel="apple-touch-icon" href="assets/avatar.png"><link rel="stylesheet" href="style.css"></head>
<body class="sl-page">{inner}</body></html>
'''
open('index.html','w').write(page("Superlifestyle4u · Melanie N. Seyfarth", body))
imp='''<main class="sl-col sl-legal"><a href="./" class="sl-back">← Zurück</a><h1>Impressum</h1><p>Angaben gemäß § 5 DDG</p>
<p>Melanie N. Seyfarth<br>Trakehner Str. 29<br>50735 Köln<br>Deutschland</p><h2>Kontakt</h2><p>E-Mail: <a href="mailto:seyfarth@my.com">seyfarth@my.com</a></p>
<h2>Hinweis</h2><p>Ich bin unabhängige Vertriebspartnerin von Super Patch. Diese Seite ist mein persönliches Angebot und keine Seite der Super Patch Company.</p></main>'''
ds='''<main class="sl-col sl-legal"><a href="./" class="sl-back">← Zurück</a><h1>Datenschutzerklärung</h1>
<h2>Verantwortliche</h2><p>Melanie N. Seyfarth, Trakehner Str. 29, 50735 Köln, Deutschland. E-Mail: <a href="mailto:seyfarth@my.com">seyfarth@my.com</a></p>
<h2>Keine Werbung, keine Tracking-Cookies</h2><p>Diese Seite zeigt keine Werbung, setzt keine Cookies und verwendet keine Analyse- oder Tracking-Werkzeuge. Schriften und Bilder werden direkt von dieser Seite geladen, nicht von Drittanbietern.</p>
<h2>Hosting</h2><p>Die Seite wird über GitHub Pages (GitHub Inc., USA) bereitgestellt. Beim Aufruf verarbeitet GitHub technisch notwendige Daten wie IP-Adresse, Datum und Uhrzeit sowie den aufgerufenen Inhalt, um die Seite auszuliefern und vor Missbrauch zu schützen (Art. 6 Abs. 1 lit. f DSGVO). Dabei kann eine Übermittlung in die USA stattfinden; GitHub ist nach dem EU-US Data Privacy Framework zertifiziert.</p>
<h2>YouTube-Videos</h2><p>Videos von YouTube werden erst geladen, wenn du sie antippst. Erst dann wird eine Verbindung zu YouTube (Google Ireland Limited) im erweiterten Datenschutzmodus (youtube-nocookie.com) hergestellt. Rechtsgrundlage ist deine Einwilligung durch das Antippen (Art. 6 Abs. 1 lit. a DSGVO).</p>
<h2>Links zu anderen Diensten</h2><p>Links zu Instagram, YouTube, Facebook, Telegram, WhatsApp und Super Patch führen zu den Seiten dieser Anbieter. Für die dortige Datenverarbeitung gelten deren Datenschutzerklärungen.</p>
<h2>Deine Rechte</h2><p>Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht auf Beschwerde bei einer Datenschutzaufsichtsbehörde. Schreib mir dazu einfach eine E-Mail.</p></main>'''
nr='<meta name="robots" content="noindex">'
open('impressum.html','w').write(page("Impressum · Superlifestyle4u", imp, extra=nr))
open('datenschutz.html','w').write(page("Datenschutz · Superlifestyle4u", ds, extra=nr))
