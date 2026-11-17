import os
import re
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fragment.txt")
with open(FILENAME, "r", encoding="utf-8") as f:
    lines = [re.sub(r"\s+", " ", line.strip()) for line in f]
with open(FILENAME, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
words = re.findall(r"[a-z]+(?:'[a-z]+)?", " ".join(lines).lower())
print("Кількість рядків тексту:", len([l for l in lines if l]))
print("Кількість оригінальних слів:", len(set(words)))