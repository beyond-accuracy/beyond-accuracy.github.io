"""Build ../index.html (the served page) from src/page.html. Run after editing page.html.

page.html holds the head assets (stylesheets and the <style> block, up to the "Title" marker)
followed by the body. This script moves the head part into <head> and adds the meta tags.
"""
from pathlib import Path

here = Path(__file__).parent
src = (here / "page.html").read_text(encoding="utf-8").replace("<title>Beyond Accuracy</title>\n", "", 1)
marker = "<!-- ───────── Title ───────── -->"
head_assets, body = src.split(marker, 1)
body = marker + body

URL = "https://beyond-accuracy.github.io/"
TITLE = "Beyond Accuracy: Auditing Agent-Removal Sensitivity in Motion Forecasting"
DESC = ("NeurIPS 2026 E&D Track. Which surrounding agents does a motion forecast depend on? "
        "Leave-one-out agent removal audits five models on Argoverse 2 and Waymo.")
IMAGE = URL + "static/images/overview.png"
DESC_ATTR = DESC.replace("&", "&amp;")  # DESC goes into HTML attributes
ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' "
        "height='32' rx='7' fill='%23151B20'/%3E%3Cpath d='M3 16h6M13 16h6M23 16h6' stroke='%23E9AE2E' stroke-width='2.5' "
        "stroke-linecap='round'/%3E%3Crect x='10' y='7' width='12' height='6' rx='1.5' fill='%23EEF2F4'/%3E%3Crect x='10' "
        "y='19' width='12' height='6' rx='1.5' fill='none' stroke='%23E9AE2E' stroke-width='1.5' stroke-dasharray='2 2'/%3E%3C/svg%3E")

head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{DESC_ATTR}">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC_ATTR}">
<meta property="og:image" content="{IMAGE}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{DESC_ATTR}">
<meta name="twitter:image" content="{IMAGE}">
<link rel="icon" href="{ICON}">
{head_assets.strip()}
</head>
<body>
"""
(here.parent / "index.html").write_text(head + body.rstrip() + "\n</body>\n</html>\n", encoding="utf-8")
print("wrote index.html")
