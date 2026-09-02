# Stakelums Internal Directory — A3

Single-sheet **A3 landscape (420 × 297 mm)** wall directory, rebuilt from
`source-Stakelums_Store_Directory_A3_Editable.xlsx`.

| File | Use |
| --- | --- |
| `stakelums-internal-directory-a3.pdf` | Send to the printer. A3, landscape, borderless-safe (9 mm margins). |
| `stakelums-internal-directory-a3.html` | The design. Self-contained — fonts embedded, no network needed. Edit and re-print from any browser. |
| `preview.png` | Quick look. |
| `build.py` | Regenerates the HTML from structured data. |

## Editing

**Small change (a number, a name):** open the `.html`, find the text, edit, save,
then print to PDF with *A3 · Landscape · Background graphics on · Margins: none*.

**Adding or removing people:** edit the `CARDS` list in `directory_data.py`, then
rebuild both sheets:

```bash
cd design/stakelums-directory
SCALE=1.3 COLS='[[0,1],[2,3,4,5,6],[7,8,9,10,11],[12,13,14,15,16,17]]' \
  COLGAPS='[20,18.4,12.2,4.8]' python3 build.py

SCALE=1.14 COLS='[[0,1,2,3],[4,5,6,7,8,9,10,11,12]]' \
  COLGAPS='[1.0,12.3]' python3 build_emails.py
```

`SCALE` sets the type size, `COLS` assigns cards (by list position) to the four
columns, and `COLGAPS` is the extra space added between cards in each column so
all four columns finish level at the bottom. After adding rows, drop `SCALE` a
notch and set `COLGAPS` back to `[0,0,0,0]` if the page overflows.

## How it reads

Designed to be scanned from a few feet away, not read at a desk. Names print at
roughly 13 pt and extension numbers at roughly 17 pt on the A3 sheet.

Every contact is **one line**: name, then the number hard right in the zone
colour, so the colour of a number tells you which part of the site it rings.
Alternating row tints carry the eye across.

Email addresses are not printed. They duplicated the name they sat beside and
cost roughly a third of the sheet — that space is now type size. Two rows keep
an annotation because a name cannot give you the information: Web Office, which
has no phone number at all, and the Dinans Eircode. The addresses are all still
in `build.py` if they are ever wanted back on the sheet.

Neutral zones (Key Contacts, Group Ring, Goods In, Store Yard) keep their
slate header but print their numbers near-black — Key Contacts is the most-used
card on the sheet, so it is also the highest-contrast one.

## The email sheet

Same card structure as the A3, two columns on A4 portrait. Each entry is the
name over the full address, and the address prints in its unit's colour, the way
extension numbers do on the board. An address appears once, at its first
position in A3 order, so the sheet is a list rather than a transcript — Breda
Stakelum is filed under Unit 5 Admin, not repeated under Homeware. "— Desk" and
"— Mobile" are dropped from names here; they are phone concepts.

37 addresses. The footer points back to the A3 for extensions.

## Printing

A3, landscape, **100% scale**, background graphics on. The A4 email sheet prints
portrait at 100%, same settings. The sheet uses 6 mm
margins to win space for the type. If your printer cannot reach that close to
the edge, choose *Fit to printable area* — it scales by about 3%, which is not
noticeable.

## Colours

Taken from the source workbook.

| Zone | Hex |
| --- | --- |
| Unit 5 / Unit 4 headers | `#C91C23` |
| Unit 3 — Expert | `#FF7900` |
| Unit 2 — Hire | `#2055A6` |
| Unit 4 — Garden Centre | `#2C8A3E` |
| Key Contacts / Group Ring | `#59636E` |
| Goods In / Store Yard | `#34454D` |

Extension numbers are printed in their zone colour, so the colour of a number
tells you which part of the site it rings.

## Notes on the data

Two oddities carried over from the source workbook, unchanged:

1. Anita O'Dowd (Unit 4 — Bathrooms, ext 410) is listed with the address
   `anita.kennedy@stakelums.ie`.
2. Nicola McLoughlin (Payroll, ext 602) is listed with `santina@stakelums.ie`.
