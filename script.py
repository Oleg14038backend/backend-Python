from github import Github, Auth
import os

# Берём токен из переменной окружения
token = os.getenv("")
if not token:
    raise ValueError("⚠️ Не найден токен. Установи переменную окружения")

auth = Auth.Token(token)
g = Github(auth=auth)

repo = g.get_user().get_repo("backend-Python")

with open("issues.md", "r", encoding="utf-8") as f:
    content = f.read().split("### #")

for block in content[1:]:
    lines = block.splitlines()
    title = "#" + lines[0].strip()
    body = "\n".join(lines[1:])
    repo.create_issue(title=title, body=body)

print("✅ Все Issues успешно созданы!")
