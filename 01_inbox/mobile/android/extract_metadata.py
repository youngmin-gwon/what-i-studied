import os, glob
import re

dirs = [
    "/Users/youngmin/Documents/Obsidian/what-i-studied/01_inbox/mobile/android/01_system_internals/boot-and-runtime",
    "/Users/youngmin/Documents/Obsidian/what-i-studied/01_inbox/mobile/android/01_system_internals/ipc-and-process",
    "/Users/youngmin/Documents/Obsidian/what-i-studied/01_inbox/mobile/android/01_system_internals/kernel-and-hal"
]

for d in dirs:
    print(f"\n\n=== {d} ===")
    for f in sorted(glob.glob(os.path.join(d, "**/*.md"), recursive=True)):
        if f.endswith('contracts.md') and 'contracts/' in f:
            continue
        with open(f, 'r') as file:
            content = file.read()
            title = ""
            m = re.search(r'title:\s*(.*)', content)
            if m: title = m.group(1).strip()
            alias = ""
            m = re.search(r'aliases:\s*\[(.*?)\]', content)
            if m: alias = m.group(1).strip()
            # extract first H2
            h2 = ""
            m2 = re.search(r'^##\s+(.*)', content, re.MULTILINE)
            if m2: h2 = m2.group(1).strip()
            print(f"File: {os.path.basename(f)}")
            print(f"Title: {title}")
            print(f"Alias: {alias}")
            print(f"H2: {h2}")
            print("---")
