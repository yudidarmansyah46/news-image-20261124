"""Draw the 24 November 2026 world-news front page.

Fresh program written for the news-image-20261124 bounty.
Output: entry.png, 1024 x 1024 RGB, a newspaper front page with one
lead story and six numbered secondary stories, all reported on
Tuesday 24 November 2026.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 243, 230)
CARD = (255, 253, 246)
INK = (20, 20, 20)
RED = (176, 30, 36)
NAVY = (31, 58, 95)
SEA = (28, 68, 110)
GREY = (90, 86, 76)
GOLD = (212, 160, 40)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text into lines that fit width pixels."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        if not words:
            lines.append("")
            continue
        cur = words[0]
        for word in words[1:]:
            trial = cur + " " + word
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def draw_scene(d, x0, y0, x1, y1):
    """Small sea scene: dusk sky, sea, a warship, an explosion, drones."""
    d.rectangle([x0, y0, x1, y1], fill=SEA)
    # dusk sky band
    d.rectangle([x0, y0, x1, y0 + 52], fill=(233, 150, 70))
    d.ellipse([x0 + 12, y0 + 8, x0 + 52, y0 + 48], fill=(255, 226, 160))
    # distant coastline
    d.polygon([(x0, y0 + 52), (x0 + 70, y0 + 30), (x0 + 150, y0 + 52)],
              fill=(90, 70, 60))
    # sea waves
    for i, wy in enumerate((y0 + 96, y0 + 128, y0 + 158)):
        for wx in range(x0 + 10 + i * 23, x1 - 20, 46):
            d.arc([wx, wy, wx + 30, wy + 12], 0, 180, fill=(140, 180, 215), width=2)
    # warship silhouette
    hx, hy = x0 + 60, y1 - 62
    d.polygon([(hx, hy), (hx + 150, hy), (hx + 168, hy - 22),
               (hx + 118, hy - 22), (hx + 108, hy - 40), (hx + 78, hy - 40),
               (hx + 66, hy - 22), (hx + 18, hy - 22)], fill=(18, 24, 34))
    d.rectangle([hx + 84, hy - 58, hx + 90, hy - 40], fill=(18, 24, 34))
    # explosion burst above the ship
    ex, ey = hx + 150, hy - 78
    for r, col in ((34, (255, 120, 20)), (24, (255, 180, 40)), (13, (255, 230, 120))):
        d.ellipse([ex - r, ey - r, ex + r, ey + r], fill=col)
    # naval drones: small dark dots with rotors
    for dx, dy in ((x0 + 30, y0 + 66), (x1 - 60, y0 + 80), (x0 + 120, y0 + 62)):
        d.ellipse([dx - 5, dy - 3, dx + 5, dy + 3], fill=(20, 20, 20))
        d.line([dx - 10, dy - 6, dx + 10, dy - 6], fill=(20, 20, 20), width=2)
    # smoke
    for sx, sy, sr in ((ex - 26, ey - 34, 12), (ex - 8, ey - 48, 15), (ex + 14, ey - 40, 11)):
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(120, 118, 112))
    d.rectangle([x0, y0, x1, y1], outline=INK, width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # double outer border
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=3)
    d.rectangle([22, 22, W - 23, H - 23], outline=INK, width=1)

    # ---- masthead ----
    f_mast = font(SERIF_B, 76)
    d.text((W // 2, 100), "THE WORLD TODAY", font=f_mast, fill=INK, anchor="mm")
    d.line([36, 144, W - 36, 144], fill=INK, width=3)
    f_date = font(SANS_B, 30)
    d.text((W // 2, 166), "TUESDAY, 24 NOVEMBER 2026", font=f_date,
           fill=RED, anchor="mm")
    f_sub = font(SANS, 15)
    d.text((W // 2, 190), "ONE DAY'S WORLD NEWS IN ONE PAGE",
           font=f_sub, fill=GREY, anchor="mm")
    d.line([36, 204, W - 36, 204], fill=INK, width=2)

    # ---- lead story ----
    f_kick = font(SANS_B, 17)
    d.text((36, 222), "LEAD STORY  —  THE MEDITERRANEAN", font=f_kick, fill=RED)
    f_head = font(SERIF_B, 45)
    head_lines = ["UKRAINE SAYS IT SANK", "A RUSSIAN WARSHIP", "OFF LIBYA"]
    y = 246
    for line in head_lines:
        d.text((36, y), line, font=f_head, fill=INK)
        y += 52
    f_deck = font(SANS, 20)
    deck = ("Kyiv says seven naval drones sank the corvette Merkury at "
            "Benghazi. The UN seeks a probe as Tripoli demands answers "
            "from Kyiv.")
    deck_lines = wrap(d, deck, f_deck, 640)
    y = 408
    for line in deck_lines:
        d.text((36, y), line, font=f_deck, fill=INK)
        y += 27
    draw_scene(d, 700, 246, 988, 440)
    f_cap = font(SANS, 13)
    d.text((844, 450), "The Benghazi strike, as reported today",
           font=f_cap, fill=GREY, anchor="mm")
    d.line([36, 494, W - 36, 494], fill=INK, width=2)

    # ---- six numbered stories ----
    stories = [
        ("CLIMATE  •  ANTALYA",
         "COP31 climate talks collapse in Antalya",
         "More than 90 nations reject a draft deal that never names "
         "fossil fuels."),
        ("TECHNOLOGY  •  NVIDIA",
         "Nvidia brings back Jensen Huang as CEO",
         "Huang returns 11 days after quitting; the US blacklists chip "
         "firm Megaspeed."),
        ("MIDDLE EAST  •  THE GULF",
         "Gulf standoff deepens as Hormuz mines hit tankers",
         "Iran steps up attacks on Gulf sites; Trump warns of a \u201cvery "
         "traumatic\u201d outcome."),
        ("JUSTICE  •  MYANMAR",
         "Fourteen nations back ICJ Rohingya genocide ruling",
         "The UK, Spain, Canada and 11 more affirm the court\u2019s finding "
         "against Myanmar."),
        ("GAZA",
         "Israeli strikes in Gaza kill three, UN worker among them",
         "At least three dead, including an UNRWA worker, Al Jazeera "
         "reports."),
        ("DISASTER  •  NEPAL",
         "Magnitude 5.6 quake strikes Nepal near China border",
         "The tremor hits Koshi province, near the border with China."),
    ]
    f_num = font(SANS_B, 22)
    f_ckick = font(SANS_B, 13)
    f_chead = font(SERIF_B, 20)
    f_cbody = font(SANS, 14)
    card_w, card_h = 466, 126
    gap_x, gap_y = 16, 6
    x0, y0 = 36, 506
    for i, (kicker, headline, body) in enumerate(stories):
        cx = x0 + (i % 2) * (card_w + gap_x)
        cy = y0 + (i // 2) * (card_h + gap_y)
        d.rectangle([cx, cy, cx + card_w, cy + card_h], fill=CARD,
                    outline=INK, width=1)
        d.rectangle([cx, cy, cx + 6, cy + card_h], fill=RED)
        # number badge
        bx, by = cx + 20, cy + 16
        d.ellipse([bx, by, bx + 34, by + 34], fill=NAVY)
        d.text((bx + 17, by + 18), str(i + 1), font=f_num, fill=(255, 255, 255),
               anchor="mm")
        tx = cx + 66
        d.text((tx, cy + 18), kicker, font=f_ckick, fill=RED)
        head_wrapped = wrap(d, headline, f_chead, card_w - 82)
        hy = cy + 38
        for line in head_wrapped[:2]:
            d.text((tx, hy), line, font=f_chead, fill=INK)
            hy += 24
        body_wrapped = wrap(d, body, f_cbody, card_w - 82)
        byy = hy + 2
        for line in body_wrapped[:2]:
            d.text((tx, byy), line, font=f_cbody, fill=(40, 40, 40))
            byy += 18

    # ---- also today strip ----
    ay = y0 + 3 * card_h + 2 * gap_y + 10
    d.line([36, ay, W - 36, ay], fill=INK, width=2)
    f_also = font(SANS_B, 15)
    f_atext = font(SANS, 15)
    also = ("UN chief urges a global AI safety framework within a year  •  "
            "Oregon and Virginia sue SpaceX over Grok images  •  Mexico to "
            "try \u201cEl Chapo Isidro\u201d at home  •  Russian jets enter South "
            "Korea\u2019s air defence zone")
    d.text((36, ay + 10), "ALSO TODAY", font=f_also, fill=RED)
    also_lines = wrap(d, also, f_atext, W - 72)
    yy = ay + 34
    for line in also_lines:
        d.text((36, yy), line, font=f_atext, fill=INK)
        yy += 21
    f_foot = font(SANS, 13)
    d.text((W // 2, H - 32),
           "All stories reported on Tuesday 24 November 2026",
           font=f_foot, fill=GREY, anchor="mm")

    img.save("entry.png", format="PNG", optimize=True)
    print("saved entry.png", img.size, img.mode)


if __name__ == "__main__":
    main()
