"""Make a tall Pinterest/Instagram image (1000x1500) for every blog post."""
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
F = ROOT / "fonts"
THEME = {  # category -> (main colour, soft colour)
    "Diabetes and food": ((47, 143, 70), (231, 244, 228)), "Diabetes basics": ((37, 99, 168), (228, 238, 249)),
    "Blood pressure": ((194, 65, 12), (253, 238, 226)), "Heart health": ((190, 18, 60), (253, 231, 236)),
    "Food allergies": ((124, 58, 237), (239, 232, 253)), "African and Caribbean food": ((180, 83, 9), (253, 241, 220)),
    "Eating out": ((15, 118, 110), (223, 244, 241)), "Healthy eating": ((77, 124, 15), (238, 246, 220)),
    "Seasonal": ((162, 28, 175), (248, 230, 250)),
}
GREEN = (14, 90, 58)


def make_pin(title, category, slug, out_dir):
    out = out_dir / f"{slug}.jpg"
    col, soft = THEME.get(category, (GREEN, (231, 242, 234)))
    W, H = 1000, 1500
    im = Image.new("RGB", (W, H), (251, 249, 243))
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 760), fill=soft)
    d.ellipse((560, -260, 1320, 500), fill=tuple(min(255, c + 12) for c in soft))
    tag = ImageFont.truetype(str(F / "LiberationSans-Bold.ttf"), 34)
    tw = d.textlength(category.upper(), font=tag)
    d.rounded_rectangle((70, 80, 70 + tw + 52, 140), 30, fill=(255, 255, 255))
    d.text((96, 92), category.upper(), font=tag, fill=col)
    size = 96
    while True:
        tf = ImageFont.truetype(str(F / "LiberationSerif-Bold.ttf"), size)
        lines = textwrap.wrap(title, width=max(8, int(17 * 96 / size)))
        if len(lines) * size * 1.12 < 560 or size < 60:
            break
        size -= 6
    y = 190
    for ln in lines:
        d.text((70, y), ln, font=tf, fill=(20, 33, 26))
        y += int(size * 1.12)
    shot = ROOT / "static/img/app-swaps.webp"
    if shot.exists():
        s = Image.open(shot).convert("RGB")
        s = s.resize((520, int(520 * s.height / s.width)))
        frame = Image.new("RGB", (s.width + 24, s.height + 24), (17, 17, 17))
        frame.paste(s, (12, 12))
        im.paste(frame, (W - frame.width - 60, 700))
    sub = ImageFont.truetype(str(F / "LiberationSans-Bold.ttf"), 40)
    reg = ImageFont.truetype(str(F / "LiberationSans-Regular.ttf"), 34)
    d.text((70, 820), "Check any meal", font=sub, fill=GREEN)
    d.text((70, 870), "in one photo", font=sub, fill=GREEN)
    for i, t in enumerate(["Allergen alerts", "Sugar, salt & fat", "Healthier swaps"]):
        d.ellipse((70, 960 + i * 62, 94, 984 + i * 62), fill=col)
        d.text((112, 952 + i * 62), t, font=reg, fill=(60, 70, 64))
    d.rectangle((0, H - 150, W, H), fill=GREEN)
    logo = ROOT / "static/img/icon-180.png"
    if logo.exists():
        lg = Image.open(logo).convert("RGBA").resize((96, 96))
        im.paste(lg, (70, H - 123), lg)
    d.text((190, H - 118), "Dietary Insight Blog", font=sub, fill=(255, 255, 255))
    d.text((190, H - 70), "blog.simplerlivez.com", font=reg, fill=(214, 240, 201))
    im.save(out, "JPEG", quality=88, optimize=True)
    return out
