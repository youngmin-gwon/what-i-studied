import os
import re

target_dir = "/Users/youngmin/Documents/Obsidian/what-i-studied/02_references/oop/design_pattern"
exclude_files = {"Command Pattern.md", "Memento Pattern.md", "Chain of Responsibility Pattern.md"}

# Regex to match Markdown links: [Title](Path)
# Negative lookbehind (?<!!) ensures we don't match images ![Title](Path)
# We assume standard links without nested parentheses in the URL for simplicity,
# but handle the case of standard relative paths well.
link_regex = re.compile(r'(?<!\!)\[([^\]]+)\]\(([^)]+)\)')

def fix_links():
    count = 0
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if not file.endswith(".md"):
                continue
            if file in exclude_files:
                print(f"Skipping excluded file: {file}")
                continue

            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            def replace_callback(match):
                text = match.group(1)
                url = match.group(2)
                
                # Check if the URL starts with ../
                if url.startswith("../"):
                    # Remove the first occurrence of ../
                    # This effectively reduces the relative depth by 1
                    new_url = url[3:]
                    print(f"[{file}] Fixing link: '{url}' -> '{new_url}'")
                    return f"[{text}]({new_url})"
                
                return match.group(0)

            new_content = link_regex.sub(replace_callback, content)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                
    print(f"Total files updated: {count}")

if __name__ == "__main__":
    fix_links()
