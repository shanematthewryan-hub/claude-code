# -*- coding: utf-8 -*-
"""Renders the A4 email sheet — the companion to the A3 phone board.

Same data, same units, same colours, same order, so a name sits in the same
place on both sheets. Only rows that actually have an address appear here.

  SCALE=1.0 COLS='[[...],[...]]' COLGAPS='[0,0]' python3 build_emails.py
"""
import os, sys, json, html

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from directory_data import CARDS

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = open(os.path.join(HERE, 'inter-latin.css')).read()
e = html.escape

# ---------------------------------------------------------------- rows
# "— Desk" and "— Mobile" are phone concepts; on an email sheet they are noise.
PHONE_SUFFIXES = (" — Desk", " — Mobile")


def clean(name):
    for suffix in PHONE_SUFFIXES:
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return name


def email_cards():
    """CARDS in A3 order, keeping only rows with a real address.

    An address is listed once, at its first appearance, so the sheet stays a
    list of addresses rather than a transcript of the phone board.
    """
    seen, out = set(), []
    for card in CARDS:
        title, tone, rows = card[0], card[1], card[2]
        keep = []
        for name, _ext, addr, _mob in rows:
            if not addr or "@" not in addr or addr in seen:
                continue
            seen.add(addr)
            keep.append((clean(name), addr))
        if keep:
            out.append((title, tone, keep))
    return out


CARDS_E = email_cards()
TOTAL = sum(len(c[2]) for c in CARDS_E)

card_html = []
for i, (title, tone, rows) in enumerate(CARDS_E):
    body = "".join(
        '<div class="r"><span class="nm">%s</span><span class="ml">%s</span></div>'
        % (e(name), e(addr))
        for name, addr in rows
    )
    card_html.append(
        '<section class="card t-%s" data-i="%d"><h2>%s</h2><div class="rows">%s</div></section>'
        % (tone, i, e(title), body)
    )

COLS = json.loads(os.environ.get("COLS") or "[]")
GAPS = json.loads(os.environ.get("COLGAPS") or "[]")
if COLS:
    cards = "".join(
        '<div class="col" style="--ge:%.1fpx">%s</div>'
        % (GAPS[c] if c < len(GAPS) else 0.0, "".join(card_html[i] for i in grp))
        for c, grp in enumerate(COLS)
    )
else:
    cards = "".join(card_html)

HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Stakelums Email Directory — A4</title>
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

.page{width:210mm;height:297mm;background:var(--bg);
  padding:6mm 6mm 5mm;display:flex;flex-direction:column;margin:0 auto;overflow:hidden}

/* ---------- masthead ---------- */
.mast{display:flex;align-items:flex-end;justify-content:space-between;
  border-bottom:1mm solid var(--red);padding-bottom:1.6mm;margin-bottom:2.6mm}
.brand{display:flex;align-items:baseline;gap:3.5mm}
.brand b{font-size:17pt;font-weight:800;letter-spacing:-.018em;color:var(--red);line-height:.95}
.brand span{font-size:11pt;font-weight:600;letter-spacing:.05em;color:var(--ink);text-transform:uppercase}
.meta{text-align:right;line-height:1.4}
.meta .big{font-size:9pt;font-weight:700;color:var(--ink)}
.meta .big em{font-style:normal;font-weight:600;color:var(--muted);font-size:6.6pt;
  letter-spacing:.09em;text-transform:uppercase;margin-right:1.4mm}
.meta .sub{font-size:6.6pt;color:var(--muted);font-weight:500}

/* ---------- columns ---------- */
.grid{flex:1;display:flex;gap:3mm;align-items:flex-start}
.grid.flow{display:block;column-count:2;column-gap:3mm;column-fill:balance}
.col{flex:1;min-width:0}
.col .card:last-child{margin-bottom:0}
.card{background:var(--paper);border:.28mm solid var(--line);border-radius:1.6mm;
  overflow:hidden;margin-bottom:calc(2.4mm*var(--s) + var(--ge,0px));
  break-inside:avoid;page-break-inside:avoid;box-shadow:0 .3mm .9mm rgba(16,24,40,.05)}
.card h2{background:var(--c);color:#fff;font-size:calc(7pt*var(--s));font-weight:800;
  letter-spacing:.085em;text-transform:uppercase;
  padding:calc(1.4mm*var(--s)) 2.2mm calc(1.35mm*var(--s))}
.rows{padding:0}

/* ---------- one contact ---------- */
.r{padding:calc(1mm*var(--s)) 2.2mm;border-top:.2mm solid #F1F3F5;
   display:flex;flex-direction:column;gap:.15mm}
.r:first-child{border-top:0}
.r:nth-child(even){background:#F5F7F9}
.nm{font-size:calc(8.4pt*var(--s));font-weight:700;color:#12171C;
  line-height:1.15;letter-spacing:-.008em}
/* the address is the payload here, so it is set to be read, not skimmed past */
.ml{font-size:calc(8pt*var(--s));font-weight:500;color:var(--c);
  line-height:1.2;letter-spacing:-.004em;word-break:break-all}

/* ---------- tones ---------- */
.t-red{--c:var(--red)} .t-orange{--c:var(--orange)} .t-blue{--c:var(--blue)}
.t-green{--c:var(--green)} .t-slate{--c:var(--slate)} .t-dark{--c:var(--dark)}
.t-slate .ml,.t-dark .ml{color:#3D4650}

/* ---------- foot ---------- */
.foot{display:flex;justify-content:space-between;align-items:baseline;gap:4mm;
  padding-top:2mm;margin-top:2.4mm;border-top:.28mm solid #DCE0E5;
  font-size:6.6pt;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
.foot b{color:var(--red);font-weight:800}

@page{size:A4 portrait;margin:0}
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
    <div class="brand"><b>STAKELUMS</b><span>Email Directory</span></div>
    <div class="meta">
      <div class="big"><em>Main</em>(0504) 21900</div>
      <div class="sub">Updated September 2026 &nbsp;·&nbsp; %(total)d addresses</div>
    </div>
  </header>

  <main class="grid%(flowcls)s">%(cards)s</main>

  <footer class="foot">
    <span>Companion sheet &nbsp;·&nbsp; phone extensions are on the <b>A3 internal directory</b></span>
    <span>Trade 800 &nbsp;·&nbsp; Retail 401 &nbsp;·&nbsp; Deliveries 517</span>
  </footer>

</div>
</body></html>
""" % {
    "font": FONT,
    "scale": os.environ.get("SCALE", "1"),
    "total": TOTAL,
    "cards": cards,
    "flowcls": ("" if COLS else " flow"),
}

out = os.environ.get("OUT", os.path.join(HERE, "stakelums-email-directory-a4.html"))
open(out, "w").write(HTML)
print(out, os.path.getsize(out), "|", TOTAL, "addresses in", len(CARDS_E), "cards")
