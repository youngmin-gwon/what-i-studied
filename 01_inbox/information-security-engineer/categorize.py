import re
import os

def categorize_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split header from the rest
    parts = re.split(r'(<details>)', content, maxsplit=1)
    if len(parts) < 3:
        print(f"No <details> tags found in {filepath}")
        return
    
    header = parts[0]
    rest = parts[1] + parts[2]
    
    blocks = re.findall(r'(<details>.*?</details>)', rest, re.DOTALL)
    
    dan = []
    seo = []
    sil = []
    
    for block in blocks:
        summary_m = re.search(r'<summary>(.*?)</summary>', block, re.DOTALL)
        if not summary_m:
            continue
        summary = summary_m.group(1)
        
        # Classification logic
        if any(x in summary for x in ['서술', '설명', '차이', '이유', '비교', '특징']):
            seo.append(block)
        elif any(x in summary for x in ['명령어', '경로', '로그', '설정 파일', '설정 방법', '조치', '옵션', '룰', '규칙', '분석']):
            sil.append(block)
        else:
            dan.append(block)
            
    # Reconstruct 
    new_content = header.rstrip() + "\n\n"
    
    if dan:
        new_content += "#### 📝 단답형\n\n" + "\n\n".join(dan) + "\n\n"
    if seo:
        new_content += "#### ✍️ 서술형\n\n" + "\n\n".join(seo) + "\n\n"
    if sil:
        new_content += "#### 💻 실기형 (실무형)\n\n" + "\n\n".join(sil) + "\n\n"
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully processed {filepath}")

files = ['quiz_system.md', 'quiz_network.md', 'quiz_application.md', 'quiz_general.md']
for file in files:
    categorize_file(file)
