import os
import re

target_dir = "/Users/youngmin/Documents/Obsidian/what-i-studied/02_references/oop"

# Regex to find bold tags with leading/trailing spaces INSIDE the tags
# Matches ** space ... ** or ** ... space **
# Note: This might be dangerous if the user INTENDED ** bold **.
# But standard Markdown bold usually implies tightly interacting tokens.
# We will trim whitespace inside **.
internal_space_pattern = re.compile(r'\*\*\s+(.*?)\s*\*\*') 
internal_space_pattern_2 = re.compile(r'\*\*\s*(.*?)\s+\*\*')

# Re-run external spacing fix just in case
external_space_pattern = re.compile(r'(\*\*.*?\*\*)([가-힣a-zA-Z0-9])')

def cleanup_bold():
    count_files = 0
    count_fixes = 0
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if not file.endswith(".md"):
                continue
                
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 1. Fix internal spaces: ** text** -> **text**
            # Use a lambda to strip content
            # pattern: \*\*\s*(content)\s*\*\*
            # We want to replace matching block with **content**
            # Better regex: \*\*\s*(?P<content>.*?)\s*\*\* -> **\g<content>**
            # But we must be careful about greedy matching.
            # \s* includes newlines? No, usually . doesn't match newline.
            
            def internal_fix(match):
                inner = match.group(1).strip()
                return f"**{inner}**"
            
            # Use non-greedy match for content
            content = re.sub(r'\*\*\s+([^(*]+?)\s*\*\*', internal_fix, content)
            content = re.sub(r'\*\*\s*([^(*]+?)\s+\*\*', internal_fix, content)

            # 2. Fix external spacing (Re-run)
            content = external_space_pattern.sub(r'\1 \2', content)
            
            if content != original_content:
                print(f"Fixed formatting in: {file}")
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count_files += 1
                count_fixes += 1

    print(f"Cleanup finished. Modified {count_files} files.")

if __name__ == "__main__":
    cleanup_bold()
