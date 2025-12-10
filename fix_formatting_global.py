import os
import re

# Target the root directory of the vault
target_dir = "/Users/youngmin/Documents/Obsidian/what-i-studied"

# Improved Regex from v2
pattern_internal_1 = re.compile(r'\*\*\s+(.*?)\s*\*\*') 
pattern_internal_2 = re.compile(r'\*\*\s*(.*?)\s+\*\*')

# External spacing regex
external_space_pattern = re.compile(r'(\*\*.*?\*\*)([가-힣a-zA-Z0-9])')

def fix_formatting_global():
    count_files = 0
    count_fixes = 0
    
    for root, dirs, files in os.walk(target_dir):
        # Optional: Skip specific potentially huge or irrelevant folders if needed
        # e.g., if ".git" in dirs: dirs.remove(".git")
        if ".obsidian" in dirs:
            dirs.remove(".obsidian")
        if ".git" in dirs:
            dirs.remove(".git")
        if ".trash" in dirs:
            dirs.remove(".trash")

        for file in files:
            if not file.endswith(".md"):
                continue
                
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                print(f"Skipping file due to encoding error: {filepath}")
                continue
            
            original_content = content
            
            def internal_fix(match):
                inner = match.group(1).strip()
                return f"**{inner}**"
            
            # Fix internal spaces
            content = pattern_internal_1.sub(internal_fix, content)
            content = pattern_internal_2.sub(internal_fix, content)

            # Fix external spacing
            content = external_space_pattern.sub(r'\1 \2', content)
            
            if content != original_content:
                # print(f"Fixed formatting in: {file}") # reduce noise for global run
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count_files += 1
                count_fixes += 1

    print(f"Global Cleanup finished. Modified {count_files} files.")

if __name__ == "__main__":
    fix_formatting_global()
