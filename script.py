from github import Github
import os

# токен GitHub (создаётся в Settings -> Developer settings -> PAT)
g = Github("")
repo = g.get_user().get_repo("backend-Python")

with open("issues.md", "r", encoding="utf-8") as f:
    content = f.read().split("### #")

for block in content[1:]:  # первый кусок до ### #3 — шапка
    lines = block.splitlines()
    title = "#" + lines[0].strip()
    body = "\n".join(lines[1:])
    repo.create_issue(title=title, body=body)
