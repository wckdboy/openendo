#!/usr/bin/env python3
"""Generate the OpenEndo OpenGraph card (1200x630 PNG) in brand colors.

Brand tokens (BRAND.md): navy #1a1a2e bg, yellow #FFD60A, rose #e84a6f,
ink #1d1d1f, muted #6e6e73. Fonts: Fraunces (display) + Inter (text),
fetched once from the google/fonts repo into /tmp/oe_fonts.

Usage: python3 scripts/gen_og_card.py [out.png]
"""
import math
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

NAVY_TOP = (20, 20, 42)
NAVY_BOT = (33, 33, 62)
YELLOW = (255, 214, 10)
ROSE = (232, 74, 111)
WHITE = (255, 255, 255)
MUTED = (159, 164, 196)
FAINT = (120, 126, 160)
W, H = 1200, 630

FONT_DIR = Path("/tmp/oe_fonts")


def font(path: str, size: int, weight: int = 400, axes: list | None = None) -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(str(FONT_DIR / path), size)
    try:
        f.set_variation_by_axes(axes if axes is not None else ([0, 0, 144, weight] if "fraunces" in path else [14, weight]))
    except Exception:
        pass
    return f


def fetch_fonts() -> None:
    FONT_DIR.mkdir(exist_ok=True)
    wanted = {
        "fraunces.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/fraunces/Fraunces%5BSOFT%2CWONK%2Copsz%2Cwght%5D.ttf",
        "inter.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bopsz%2Cwght%5D.ttf",
    }
    for name, url in wanted.items():
        if not (FONT_DIR / name).exists():
            urllib.request.urlretrieve(url, FONT_DIR / name)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def draw_flower(draw, cx, cy, petal_r, dist, center_r):
    # six petals around a yellow centre (flat, brand rose/yellow)
    for k in range(6):
        ang = math.pi / 3 * k - math.pi / 2
        px = cx + dist * math.cos(ang)
        py = cy + dist * math.sin(ang)
        draw.ellipse([px - petal_r, py - petal_r, px + petal_r, py + petal_r], fill=ROSE)
    draw.ellipse([cx - center_r, cy - center_r, cx + center_r, cy + center_r], fill=YELLOW)


def fit(draw, text, f, max_w):
    while draw.textbbox((0, 0), text, font=f)[2] > max_w and f.size > 40:
        f = font(f.path.split("/")[-1], f.size - 4, 600, [0, 0, 144, 600] if "fraunces" in f.path else [14, 600])
    return f


def main(out: str = "docs/assets/og-card.png") -> None:
    fetch_fonts()
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    for y in range(H):
        d.line([(0, y), (W, y)], fill=lerp(NAVY_TOP, NAVY_BOT, y / H))

    # soft rose glow behind the flower
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([850, 130, 1210, 500], fill=ROSE + (110,))
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
    d = ImageDraw.Draw(img)

    # flower mark (right)
    draw_flower(d, 1030, 315, 62, 84, 52)

    # eyebrow
    f_eyebrow = font("inter.ttf", 27, 700, [14, 700])
    d.text((90, 118), "FOR THE 190 MILLION WOMEN WITH ENDOMETRIOSIS", font=f_eyebrow, fill=YELLOW)

    # title
    f_title = font("fraunces.ttf", 150, 620, [0, 0, 144, 620])
    f_title = fit(d, "OpenEndo", f_title, 760)
    d.text((84, 160), "OpenEndo", font=f_title, fill=WHITE)

    # divider
    d.rounded_rectangle([92, 348, 168, 356], radius=4, fill=YELLOW)

    # taglines
    d.text((90, 384), "Open data hub for endometriosis research", font=font("inter.ttf", 40, 500, [14, 500]), fill=(221, 224, 244))
    d.text((90, 442), "Clinical trials \u00b7 papers \u00b7 funding \u00b7 policy \u2014 refreshed weekly", font=font("inter.ttf", 27, 400, [14, 400]), fill=MUTED)

    # footer
    d.text((90, 540), "openendo.org", font=font("inter.ttf", 30, 700, [14, 700]), fill=YELLOW)
    d.text((300, 546), "MIT \u00b7 open source \u00b7 humans & AI agents welcome", font=font("inter.ttf", 25, 400, [14, 400]), fill=FAINT)

    Path(out).parent.mkdir(exist_ok=True, parents=True)
    img.save(out, optimize=True)
    print(f"saved {out} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "docs/assets/og-card.png")
