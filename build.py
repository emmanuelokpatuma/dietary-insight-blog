#!/usr/bin/env python3
"""Build the Dietary Insight blog into ./public (static HTML, no server needed).

Posts live in content/posts/YYYY-MM-DD-slug.md with YAML front matter:
  title, description (<=155 chars), keywords [..], category, date, updated?,
  faq: [{q, a}], sources: [{title, url}], draft: false
"""
import datetime as dt, html, json, math, re, shutil, sys
from pathlib import Path
from email.utils import format_datetime
import markdown, yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent
OUT = ROOT / "public"
SITE = yaml.safe_load((ROOT / "site.yml").read_text())
env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html", "xml"]))
MD = markdown.Markdown(extensions=["extra", "toc", "sane_lists", "smarty"], extension_configs={"toc": {"permalink": False}})


THEMES = {
    "Diabetes and food": ("#2f8f46", "#e7f4e4", "plate"),
    "Diabetes basics": ("#2563a8", "#e4eef9", "info"),
    "Blood pressure": ("#c2410c", "#fdeee2", "heart"),
    "Heart health": ("#be123c", "#fde7ec", "heart"),
    "Food allergies": ("#7c3aed", "#efe8fd", "shield"),
    "African and Caribbean food": ("#b45309", "#fdf1dc", "bowl"),
    "Eating out": ("#0f766e", "#dff4f1", "bag"),
    "Healthy eating": ("#4d7c0f", "#eef6dc", "leaf"),
    "Seasonal": ("#a21caf", "#f8e6fa", "star"),
}
DEFAULT_THEME = ("#0e5a3a", "#e7f2ea", "leaf")


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def read_doc(path):
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        sys.exit(f"{path}: missing front matter")
    meta = yaml.safe_load(m.group(1)) or {}
    MD.reset()
    body = MD.convert(m.group(2))
    meta["toc"] = getattr(MD, "toc_tokens", [])
    meta["html"] = body
    meta["words"] = len(re.sub(r"<[^>]+>", " ", body).split())
    meta["minutes"] = max(1, math.ceil(meta["words"] / 220))
    return meta


def app_links():
    a, u = SITE["app"], SITE["utm"]
    sep = lambda url: "&" if "?" in url else "?"
    return {"play": a["play_url"] + sep(a["play_url"]) + u, "ios": a["ios_url"] + sep(a["ios_url"]) + u}


def load_posts():
    posts, today = [], dt.date.today()
    for p in sorted((ROOT / "content/posts").glob("*.md")):
        meta = read_doc(p)
        if meta.get("draft"):
            continue
        d = meta["date"] if isinstance(meta["date"], dt.date) else dt.date.fromisoformat(str(meta["date"]))
        if d > today:  # scheduled for later
            continue
        meta["date"] = d
        meta["updated"] = meta.get("updated") or d
        meta["slug"] = meta.get("slug") or re.sub(r"^\d{4}-\d{2}-\d{2}-", "", p.stem)
        meta["url"] = f"/{meta['slug']}/"
        meta["category"] = meta.get("category", "Healthy eating")
        meta["cat_url"] = f"/topics/{slugify(meta['category'])}/"
        meta["theme"] = THEMES.get(meta["category"], DEFAULT_THEME)
        for k, lim in (("title", 65), ("description", 160)):
            if len(meta.get(k, "")) > lim:
                print(f"WARN {p.name}: {k} is {len(meta[k])} chars (aim <= {lim})")
        posts.append(meta)
    posts.sort(key=lambda x: x["date"], reverse=True)
    return posts


def related(post, posts, n=3):
    kw = set(map(str.lower, post.get("keywords", [])))
    score = lambda o: (o["category"] == post["category"]) * 2 + len(kw & set(map(str.lower, o.get("keywords", []))))
    others = [o for o in posts if o is not post]
    return sorted(others, key=lambda o: (score(o), o["date"]), reverse=True)[:n]


def write(path, text):
    f = OUT / path.lstrip("/")
    if path.endswith("/"):
        f = f / "index.html"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT)
    posts = load_posts()
    ctx = {"site": SITE, "links": app_links(), "year": dt.date.today().year,
           "categories": sorted({p["category"]: p["cat_url"] for p in posts}.items()),
           "themes": THEMES, "default_theme": DEFAULT_THEME}

    for p in posts:
        write(p["url"], env.get_template("post.html").render(**ctx, post=p, related=related(p, posts)))

    per = SITE["posts_per_page"]
    pages = [posts[i:i + per] for i in range(0, max(len(posts), 1), per)] or [[]]
    for i, chunk in enumerate(pages):
        url = "/" if i == 0 else f"/page/{i + 1}/"
        write(url, env.get_template("list.html").render(**ctx, posts=chunk, page=i + 1, pages=len(pages), canonical=url,
              heading=None, title=SITE["name"] + (f" – page {i + 1}" if i else ""), description=SITE["description"]))

    for cat, curl in ctx["categories"]:
        cp = [p for p in posts if p["category"] == cat]
        write(curl, env.get_template("list.html").render(**ctx, posts=cp, page=1, pages=1, canonical=curl, heading=cat,
              title=f"{cat} – {SITE['name']}", description=f"Guides on {cat.lower()} from the Dietary Insight team."))

    for pg in (ROOT / "content/pages").glob("*.md"):
        meta = read_doc(pg)
        meta["url"] = f"/{pg.stem}/"
        write(meta["url"], env.get_template("page.html").render(**ctx, page=meta))

    write("/404.html", env.get_template("page.html").render(**ctx, page={"title": "Page not found", "url": "/404.html",
          "description": "That page does not exist.", "noindex": True,
          "html": '<p>Sorry, that page has moved or never existed. <a href="/">Go to the latest articles</a>.</p>'}))

    # sitemap, robots, RSS
    urls = [("/", posts[0]["updated"] if posts else dt.date.today())] + [(p["url"], p["updated"]) for p in posts]
    urls += [(c, None) for _, c in ctx["categories"]] + [(f"/{pg.stem}/", None) for pg in (ROOT / "content/pages").glob("*.md")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, d in urls:
        sm.append(f"<url><loc>{SITE['url']}{u}</loc>" + (f"<lastmod>{d}</lastmod>" if d else "") + "</url>")
    write("/sitemap.xml", "\n".join(sm + ["</urlset>"]))
    if SITE.get("adsense_client"):
        pub = SITE["adsense_client"].replace("ca-", "")
        write("/ads.txt", f"google.com, {pub}, DIRECT, f08c47fec0942fa0\n")
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n")
    items = []
    for p in posts[:20]:
        when = format_datetime(dt.datetime.combine(p["date"], dt.time(7), dt.timezone.utc))
        items.append(f"<item><title>{html.escape(p['title'])}</title><link>{SITE['url']}{p['url']}</link>"
                     f"<guid>{SITE['url']}{p['url']}</guid><pubDate>{when}</pubDate>"
                     f"<description>{html.escape(p['description'])}</description></item>")
    write("/feed.xml", f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{html.escape(SITE["name"])}</title>'
          f"<link>{SITE['url']}/</link><description>{html.escape(SITE['description'])}</description>"
          f"<language>{SITE['lang']}</language>{''.join(items)}</channel></rss>")
    print(f"built {len(posts)} posts -> {OUT}")


if __name__ == "__main__":
    main()
