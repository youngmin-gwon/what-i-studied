import os
import re

target_dir = "/Users/youngmin/Documents/Obsidian/what-i-studied/02_references/oop"

# Regex explanation:
# (\*\*.*?\*\*) : Group 1. Matches **content** non-greedily. 
#                 Matches literal **, ANY character (non-greedy), literal **.
# ([가-힣a-zA-Z0-9]) : Group 2. Matches a Korean char, letter, or digit immediately following Group 1.
# We do NOT match if followed by space, punctuation (.,), newline, etc.
pattern = re.compile(r'(\*\*.*?\*\*)([가-힣a-zA-Z0-9])')

def fix_bold_spacing():
    count_files = 0
    count_substitutions = 0
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if not file.endswith(".md"):
                continue
                
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Using function in sub to debug/count if needed, but simple sub is fine
            new_content, n = pattern.subn(r'\1 \2', content)
            
            if n > 0:
                print(f"Fixing {n} issues in: {file}")
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count_files += 1
                count_substitutions += n

    print(f"Finished. Modified {count_files} files with {count_substitutions} fixes.")

if __name__ == "__main__":
    fix_bold_spacing()
