"""Refresh the post list between BLOG:START and BLOG:END in README.md from the Medium feed."""
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

FEED = "https://indranilroy9.medium.com/feed"
COUNT = 5
README = "README.md"
# A post is listed only if it carries at least one of these tags. Edit freely.
TAGS = {
    "incident-response", "threat-hunting", "red-teaming", "red-team", "purple-team",
    "pentesting", "cloud-security", "digital-forensics", "endpoint-security",
    "detection-engineering", "threat-intelligence", "malware-analysis",
}
BLOCK = re.compile(r"(<!-- BLOG:START -->)(.*?)(<!-- BLOG:END -->)", re.S)


def fetch_posts():
    req = urllib.request.Request(FEED, headers={"User-Agent": "profile-readme-refresh"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        root = ET.fromstring(resp.read())
    posts = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").split("?")[0]
        stamp = item.findtext("pubDate")
        tags = {c.text for c in item.findall("category") if c.text}
        if title and link and stamp and tags & TAGS:
            posts.append((parsedate_to_datetime(stamp), title, link))
    posts.sort(reverse=True)
    return posts[:COUNT]


def render(posts):
    lines = [f"- [{t.replace('[', '(').replace(']', ')')}]({u})" for _, t, u in posts]
    return "\n" + "\n".join(lines) + "\n"


def main():
    posts = fetch_posts()
    if not posts:
        sys.exit("no matching posts in the feed; README left unchanged")
    with open(README, encoding="utf-8") as fh:
        text = fh.read()
    if not BLOCK.search(text):
        sys.exit("BLOG markers not found in README.md")
    new = BLOCK.sub(lambda m: m.group(1) + render(posts) + m.group(3), text)
    if new != text:
        with open(README, "w", encoding="utf-8") as fh:
            fh.write(new)


if __name__ == "__main__":
    main()
