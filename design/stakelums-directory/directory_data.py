# -*- coding: utf-8 -*-
"""Contact data for the Stakelums directory sheets.

Single source of truth: build.py renders the A3 phone board from it and
build_emails.py renders the A4 email sheet from the same rows, so the two
sheets can never drift apart.

CARDS entries are (title, tone, rows[, note]); a row is
(name, extension, email, mobile) with None for anything absent.
"""

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
