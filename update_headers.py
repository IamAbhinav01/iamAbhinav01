import re

with open("readme.md", "r", encoding="utf-8") as f:
    content = f.read()

# Pattern to find capsule-render images that have %200X%20
pattern = r'<img src="https://capsule-render\.vercel\.app/[^>]+%20(0[1-8])%20[^>]+/>'

def replace_header(match):
    num = match.group(1)
    return f'''  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./header_{num}_dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./header_{num}_light.svg">
    <img alt="Header {num}" src="./header_{num}_dark.svg" width="100%">
  </picture>'''

new_content = re.sub(pattern, replace_header, content)

with open("readme.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Headers replaced successfully.")
