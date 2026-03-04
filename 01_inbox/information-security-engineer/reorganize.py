import os
import re

content = open("quiz_system.md", "r", encoding="utf-8").read()

# Separate frontmatter
frontmatter_match = re.search(r"^(---.*?---)\s*(.*)", content, flags=re.DOTALL)
frontmatter = frontmatter_match.group(1)
body = frontmatter_match.group(2)

# Find all questions
pattern = r"(<details.*?>\s*<summary>.*?</summary>\s*<blockquote>.*?</blockquote>\s*</details>)"
raw_questions = re.findall(pattern, body, flags=re.DOTALL)

# Convert all `<details...>` to `<details open>`
questions = []
for q in raw_questions:
    q = re.sub(r"^<details.*?>", "<details open>", q)
    questions.append(q)

def q_has(q, keywords):
    text = q.lower()
    return any(k.lower() in text for k in keywords)

# Map questions to categories
categories = {}
def add_q(cat, q):
    if cat not in categories:
        categories[cat] = []
    if q not in categories[cat]:
        categories[cat].append(q)

unassigned = list(questions)

# Matching logic
def assign_question(kws, cat_path, exclude_kws=None):
    global unassigned
    new_unassigned = []
    for q in unassigned:
        if q_has(q, kws) and (not exclude_kws or not q_has(q, exclude_kws)):
            add_q(cat_path, q)
        else:
            new_unassigned.append(q)
    unassigned = new_unassigned

assign_question(["LSA(lsass.exe)", "LSA와 SAM", "Winlogon이 LSA", "SRM(Security Reference Monitor)이 커널 모드", "SRM(Security Reference Monitor)과 LSA", "LSA, SAM, SRM"], "공부노트/윈도우 기본 학습/윈도우 인증과정/윈도우 인증 구성 요소")
assign_question(["'로컬 인증'을 수행할 때", "로컬 인증과 원격(도메인) 인증은 서로 다른 모듈"], "공부노트/윈도우 기본 학습/윈도우 인증과정/로컬 인증")
assign_question(["원격(도메인) 인증", "Netlogon 서비스"], "공부노트/윈도우 기본 학습/윈도우 인증과정/원격 인증")

# SAM File Access Control
assign_question(["SAM 파일", "HKEY_LOCAL_MACHINE\\SAM", "SAM 계정과 공유의 익명 열거", "System", "Administrators"], "공부노트/윈도우 기본 학습/윈도우 인증과정/SAM 파일 접근통제 설정")

assign_question(["무차별 대입", "사전 공격"], "공부노트/윈도우 기본 학습/패스워드 크래킹 (17년 산기)/사전 공격/사전 대입 공격")
assign_question(["도메인", "워크그룹", "Active Directory"], "공부노트/윈도우 기본 학습/윈도우 인증 구조/개요")
assign_question(["NTLM", "Kerberos", "커버로스"], "공부노트/윈도우 기본 학습/윈도우 인증 구조/인증 암호 알고리즘")
assign_question(["NT, NTFS", "SMSS", "lsass.exe", "BitLocker"], "공부노트/윈도우 기본 학습/윈도우 인증과정/윈도우 인증 구성 요소")

# Logs
assign_question(["이벤트 로그", "Event Viewer", "감사 정책", "evtx", "Winevt", "보안(Security) 로그"], "공부노트/윈도우 기본 학습/윈도우 로그 및 기타 (추가됨)")
assign_question(["/var/log/secure", "dmesg", "lastlog"], "공부노트/UNIX/Linux 서버 보안/시스템 로그 설정과 관리/유닉스/리눅스 주요 로그 파일")
assign_question(["/etc/skel"], "공부노트/UNIX/Linux 시스템 관리/사용자 및 그룹 관리/사용자 관리(추가, 변경 및 삭제)")
assign_question(["/etc/shadow"], "공부노트/UNIX/Linux 서버 보안/시스템 보안/사용자의 패스워드 관리")
assign_question(["SetUID", "SUID", "SGID"], "공부노트/UNIX/Linux 서버 보안/시스템 보안/프로세스 실행권한[SUID,SGID] (13/22년 기사, 14/15/22년 산기)")
assign_question(["포맷 스트링", "%n"], "공부노트/시스템 해킹/포맷 스트링 공격(Format String Attack)")
assign_question(["DEP/NX", "ASLR"], "공부노트/시스템 해킹/버퍼 오버플로우 공격(Buffer Overflow Attack)")
assign_question(["싱글 모드"], "공부노트/UNIX/Linux 시스템 관리/시스템 시작과 종료/시스템 시작")
assign_question(["슬랙 공간"], "공부노트/UNIX/Linux 서버 보안/시스템 보안/기타 (추가됨)")
assign_question(["트립와이어"], "공부노트/UNIX/Linux 서버 보안/기타 (추가됨)")

# Remaining Windows / Unix / Generic
assign_question(["하이퍼바이저"], "공부노트/UNIX/Linux 기본 학습/시스템 기본/특수 문자(메타 문자, Meta character)") # Arbitrary fallback
assign_question(["엘리베이터 알고리즘", "SCAN"], "공부노트/UNIX/Linux 기본 학습/시스템 기본/특수 문자(메타 문자, Meta character)")
assign_question(["NAC", "Network Access Control"], "공부노트/UNIX/Linux 서버 보안/네트워크 보안/접근 통제[TCP Wrapper]")

# If there is anything else unassigned, put in a catch-all
for q in unassigned:
    add_q("미분류 기타", q)

tree_text = """
공부노트

윈도우 기본 학습

윈도우 인증과정
- 윈도우 인증 구성 요소
- 로컬 인증
- 원격 인증
- SAM 파일 접근통제 설정

윈도우 보안 식별자
- 개요
- 구조

윈도우 인증 구조
- 개요
- 인증 암호 알고리즘
- lan manager 인증 수준

패스워드 크래킹 (17년 산기)
- 사전 공격/사전 대입 공격
- 무차별 공격

윈도우 로그 및 기타 (추가됨)

UNIX/Linux 기본 학습

시스템 기본
- 사용자 정보
- 그룹 정보
- 입출력 재지정(I/O Redirection) 기능
- 파이프 또는 파이프라인 기능
- 특수 문자(메타 문자, Meta character)

파일 시스템 응용
- 파일 시스템 개요
- 파일 시스템 링크 파일
- 디렉터리 관리
- 파일 권한 관리
- 파일 검색
- 파일 및 디렉터리 관련 명령어 요약

프로세스 응용
- 프로세스 개요
- 프로세스 정보 확인
- 프로세스 간 통신(시그널)

UNIX/Linux 시스템 관리

시스템 시작과 종료
- 시스템 런 레벨
- 시스템 시작
- 시스템 종료

사용자 및 그룹 관리
- 사용자 관리(추가, 변경 및 삭제)
- 그룹 관리(추가, 변경 및 삭제)

파일 시스템 관리
- 파일시스템(디스크) 여유 공간 키그 관리(df 명령어)
- 디렉터리(파일)별 파일시스템(디스크) 사용량 관리(du 명령어)

작업 스케줄 관리
- cron 서비스(정기적 작업 스케줄 관리 서비스)

UNIX/Linux 서버 보안

시스템 보안
- 사용자의 패스워드 관리
- 프로세스 실행권한[SUID,SGID] (13/22년 기사, 14/15/22년 산기)
- 기타 (추가됨)

네트워크 보안
- 보안 쉘(SSH)
- 슈퍼 서버[inetd 데몬]
- 접근 통제[TCP Wrapper]
- xinetd 슈퍼 데몬

PAM(장착형 인증 모듈, Pluggable Authentication Modules)
- 개요
- PAM을 사용한 인증 절차
- PAM 설정파일(/etc/pam.d/remote 설정파일 일부)
- PAM 활용 예1 (시스템 취약점 분석, 평가 항목)
- PAM 활용 예2(시스템 취약점 분석, 평가 일부 항목)
- PAM 활용 예3(시스템 취약점 분석, 평가 일부 항목)

시스템 로그 설정과 관리
- 개요
- 유닉스/리눅스 주요 로그 파일

syslog 설정 및 관리
- 개요

리눅스 로그 관리

기타 (추가됨)

시스템 해킹

버퍼 오버플로우 공격(Buffer Overflow Attack)

레이스 컨디션 공격(Race Condition Attack)

포맷 스트링 공격(Format String Attack)

미분류 기타
"""

lines = tree_text.strip().split('\n')
output_lines = [frontmatter, "", "## 🛡️ 정보보안기사 실기 Quiz\n"]

cur_h1 = ""
cur_h2 = ""
cur_h3 = ""

def print_qs(path):
    if path in categories and categories[path]:
        for q in categories[path]:
            output_lines.append(q + "\n")
        # clear to prevent duplicates
        categories[path] = []

for line in lines:
    line = line.strip()
    if not line:
        continue
    
    if line == "공부노트":
        cur_h1 = line
        output_lines.append(f"### {cur_h1}")
        continue

    # Is it a level 2 or level 3 or a leaf?
    # In user's text:
    # 윈도우 기본 학습 (H2)
    # 윈도우 인증과정 (H3)
    # - 윈도우 인증 구성 요소 (H4)
    if line.startswith("-"):
        h4 = line[1:].strip()
        path = f"{cur_h1}/{cur_h2}/{cur_h3}/{h4}".replace("//", "/")
        output_lines.append(f"###### {h4}")
        print_qs(path)
    else:
        # Determine if H2 or H3 based on context. 
        # Known H2: 윈도우 기본 학습, UNIX/Linux 기본 학습, UNIX/Linux 시스템 관리, UNIX/Linux 서버 보안, 시스템 해킹, 미분류 기타, 윈도우 로그 및 기타 (추가됨)
        h2_list = ["윈도우 기본 학습", "UNIX/Linux 기본 학습", "UNIX/Linux 시스템 관리", "UNIX/Linux 서버 보안", "시스템 해킹", "미분류 기타", "윈도우 로그 및 기타 (추가됨)"]
        if line in h2_list:
            cur_h2 = line
            cur_h3 = ""
            output_lines.append(f"#### {cur_h2}")
            path = f"{cur_h1}/{cur_h2}"
            print_qs(path)
        else:
            cur_h3 = line
            output_lines.append(f"##### {cur_h3}")
            path = f"{cur_h1}/{cur_h2}/{cur_h3}"
            print_qs(path)

# Print any leftover queries that somehow didn't get matched to the exact tree paths
leftover = False
for k, v in categories.items():
    if v:
        if not leftover:
            output_lines.append("#### 누락된 항목")
            leftover = True
        output_lines.append(f"##### {k.split('/')[-1]}")
        for q in v:
            output_lines.append(q + "\n")

with open("quiz_system.md", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))
print("Done!")
