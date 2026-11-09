"""Fetch the live site and compare it with the checked-out repository (standard library only).

  live_check.py --base-url URL [--tries 8] [--wait 15]

Every committed .html, .css, .png, .jpg, .svg, .mp4, .zip, .pdf and .md file outside .github is
fetched and its bytes must equal the committed file; every same-site link and image on
the pages found must resolve. Exit 1 on any difference.
"""
import argparse
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

EXT = {".html", ".css", ".png", ".jpg", ".jpeg", ".svg", ".mp4", ".zip", ".pdf", ".md", ".js", ".json"}
LINK = re.compile(r"""(?:href|src)\s*=\s*["']([^"'#]+)""", re.I)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "release-live-check"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def url_of(base, rel):
    rel = rel.as_posix()
    if rel == "index.html":
        return base + "/"
    if rel.endswith("/index.html"):
        return base + "/" + rel[: -len("index.html")]
    return base + "/" + urllib.parse.quote(rel)


def check(base):
    bad, pages = [], []
    for p in sorted(Path(".").rglob("*")):
        rel = p.relative_to(".")
        if not p.is_file() or rel.parts[0] in (".git", ".github") or p.suffix.lower() not in EXT:
            continue
        if p.suffix.lower() == ".md" and len(rel.parts) == 1:
            continue  # repository notes (README.md) are not served as pages
        try:
            data = fetch(url_of(base, rel))
        except urllib.error.URLError as why:
            bad.append(f"{rel}: {why}")
            continue
        if data != p.read_bytes():
            bad.append(f"{rel}: live bytes differ from the committed file")
        elif rel.suffix == ".html":
            pages.append((rel, data.decode("utf-8", "replace")))
    for rel, text in pages:
        for ref in LINK.findall(text):
            if re.match(r"^(mailto:|tel:|javascript:|data:)", ref):
                continue
            target = urllib.parse.urljoin(url_of(base, rel), ref)
            if not target.startswith(base):
                continue  # external links are not this site's to prove
            try:
                fetch(target)
            except urllib.error.URLError as why:
                bad.append(f"{rel}: link {ref} -> {why}")
    return len(pages), bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", required=True)
    ap.add_argument("--tries", type=int, default=8)
    ap.add_argument("--wait", type=float, default=15)
    a = ap.parse_args()
    base = a.base_url.rstrip("/")
    bad = ["not run"]
    for n in range(a.tries):
        pages, bad = check(base)
        if not bad:
            print(f"live check ok: {pages} pages and every file equal to the repository")
            return
        print(f"try {n + 1}/{a.tries}: {len(bad)} problem(s), first: {bad[0]}")
        time.sleep(a.wait)
    print("\n".join(bad))
    sys.exit(1)


if __name__ == "__main__":
    main()
