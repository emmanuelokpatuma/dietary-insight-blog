"""Make a 1080x1350 (4:5) Instagram/Facebook image for every blog post."""
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from pins import THEME, GREEN, F, ROOT


def font(name, size):
    return ImageFont.truetype(str(F / name), size)


def make_ig(title, category, slug, out_dir, kicker=None, footer="Link in bio · @dietaryinsightapp"):
    out = out_dir / f"{slug}.jpg"
    col, soft = THEME.get(category, (GREEN, (231, 242, 234)))
    W, H = 1080, 1350
    im = Image.new("RGB", (W, H), soft)
    d = ImageDraw.Draw(im)
    d.ellipse((620, -300, 1400, 480), fill=tuple(min(255, c + 12) for c in soft))
    tag = font("LiberationSans-Bold.ttf", 34)
    label = (kicker or category).upper()
    tw = d.textlength(label, font=tag)
    d.rounded_rectangle((70, 80, 70 + tw + 52, 140), 30, fill=(255, 255, 255))
    d.text((96, 92), label, font=tag, fill=col)
    size = 100
    while True:
        tf = font("LiberationSerif-Bold.ttf", size)
        lines = textwrap.wrap(title, width=max(8, int(18 * 100 / size)))
        if len(lines) * size * 1.12 < 470 or size < 60:
            break
        size -= 6
    y = 190
    for ln in lines:
        d.text((70, y), ln, font=tf, fill=(20, 33, 26))
        y += int(size * 1.12)
    shot = ROOT / "static/img/app-swaps.webp"
    if shot.exists():
        s = Image.open(shot).convert("RGB")
        s = s.resize((440, int(440 * s.height / s.width)))
        frame = Image.new("RGB", (s.width + 20, s.height + 20), (17, 17, 17))
        frame.paste(s, (10, 10))
        top = max(y + 30, 690)
        crop_h = H - 130 - top
        frame = frame.crop((0, 0, frame.width, min(frame.height, crop_h)))
        im.paste(frame, (W - frame.width - 70, top))
    sub, reg = font("LiberationSans-Bold.ttf", 42), font("LiberationSans-Regular.ttf", 36)
    by = max(y + 60, 760)
    d.text((70, by), "Check any meal", font=sub, fill=GREEN)
    d.text((70, by + 52), "in one photo", font=sub, fill=GREEN)
    for i, t in enumerate(["Allergen alerts", "Sugar, salt & fat", "Healthier swaps"]):
        d.ellipse((70, by + 146 + i * 64, 96, by + 172 + i * 64), fill=col)
        d.text((114, by + 138 + i * 64), t, font=reg, fill=(60, 70, 64))
    d.rectangle((0, H - 130, W, H), fill=GREEN)
    logo = ROOT / "static/img/icon-180.png"
    if logo.exists():
        lg = Image.open(logo).convert("RGBA").resize((86, 86))
        im.paste(lg, (70, H - 108), lg)
    d.text((176, H - 104), "Dietary Insight", font=sub, fill=(255, 255, 255))
    d.text((176, H - 56), footer, font=font("LiberationSans-Regular.ttf", 30), fill=(214, 240, 201))
    im.save(out, "JPEG", quality=90, optimize=True)
    return out


def make_og(title, category, slug, out_dir):
    """1200x630 link-preview image (Facebook, Flipboard, LinkedIn, X)."""
    out = out_dir / f"{slug}.jpg"
    col, soft = THEME.get(category, (GREEN, (231, 242, 234)))
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), soft)
    d = ImageDraw.Draw(im)
    d.ellipse((820, -260, 1460, 380), fill=tuple(min(255, c + 12) for c in soft))
    tag = font("LiberationSans-Bold.ttf", 28)
    label = category.upper()
    tw = d.textlength(label, font=tag)
    d.rounded_rectangle((60, 54, 60 + tw + 44, 104), 25, fill=(255, 255, 255))
    d.text((82, 64), label, font=tag, fill=col)
    size = 78
    while True:
        tf = font("LiberationSerif-Bold.ttf", size)
        lines = textwrap.wrap(title, width=max(10, int(24 * 78 / size)))
        if len(lines) * size * 1.12 < 330 or size < 46:
            break
        size -= 4
    y = 135
    for ln in lines:
        d.text((60, y), ln, font=tf, fill=(20, 33, 26))
        y += int(size * 1.12)
    d.rectangle((0, H - 110, W, H), fill=GREEN)
    logo = ROOT / "static/img/icon-180.png"
    if logo.exists():
        lg = Image.open(logo).convert("RGBA").resize((76, 76))
        im.paste(lg, (60, H - 93), lg)
    d.text((156, H - 92), "Dietary Insight Blog", font=font("LiberationSans-Bold.ttf", 36), fill=(255, 255, 255))
    d.text((156, H - 48), "blog.simplerlivez.com", font=font("LiberationSans-Regular.ttf", 26), fill=(214, 240, 201))
    im.save(out, "JPEG", quality=88, optimize=True)
    return out
