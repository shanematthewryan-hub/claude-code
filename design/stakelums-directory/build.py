# -*- coding: utf-8 -*-
import os, html, io

FONT = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inter-latin.css')).read()

# ---------------------------------------------------------------- data
# row = (name, ext, email, mobile)
QUICK = [
    ("Builders",         "507",  "red"),
    ("Trade Electrical", "503",  "red"),
    ("Plumbing",         "505",  "red"),
    ("Flooring",         "510",  "red"),
    ("Paint",            "1200", "red"),
    ("Beds",             "409",  "red"),
    ("Bathrooms",        "411",  "red"),
    ("Stoves",           "413",  "red"),
    ("Expert",           "900",  "orange"),
    ("Tool Hire",        "1100", "blue"),
    ("Josie Hayes",      "518",  "slate"),
    ("Niamh Irwin",      "515",  "slate"),
]

CARDS = [
 ("KEY CONTACTS", "slate", [
    ("Trade Reception",     "501", None, None),
    ("Trade (All Phones)",  "800", None, None),
    ("Retail Reception",    "401", None, None),
    ("Deliveries Desk",     "517", None, None),
    ("Niamh Irwin",         "515", None, None),
    ("Josie Hayes A/C In",  "518", None, None),
    ("Beds Department",     "409", None, None),
    ("Paint",               "407 / 408", None, None),
 ]),
 ("UNIT 5 — ADMIN", "red", [
    ("Pat Stakelum",                    "517", "pat@stakelums.ie", None),
    ("John Stakelum",                   "516", "john@stakelums.ie", None),
    ("Breda Stakelum",                  "307", "breda@stakelums.ie", None),
    ("Eamonn Nolan",                    None,  "eamonn@stakelums.ie", "087 661 1563"),
    ("Niamh Irwin",                     "515", "niamh@stakelums.ie", None),
    ("Joe Connolly — Desk",             "304", "joe@stakelums.ie", None),
    ("Joe Connolly — Mobile",           None,  None, "086 823 1699"),
    ("Nicola McLoughlin — Payroll",     "602", "santina@stakelums.ie", None),
    ("Triona O’Dwyer — HR / Accounts",  "601", "trina@stakelums.ie", None),
    ("Marie Loughnane — Accounts Out",  "603", "marie.loughnane@stakelums.ie", None),
    ("Mary Fitzgibbon — Accounts Out",  "604", "mary.fitzgibbon@stakelums.ie", None),
    ("Josie Hayes — Accounts In",       "518", "josie@stakelums.ie", None),
    ("Jess O’Malley",                   "610", "jessica@stakelums.ie", None),
    ("Robert Harris — Marketing",       "606", "marketing@stakelums.ie", None),
    ("Cash Office",                     "406", None, None),
    ("Homewares Office",                "414", None, None),
 ]),
 ("UNIT 5 — TRADE DEPARTMENT", "red", [
    ("Trade Reception",             "501", "info@stakelums.ie", None),
    ("Trade Reception 2",           "502", None, None),
    ("Trade (All Phones)",          "800", None, None),
    ("Trade Counter 1 — Electrical","503 / 504", "electrical@stakelums.ie", None),
    ("Trade Counter 2 — Plumbing",  "505 / 506", "homeheat@stakelums.ie", None),
    ("Trade Counter 3 — Builders",  "507 / 508 / 509", None, None),
    ("James Kennedy",               "513", "james@stakelums.ie", None),
 ]),
 ("UNIT 5 — TRADE SALES", "red", [
    ("Podge Kiely", "512", "salesoffice@stakelums.ie", None),
    ("John Tynan",  "514", "johntynan@stakelums.ie", None),
 ]),
 ("UNIT 5 — WEB SALES", "red", [
    ("Web Office",                   None,  "websales@stakelums.ie", None),
    ("Brid Skelly",                  "607", "brid@stakelums.ie", None),
    ("Caroline Shanahan — Accounts", "605", "caroline@stakelums.ie", None),
 ]),
 ("UNIT 5 — DOORS & FLOORS", "red", [
    ("David Nessbert", "510", "doorsandfloors@stakelums.ie", None),
 ]),
 ("GROUP RING — ALL PHONES", "slate", [
    ("Trade — every trade phone",      "800",  None, None),
    ("Expert — every Expert phone",    "900",  None, None),
    ("Hire — every Unit 2 phone",      "1100", None, None),
    ("Paint — both paint counters",    "1200", None, None),
    ("Showrooms — bathrooms & stoves", "1300", None, None),
 ], "Dial from any internal handset. Group numbers ring every phone in that department. M marks a mobile."),
 ("UNIT 4 — MAIN SHOP", "red", [
    ("Customer Service / Checkout 01", "401", "retail@stakelums.ie", None),
    ("Customer Service 02",            "402", None, None),
    ("Retail Checkout Till 03",        "403", None, None),
    ("Retail Checkout Till 04",        "404", None, None),
    ("Retail Checkout Till 05",        "405", None, None),
    ("Jay Connors — Mobile",           None,  "jay.connors@stakelums.ie", "087 950 6311"),
    ("Lyndsey Dunphy — Mobile",        None,  "lyndsey@stakelums.ie", "087 213 9533"),
    ("Breda Stakelum — Homeware",      "307", "breda@stakelums.ie", None),
    ("Simon Pink — Desk",              "414", None, None),
 ]),
 ("UNIT 4 — BEDS / FURNITURE", "red", [
    ("Jay Connors — Desk",   "409", "jay.connors@stakelums.ie", None),
    ("Jay Connors — Mobile", None,  None, "087 950 6311"),
 ]),
 ("UNIT 4 — PAINT", "red", [
    ("Paint Counter 1",      "407", "paint@stakelums.ie", None),
    ("Paint Counter 2",      "408", None, None),
    ("Paint Counter — Direct","0504 29813", None, None),
    ("Paint (All Phones)",   "1200", None, None),
 ]),
 ("UNIT 4 — BATHROOMS", "red", [
    ("Bathrooms Desk 1",    "411", "showrooms@stakelums.ie", None),
    ("Bathrooms Desk 2",    "412", None, None),
    ("Anita O’Dowd — Desk", "410", "anita.kennedy@stakelums.ie", None),
 ]),
 ("UNIT 4 — STOVES", "red", [
    ("Stoves Desk",           "413",  "stovecentre@stakelums.ie", None),
    ("Showrooms (All Phones)","1300", None, None),
 ]),
 ("UNIT 4 — GARDEN CENTRE", "green", [
    ("Garden Centre", "704", None, None),
 ]),
 ("UNIT 3 — EXPERT", "orange", [
    ("Expert Counter 1",    "301", "expert@stakelums.ie", None),
    ("Expert Counter 2",    "302", None, None),
    ("Expert Counter 3",    "303", None, None),
    ("Expert Floor",        "306", None, None),
    ("Expert (All Phones)", "900", None, None),
    ("Cordless",            "710", None, None),
    ("Colm Fitzgibbon",     "308", "colm@stakelums.ie", None),
 ]),
 ("UNIT 2 — HIRE", "blue", [
    ("Hire (All Phones)", "1100", None, None),
    ("Counter 1",         "201",  "unit2@stakelums.ie", None),
    ("Counter 2",         "202",  None, None),
    ("Tom Stakelum — Desk","204", "tom@stakelums.ie", None),
 ]),
 ("UNIT 1 — GOODS IN", "dark", [
    ("Rocky (Martin)", "519", "goodsinwards@stakelums.ie", None),
    ("Kevin Trayer",   None,  None, "087 275 8167"),
 ]),
 ("STORE YARD — DELIVERIES", "dark", [
    ("Deliveries Desk", "517", "deliveries@stakelums.ie", None),
    ("Pat Stakelum",    "517", "pat@stakelums.ie", None),
    ("Paddy Stakelum",  None,  "paddy@stakelums.ie", "086 214 7908"),
 ]),
 ("STORE YARD — DINANS", "dark", [
    ("Stakelums Office Supplies", "0504 21888", "E41 H9C7", None),
    ("The Runner Bean — Louise",  None, None, "087 853 6339"),
 ]),
]

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
