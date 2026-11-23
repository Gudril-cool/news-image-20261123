#!/usr/bin/env python3
"""Compose the entry image for make.fun's news-image-20261123 bounty.

Draws a one-page newspaper front page that sums up the world news of
Monday 23 November 2026, as reported that day (Just Security's Early
Edition of 23 Nov 2026, Reuters wires and the day's news digests):

  lead   Iran's missile and drone strikes on Bahrain (US positions and a
         civilian industrial plant) and tankers targeted in the Strait of
         Hormuz; Trump says Tehran wants a deal, "not an acceptable one".
  panel  COP31 in Turkiye ends with no deal - the longest UN climate
         conference in history, split over fossil fuels and money.
  panel  Russian strikes kill a child and a young woman in Kryvyi Rih and
         hit homes near Kyiv; Ukraine says its naval drones sank the
         Russian corvette Mercury in Benghazi, Libya.
  panel  The ICJ rules Myanmar committed genocide against the Rohingya.
  panel  US Democrats win at least 258 House seats, their largest
         majority in decades; Trump moves to curb oversight.
  panel  Israel's PM-elect Eisenkot calls settler arson attacks on
         Palestinian villages "Jewish terrorism"; a strike on a truck in
         Gaza kills three.
  panel  An Anthropic mathematician and Claude claim a proof of the
         Riemann Hypothesis, open for over 160 years.
  strip  Taiwan stocks plunge from their record peak; Nvidia jumps;
         Sinaloa cartel leader "Chapo Isidro" captured in Mexico;
         Bangladesh says Sheikh Hasina faces arrest if she returns.

Everything is drawn with PIL shapes and real fonts, so every word stays
crisp - no generated raster text anywhere. Output: entry.png, 1024x1024.

Layout revision (2026-11-23): panel type enlarged and each panel set in
a ruled cell, and the lead illustration given a lit horizon, a wake and
a navigation light - all so the page stays legible at thumbnail size.
"""

from PIL import Image, ImageDraw, ImageFont

W = 1024
PAPER = (248, 245, 238)
INK = (20, 24, 29)
NAVY = (29, 53, 87)
RED = (179, 52, 31)
GOLD = (201, 147, 43)
GREY = (92, 96, 102)
PANEL_LINE = (198, 192, 178)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, W), PAPER)
d = ImageDraw.Draw(img)

M = 36  # page margin


def centered(text, y, fnt, fill=INK):
    box = d.textbbox((0, 0), text, font=fnt)
    d.text(((W - (box[2] - box[0])) / 2, y), text, font=fnt, fill=fill)


def wrap(text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if d.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- masthead
d.line([(M, 26), (W - M, 26)], fill=INK, width=5)
d.line([(M, 34), (W - M, 34)], fill=INK, width=2)
centered("THE WORLD IN ONE DAY", 44, font(SERIF_B, 55))
d.line([(M, 122), (W - M, 122)], fill=INK, width=2)
d.line([(M, 128), (W - M, 128)], fill=INK, width=5)

# ---------------------------------------------------------------- date band
d.rectangle([M, 142, W - M, 208], fill=NAVY)
centered("MONDAY  23 NOVEMBER 2026", 156, font(SANS_B, 43), fill=(255, 255, 255))

# ---------------------------------------------------------------- lead story
LY = 226
# illustration: night strait, tanker silhouette, missile trails and bursts
d.rectangle([M, LY, M + 296, LY + 196], fill=(16, 26, 44))
d.ellipse([M + 226, LY + 18, M + 268, LY + 60], fill=(238, 230, 200))  # moon
for sx, sy in [(30, 30), (90, 64), (180, 96), (52, 120), (250, 130)]:
    d.ellipse([M + sx, LY + sy, M + sx + 5, LY + sy + 5], fill=(210, 216, 230))
# lit horizon band, then the sea
d.rectangle([M, LY + 124, M + 296, LY + 140], fill=(33, 52, 82))
d.rectangle([M, LY + 140, M + 296, LY + 196], fill=(24, 52, 84))
# wake trailing behind the hull
d.polygon([(M + 58, LY + 166), (M + 8, LY + 181), (M + 64, LY + 181)], fill=(58, 88, 128))
# tanker hull + bridge + containers
d.polygon([(M + 40, LY + 150), (M + 250, LY + 150), (M + 232, LY + 168), (M + 58, LY + 168)], fill=(12, 14, 18))
d.rectangle([M + 196, LY + 128, M + 226, LY + 150], fill=(12, 14, 18))
d.ellipse([M + 208, LY + 120, M + 215, LY + 127], fill=(255, 70, 50))  # navigation light
for i, c in enumerate([(179, 52, 31), (201, 147, 43), (70, 110, 160)]):
    d.rectangle([M + 62 + i * 42, LY + 132, M + 98 + i * 42, LY + 150], fill=c)
# missile trails
d.line([(M + 30, LY + 16), (M + 130, LY + 92)], fill=(255, 170, 60), width=4)
d.line([(M + 96, LY + 8), (M + 176, LY + 84)], fill=(255, 170, 60), width=4)
for bx, by in [(130, 92), (176, 84)]:
    d.ellipse([M + bx - 13, LY + by - 13, M + bx + 13, LY + by + 13], fill=(255, 120, 40))
    d.ellipse([M + bx - 6, LY + by - 6, M + bx + 6, LY + by + 6], fill=(255, 210, 90))

LX = M + 320
d.text((LX, LY - 4), "THE LEAD STORY · THE GULF", font=font(SANS_B, 19), fill=RED)
lead_head = wrap("IRAN STRIKES BAHRAIN; TANKERS HIT IN HORMUZ", font(SANS_B, 41), W - M - LX)
yy = LY + 26
for line in lead_head:
    d.text((LX, yy), line, font=font(SANS_B, 41), fill=INK)
    yy += 50
lead_sub = ("Missiles and drones hit US positions and a civilian plant in Bahrain. "
            "Trump: Tehran wants a deal — “not an acceptable one.”")
for line in wrap(lead_sub, font(SANS, 21), W - M - LX):
    d.text((LX, yy + 4), line, font=font(SANS, 21), fill=(52, 56, 62))
    yy += 29

d.line([(M, 446), (W - M, 446)], fill=INK, width=3)

# ---------------------------------------------------------------- panels
panels = [
    ("CLIMATE · TÜRKIYE", RED,
     "COP31 ENDS WITH NO DEAL",
     "The longest climate summit in history closes split over fossil fuels and money."),
    ("UKRAINE WAR", NAVY,
     "RUSSIAN STRIKES KILL A CHILD",
     "Kryvyi Rih and Kyiv homes hit; Ukraine says its drones sank a Russian warship in Libya."),
    ("THE HAGUE · JUSTICE", GOLD,
     "ICJ: MYANMAR COMMITTED GENOCIDE",
     "The World Court rules Myanmar's forces committed genocide against the Rohingya people."),
    ("WASHINGTON · POLITICS", NAVY,
     "DEMOCRATS WIN BIG HOUSE MAJORITY",
     "At least 258 seats, their largest in decades, as Trump moves to curb oversight."),
    ("GAZA & WEST BANK", RED,
     "SETTLER ARSON: “JEWISH TERRORISM”",
     "Israel's PM-elect Eisenkot condemns attacks on Palestinian villages; Gaza truck strike kills 3."),
    ("SCIENCE · MATHEMATICS", GOLD,
     "RIEMANN HYPOTHESIS “PROVED”",
     "An Anthropic mathematician and the Claude AI claim a proof of the 160-year-old problem."),
]

GX, GY = M, 462
CW, CH = (W - 2 * M - 20) // 2, 150
for i, (kicker, kc, head, sub) in enumerate(panels):
    x = GX + (i % 2) * (CW + 20)
    y = GY + (i // 2) * (CH + 9)
    # ruled cell: top and bottom rules make the grid read as columns
    d.line([(x, y), (x + CW, y)], fill=PANEL_LINE, width=2)
    d.line([(x, y + CH - 2), (x + CW, y + CH - 2)], fill=PANEL_LINE, width=2)
    d.text((x + 2, y + 9), kicker, font=font(SANS_B, 17), fill=kc)
    hy = y + 36
    for line in wrap(head, font(SANS_B, 25), CW - 4):
        d.text((x + 2, hy), line, font=font(SANS_B, 25), fill=INK)
        hy += 30
    for line in wrap(sub, font(SANS, 18), CW - 4):
        d.text((x + 2, hy + 2), line, font=font(SANS, 18), fill=(52, 56, 62))
        hy += 24

# ---------------------------------------------------------------- bottom strip
BY = 940
d.rectangle([M, BY, W - M, 996], fill=INK)
strip = ("ALSO MONDAY: Taiwan stocks plunge from their record peak · Nvidia jumps 7% · "
         "Sinaloa cartel leader “Chapo Isidro” captured in Mexico · Bangladesh: Hasina faces arrest if she returns")
sy = BY + 9
for line in wrap(strip, font(SANS_B, 16), W - 2 * M - 24):
    box = d.textbbox((0, 0), line, font=font(SANS_B, 16))
    d.text(((W - (box[2] - box[0])) / 2, sy), line, font=font(SANS_B, 16), fill=(240, 236, 224))
    sy += 22

img.save("entry.png", optimize=True)
print("wrote entry.png", img.size)
