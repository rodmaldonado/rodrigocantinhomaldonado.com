from pathlib import Path
from bs4 import BeautifulSoup
import json
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "public").resolve()
errors = []
html_files = list(root.rglob("*.html"))

if not root.exists():
    print(f"missing site directory: {root}")
    sys.exit(1)

for file_path in html_files:
    soup = BeautifulSoup(file_path.read_text(encoding="utf-8"), "html.parser")
    rel = "/" + str(file_path.relative_to(root)).replace("index.html", "").replace("\\", "/")
    if file_path.name == "404.html":
        rel = "/404.html"

    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    description = soup.find("meta", attrs={"name": "description"})
    canonical = soup.find("link", rel="canonical")
    h1 = soup.find_all("h1")

    if not title:
        errors.append(f"{rel}: missing title")
    if not description or not description.get("content"):
        errors.append(f"{rel}: missing description")
    if not canonical or not canonical.get("href"):
        errors.append(f"{rel}: missing canonical")
    if len(h1) != 1:
        errors.append(f"{rel}: expected 1 h1, got {len(h1)}")

    for script in soup.find_all("script", type="application/ld+json"):
        try:
            json.loads(script.string or "")
        except Exception as exc:
            errors.append(f"{rel}: invalid JSON-LD {exc}")

    for anchor in soup.find_all("a", href=True):
        href = anchor["href"]
        if href.startswith("/") and not href.startswith("//") and "#" not in href:
            target = href.split("?")[0]
            if target.endswith("/"):
                destination = root / target.lstrip("/") / "index.html"
            else:
                destination = root / target.lstrip("/")
            if not destination.exists():
                errors.append(f"{rel}: broken internal link {href}")

sitemap_path = root / "sitemap.xml"
if not sitemap_path.exists():
    errors.append("sitemap: missing sitemap.xml")
else:
    sitemap = sitemap_path.read_text(encoding="utf-8")
    if "#" in sitemap:
        errors.append("sitemap: contains URL fragment")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print(f"OK: {len(html_files)} HTML files validated")
