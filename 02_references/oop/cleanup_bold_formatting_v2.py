import os
import re

target_dir = "/Users/youngmin/Documents/Obsidian/what-i-studied/02_references/oop"

# Improved Regex
# Matches ** space ... ** or ** ... space **
# Uses non-greedy .*? to allow any character (except newline) inside, including (
pattern_internal_1 = re.compile(r'\*\*\s+(.*?)\s*\*\*') 
pattern_internal_2 = re.compile(r'\*\*\s*(.*?)\s+\*\*')

# Re-run external spacing fix just in case
external_space_pattern = re.compile(r'(\*\*.*?\*\*)([가-힣a-zA-Z0-9])')

def cleanup_bold_v2():
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
            
            def internal_fix(match):
                inner = match.group(1).strip()
                return f"**{inner}**"
            
            # Fix internal spaces
            # Run multiple times or use loop to handle nested cases if any (unlikely for bold)
            # But single pass per pattern is usually enough
            content = pattern_internal_1.sub(internal_fix, content)
            content = pattern_internal_2.sub(internal_fix, content)

            # Fix external spacing
            content = external_space_pattern.sub(r'\1 \2', content)
            
            if content != original_content:
                print(f"Fixed formatting in: {file}")
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count_files += 1
                count_fixes += 1

    print(f"Cleanup V2 finished. Modified {count_files} files.")

if __name__ == "__main__":
    cleanup_bold_v2()
