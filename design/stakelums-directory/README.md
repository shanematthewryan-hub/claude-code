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

**Adding or removing people:** edit the `CARDS` list in `build.py`, then:

```bash
cd design/stakelums-directory
SCALE=1.12 COLS='[[0,1],[2,3,4,5,6],[7,8,9,10,11],[12,13,14,15,16,17]]' python3 build.py
```

`SCALE` sets the type size and `COLS` assigns cards (by list position) to the four
columns. After adding rows, drop `SCALE` a notch or move a card to another column
if the page overflows.

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
