# -*- coding: utf-8 -*-
import os, sys, html, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

FONT = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inter-latin.css')).read()

from directory_data import QUICK, CARDS


e = html.escape

def row_html(name, ext, email, mob):
    """One line: name, then the number hard right.

    Email addresses are not printed beside names — they duplicate the name and
    cost the type size. The grey annotation slot is kept only for information a
    name cannot give you (an Eircode), and a row with no phone number at all
    falls back to showing its address in the number slot.
    """
    annot = email if (email and "@" not in email) else ""
    who = '<span class="nm">%s</span>' % e(name)
    if annot:
        who += '<span class="em">%s</span>' % e(annot)

    extcls = "ext multi" if ext and "/" in ext else "ext"
    if ext and mob:
        val = '<span class="%s">%s</span><span class="ext mob"><i>M</i>%s</span>' % (extcls, e(ext), e(mob))
    elif ext:
        val = '<span class="%s">%s</span>' % (extcls, e(ext))
    elif mob:
        val = '<span class="ext mob"><i>M</i>%s</span>' % e(mob)
    elif email:
        val = '<span class="ext addr">%s</span>' % e(email)
    else:
        val = ""
    return '<div class="r"><div class="w">%s</div><div class="v">%s</div></div>' % (who, val)

import json
card_html = []
for i, c in enumerate(CARDS):
    title, tone, rows = c[0], c[1], c[2]
    note = c[3] if len(c) > 3 else None
    body = "".join(row_html(*r) for r in rows)
    if note:
        body += '<p class="note">%s</p>' % e(note)
    card_html.append('<section class="card t-%s" data-i="%d"><h2>%s</h2><div class="rows">%s</div></section>'
                     % (tone, i, e(title), body))

COLS = json.loads(os.environ.get("COLS") or "[]")
if COLS:
    GAPS = json.loads(os.environ.get("COLGAPS") or "[]")
    cards = "".join(
        '<div class="col" style="--ge:%.1fpx">%s</div>'
        % (GAPS[c] if c < len(GAPS) else 0.0, "".join(card_html[i] for i in grp))
        for c, grp in enumerate(COLS))
else:
    cards = "".join(card_html)

tiles = "".join(
    '<div class="tile t-%s"><span class="tl">%s</span><span class="tn">%s</span></div>' % (tone, e(lab), e(num))
    for lab, num, tone in QUICK)

HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Stakelums Internal Directory — A3</title>
<style>
%(font)s
:root{
  --red:#C91C23; --orange:#FF7900; --blue:#2055A6; --green:#2C8A3E;
  --slate:#59636E; --dark:#34454D; --ink:#1B2229; --text:#20272F;
  --muted:#7A828C; --line:#E4E7EB; --paper:#FFFFFF; --bg:#EEF0F3;
  --s:%(scale)s;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#8A8F96}
body{font-family:'Inter',"Helvetica Neue",Arial,sans-serif;color:var(--text);
  -webkit-font-smoothing:antialiased;font-feature-settings:"tnum" 1,"cv05" 1;}

.page{
  width:420mm;height:297mm;background:var(--bg);
  padding:6mm 6mm 5mm;display:flex;flex-direction:column;
  margin:0 auto;overflow:hidden;
}

/* ---------- masthead ---------- */
.mast{display:flex;align-items:flex-end;justify-content:space-between;
  border-bottom:1mm solid var(--red);padding-bottom:1.6mm;margin-bottom:2.4mm}
.brand{display:flex;align-items:baseline;gap:5mm}
.brand b{font-size:21pt;font-weight:800;letter-spacing:-.018em;color:var(--red);line-height:.95}
.brand span{font-size:13.5pt;font-weight:600;letter-spacing:.055em;color:var(--ink);text-transform:uppercase}
.meta{text-align:right;line-height:1.45}
.meta .big{font-size:11.5pt;font-weight:700;color:var(--ink);letter-spacing:-.01em}
.meta .big em{font-style:normal;font-weight:600;color:var(--muted);font-size:8pt;
  letter-spacing:.09em;text-transform:uppercase;margin-right:2mm}
.meta .sub{font-size:7.8pt;color:var(--muted);font-weight:500}
.meta .sub b{color:var(--ink);font-weight:700}

/* ---------- quick strip ---------- */
.quick{background:var(--paper);border:.28mm solid var(--line);border-radius:1.6mm;
  padding:1.8mm 2.2mm 2mm;margin-bottom:2.4mm;box-shadow:0 .3mm .9mm rgba(16,24,40,.05)}
.quick h1{font-size:7.4pt;font-weight:800;letter-spacing:.13em;text-transform:uppercase;
  color:var(--muted);margin-bottom:1.5mm;display:flex;align-items:center;gap:2.5mm}
.quick h1:after{content:"";flex:1;height:.25mm;background:var(--line)}
.tiles{display:grid;grid-template-columns:repeat(12,1fr);gap:1.6mm}
.tile{background:#F7F8FA;border:.25mm solid var(--line);border-top:1mm solid var(--c);
  border-radius:1.2mm;padding:1.3mm 1.8mm 1.4mm;display:flex;flex-direction:column;gap:.2mm}
.tile .tl{font-size:7pt;font-weight:700;letter-spacing:.075em;text-transform:uppercase;color:var(--muted);
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tile .tn{font-size:19pt;font-weight:800;letter-spacing:-.02em;color:var(--c);line-height:1}

/* ---------- columns ---------- */
.grid{flex:1;display:flex;gap:3mm;align-items:flex-start}
.grid.flow{display:block;column-count:4;column-gap:3mm;column-fill:balance}
.col{flex:1;min-width:0}
.col .card:last-child{margin-bottom:0}
.card{background:var(--paper);border:.28mm solid var(--line);border-radius:1.6mm;
  overflow:hidden;margin-bottom:calc(2.5mm*var(--s) + var(--ge,0px));break-inside:avoid;page-break-inside:avoid;
  box-shadow:0 .3mm .9mm rgba(16,24,40,.05)}
.card h2{background:var(--c);color:#fff;font-size:calc(7.9pt*var(--s));font-weight:800;letter-spacing:.085em;
  text-transform:uppercase;padding:calc(1.5mm*var(--s)) 2.2mm calc(1.45mm*var(--s))}
.rows{padding:0}
.r{display:flex;align-items:baseline;gap:1.8mm;padding:calc(.88mm*var(--s)) 2.2mm;
   border-top:.2mm solid #F1F3F5}
.r:first-child{border-top:0}
.r:nth-child(even){background:#F5F7F9}
.w{flex:1;min-width:0;display:flex;flex-wrap:wrap;align-items:baseline;
   column-gap:1.8mm;row-gap:.2mm;overflow:hidden}
.nm{font-size:calc(10pt*var(--s));font-weight:600;color:#12171C;line-height:1.2;
  letter-spacing:-.008em;white-space:nowrap}
.em{font-size:calc(7.2pt*var(--s));font-weight:500;color:#8A919A;line-height:1.15;
  white-space:nowrap;flex:0 0 auto}
.v{display:flex;align-items:baseline;justify-content:flex-end;gap:1.4mm;flex:none}
.ext{font-size:calc(13pt*var(--s));font-weight:800;color:var(--c);line-height:1.1;letter-spacing:-.022em;white-space:nowrap}
.ext.multi{font-size:calc(9.6pt*var(--s));letter-spacing:-.015em}
.ext.addr{font-size:calc(8.8pt*var(--s));font-weight:600;color:#4A525B;letter-spacing:0}
.ext.mob{font-size:calc(9pt*var(--s));font-weight:700;color:var(--ink);letter-spacing:-.01em}
.ext.mob i{font-style:normal;font-size:calc(6.2pt*var(--s));font-weight:800;letter-spacing:.06em;
  color:#fff;background:var(--muted);border-radius:.7mm;padding:.25mm .8mm;
  margin-right:1.1mm;position:relative;top:-.4mm}

.note{font-size:calc(7pt*var(--s));line-height:1.4;color:var(--muted);font-weight:500;
  padding:calc(1.4mm*var(--s)) 2.2mm calc(1.2mm*var(--s));border-top:.22mm solid #EFF1F4;background:#FAFBFC}

/* ---------- tones ---------- */
.t-red{--c:var(--red)} .t-orange{--c:var(--orange)} .t-blue{--c:var(--blue)}
.t-green{--c:var(--green)} .t-slate{--c:var(--slate)} .t-dark{--c:var(--dark)}
/* neutral zones: header keeps its tone, numbers go near-black so the most
   frequently dialled card is also the highest-contrast one */
.t-slate .ext,.t-dark .ext{color:#12171C}

@page{size:A3 landscape;margin:0}
@media print{
  html,body{background:#fff}
  .page{margin:0;box-shadow:none}
  *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
}
@media screen{ .page{box-shadow:0 4mm 12mm rgba(0,0,0,.28);margin:6mm auto} }
</style></head>
<body>
<div class="page">

  <header class="mast">
    <div class="brand"><b>STAKELUMS</b><span>Internal Directory</span></div>
    <div class="meta">
      <div class="big"><em>Main</em>(0504) 21900 &nbsp;&nbsp;<em>Trade</em>800</div>
      <div class="sub">Updated September 2026 &nbsp;·&nbsp; Dial the extension from any internal handset</div>
    </div>
  </header>

  <div class="quick">
    <h1>Quick transfers</h1>
    <div class="tiles">%(tiles)s</div>
  </div>

  <main class="grid%(flowcls)s">%(cards)s</main>


</div>
</body></html>
""" % {"font": FONT, "tiles": tiles, "scale": os.environ.get("SCALE","1"), "cards": cards, "flowcls": ("" if COLS else " flow")}

out = os.environ.get("OUT", "/home/user/claude-code/design/stakelums-directory/stakelums-internal-directory-a3.html")
open(out, "w").write(HTML)
print(out, os.path.getsize(out))
