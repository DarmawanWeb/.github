"""Render a commit and repository count card for a GitHub organization."""
import json, os, re, sys, urllib.request

org, out, accent = sys.argv[1], sys.argv[2], sys.argv[3]
token = os.environ["GH_TOKEN"]


def get(url):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r), r.headers.get("Link", "")


repos, page = [], 1
while True:
    batch, _ = get(f"https://api.github.com/orgs/{org}/repos?per_page=100&type=all&page={page}")
    repos += batch
    if len(batch) < 100:
        break
    page += 1

commits = 0
for repo in repos:
    if repo.get("size", 0) == 0:
        continue
    try:
        data, link = get(f"https://api.github.com/repos/{org}/{repo['name']}/commits?per_page=1")
    except Exception:
        continue
    m = re.search(r'page=(\d+)>; rel="last"', link)
    commits += int(m.group(1)) if m else len(data)

public = sum(1 for r in repos if not r.get("private"))
stats = [("Commits", f"{commits:,}"), ("Repositories", str(len(repos))), ("Public", str(public)),
         ("Stars", str(sum(r.get("stargazers_count", 0) for r in repos)))]
w = 720
cells = "".join(
    f'<text x="{60 + i * 170}" y="78" font-size="30" font-weight="700" fill="#{accent}" text-anchor="middle">{v}</text>'
    f'<text x="{60 + i * 170}" y="104" font-size="13" fill="#8B949E" text-anchor="middle">{k}</text>'
    for i, (k, v) in enumerate(stats))
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="130" viewBox="0 0 {w} 130" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif">
  <text x="20" y="30" font-size="18" fill="#{accent}">Commits across {org}</text>
  <g transform="translate(40 0)">{cells}</g>
</svg>
"""
open(out, "w").write(svg)
print(stats)
