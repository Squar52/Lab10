import os
import shutil
FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "MY_FILES")
if not os.path.isdir(FOLDER):
    os.makedirs(FOLDER)
    for name in ["a.txt", "b.txt", "c.txt", "d.jpg", "e.jpg", "f.png", "g.pdf",
                 "h.pdf", "i.docx", "j.docx", "k.py", "l.py", "m.mp3", "n.csv",
                 "o.csv", "p.zip"]:
        open(os.path.join(FOLDER, name), "w").close()
for name in os.listdir(FOLDER):
    path = os.path.join(FOLDER, name)
    if os.path.isfile(path):
        ext = os.path.splitext(name)[1][1:].lower() or "no_extension"
        os.makedirs(os.path.join(FOLDER, ext), exist_ok=True)
        shutil.move(path, os.path.join(FOLDER, ext, name))
        print(f"{name} -> {ext}/")