---
title: Text Processing Commands
tags: [linux, commands, text-processing, grep, sed, awk]
aliases: [텍스트 처리, Text Commands, grep, sed, awk]
date modified: 2025-12-20 13:59:24 +09:00
date created: 2025-12-20 13:59:24 +09:00
---

## 🌐 개요 (Overview)

Linux에서 텍스트 파일을 처리하는 강력한 명령어들입니다. 패턴 검색, 스트림 편집, 데이터 추출, 정렬, 필터링 등을 다룹니다.

## 📋 Quick Reference

| 명령어 | 용도 | 핵심 기능 |
|--------|------|-----------|
| `grep` | 패턴 검색 | 정규식, 재귀 검색 |
| `sed` | 스트림 편집 | 치환, 삭제, 삽입 |
| `awk` | 텍스트 분석 | 필드 처리, 계산 |
| `sort` | 정렬 | 다양한 정렬 옵션 |
| `uniq` | 중복 제거 | 연속 중복 처리 |
| `cut` | 필드 추출 | 구분자 기반 |
| `tr` | 문자 변환 | 대소문자, 삭제 |
| `wc` | 개수 세기 | 줄, 단어, 바이트 |

## 🔍 Pattern Matching

### grep - Global Regular Expression Print

**Syntax**:
```bash
grep [OPTIONS] PATTERN [FILE...]
```

**주요 옵션**:

| 옵션 | 설명 |
|------|------|
| `-i` | 대소문자 무시 |
| `-v` | 패턴 불일치 줄 출력 (반전) |
| `-n` | 줄 번호 표시 |
| `-c` | 매칭 줄 수만 출력 |
| `-l` | 매칭된 파일명만 출력 |
| `-L` | 매칭 안 된 파일명 출력 |
| `-r`, `-R` | 재귀 검색 |
| `-w` | 단어 단위 매칭 |
| `-x` | 전체 줄 매칭 |
| `-A NUM` | 매칭 후 NUM줄 출력 (After) |
| `-B NUM` | 매칭 전 NUM줄 출력 (Before) |
| `-C NUM` | 전후 NUM줄 출력 (Context) |
| `-E` | 확장 정규식 (egrep) |
| `-F` | 고정 문자열 (fgrep) |
| `--color` | 매칭 부분 색상 표시 |

**실용 예제**:

```bash
# 기본 검색
grep "error" /var/log/syslog

# 대소문자 무시
grep -i "error" logfile.txt

# 줄 번호 포함
grep -n "TODO" source.py

# 재귀 검색
grep -r "function" /path/to/code/

# 패턴 제외
grep -v "^#" config.conf  # 주석 제외

# 단어 단위 매칭
grep -w "log" file.txt  # "login", "catalog"는 제외

# 전후 문맥 포함
grep -C 3 "error" logfile  # 전후 3줄

# 여러 패턴
grep -e "error" -e "warning" logfile
grep "error\|warning" logfile  # 또는

# 파일명만 출력
grep -l "TODO" *.py

# 개수만
grep -c "error" /var/log/syslog

# 정규식
grep -E "^[0-9]{3}-[0-9]{4}$" contacts.txt  # 전화번호 패턴
```

**정규식 패턴**:

```bash
# 앵커
grep "^start" file.txt     # 줄 시작
grep "end$" file.txt        # 줄 끝
grep "^$" file.txt          # 빈 줄

# 문자 클래스
grep "[0-9]" file.txt       # 숫자
grep "[a-zA-Z]" file.txt    # 알파벳
grep "[^0-9]" file.txt      # 숫자 아닌 것

# 수량자
grep "a*" file.txt          # a가 0개 이상
grep -E "a+" file.txt       # a가 1개 이상
grep -E "a?" file.txt       # a가 0 또는 1개
grep -E "a{3}" file.txt     # a가 정확히 3개
grep -E "a{2,5}" file.txt   # a가 2~5개

# 그룹화
grep -E "(cat|dog)" file.txt  # cat 또는 dog
```

## ✂️ Stream Editing

### sed - Stream Editor

**Syntax**:
```bash
sed [OPTIONS] 'command' FILE
```

**주요 명령**:

| 명령 | 기능 | 예시 |
|------|------|------|
| `s/old/new/` | 치환 (첫 번째만) | `sed 's/foo/bar/'` |
| `s/old/new/g` | 치환 (전체) | `sed 's/foo/bar/g'` |
| `d` | 삭제 | `sed '1d'` |
| `p` | 출력 | `sed -n '1,5p'` |
| `a` | 다음 줄에 추가 | `sed '/pattern/a text'` |
| `i` | 이전 줄에 삽입 | `sed '/pattern/i text'` |
| `c` | 줄 변경 | `sed '/pattern/c new line'` |

**실용 예제**:

```bash
# 치환
sed 's/oldstring/newstring/' file.txt
sed 's/oldstring/newstring/g' file.txt  # 전체
sed 's/oldstring/newstring/gi' file.txt  # 대소문자 무시

# 파일 직접 수정
sed -i 's/old/new/g' file.txt
sed -i.bak 's/old/new/g' file.txt  # 백업 생성

# 줄 삭제
sed '1d' file.txt              # 첫 줄 삭제
sed '1,10d' file.txt           # 1~10줄 삭제
sed '/pattern/d' file.txt      # 패턴 매칭 줄 삭제
sed '/^$/d' file.txt           # 빈 줄 삭제
sed '/^#/d' file.txt           # 주석 삭제

# 줄 출력
sed -n '5p' file.txt           # 5번째 줄만
sed -n '1,10p' file.txt        # 1~10줄
sed -n '/pattern/p' file.txt   # 패턴 매칭 줄만

# 복합 명령
sed -e 's/foo/bar/g' -e 's/baz/qux/g' file.txt
sed '1,10s/old/new/g' file.txt  # 1~10줄만 치환

# 특수 문자 처리
sed 's/\/usr\/local/\/opt/g' file.txt  # 이스케이프
sed 's|/usr/local|/opt|g' file.txt     # 구분자 변경

# 정규식
sed 's/^[ \t]*//' file.txt     # 앞 공백 제거
sed 's/[ \t]*$//' file.txt     # 뒤 공백 제거
sed 's/  */ /g' file.txt       # 여러 공백을 하나로
```

## 📊 Text Analysis

### awk - Pattern Scanning and Processing

**Syntax**:
```bash
awk 'pattern {action}' FILE
```

**기본 구조**:
```awk
BEGIN { 초기화 }
pattern { 각 줄마다 실행 }
END { 마무리 }
```

**Built-in Variables**:

| 변수 | 의미 |
|------|------|
| `$0` | 전체 줄 |
| `$1, $2, ...` | 1번째, 2번째 필드 |
| `NF` | 필드 개수 (Number of Fields) |
| `NR` | 현재 줄 번호 (Number of Records) |
| `FS` | 필드 구분자 (Field Separator) |
| `OFS` | 출력 필드 구분자 (Output FS) |
| `RS` | 레코드 구분자 (Record Separator) |

**실용 예제**:

```bash
# 필드 출력
awk '{print $1}' file.txt              # 첫 번째 필드
awk '{print $1, $3}' file.txt          # 1, 3번째 필드
awk '{print $NF}' file.txt             # 마지막 필드
awk '{print $1 ":" $2}' file.txt       # 연결

# 구분자 지정
awk -F: '{print $1}' /etc/passwd       # : 구분자
awk -F',' '{print $2}' data.csv        # CSV

# 조건
awk '$3 > 100' file.txt                # 3번째 필드가 100 초과
awk '$1 == "user"' file.txt            # 1번째 필드가 "user"
awk '/pattern/' file.txt               # 패턴 매칭
awk '!/pattern/' file.txt              # 패턴 불일치

# 계산
awk '{sum += $1} END {print sum}' file.txt      # 합계
awk '{sum += $1} END {print sum/NR}' file.txt   # 평균
awk '{if ($1 > max) max = $1} END {print max}' file.txt  # 최대값

# 줄 번호
awk 'NR==5' file.txt                   # 5번째 줄
awk 'NR>=5 && NR<=10' file.txt         # 5~10줄

# BEGIN/END
awk 'BEGIN {print "Start"} {print} END {print "End"}' file.txt

# 실용 예제: 로그 분석
awk '/error/ {count++} END {print count}' /var/log/syslog

# CSV 처리
awk -F',' '{print $1 "\t" $2}' data.csv

# 사용자별 프로세스 개수
ps aux | awk '{count[$1]++} END {for (user in count) print user, count[user]}'
```

## 🔢 Sorting and Filtering

### sort - Sort Lines

**주요 옵션**:

| 옵션 | 설명 |
|------|------|
| `-r` | 역순 |
| `-n` | 숫자 정렬 |
| `-h` | 사람이 읽기 쉬운 숫자 (K, M, G) |
| `-k N` | N번째 필드로 정렬 |
| `-t CHAR` | 필드 구분자 |
| `-u` | 중복 제거 |
| `-f` | 대소문자 무시 |
| `-V` | 버전 순 정렬 |

**실용 예제**:

```bash
# 기본 정렬
sort file.txt

# 역순
sort -r file.txt

# 숫자 정렬
sort -n numbers.txt

# 필드별 정렬
sort -k 2 file.txt          # 2번째 필드
sort -t: -k 3 -n /etc/passwd  # : 구분, 3번째 필드, 숫자

# 중복 제거하고 정렬
sort -u file.txt

# 크기 정렬
du -sh * | sort -h

# 복합 정렬
sort -k1,1 -k2,2n file.txt  # 1번째는 문자, 2번째는 숫자
```

### uniq - Remove Duplicate Lines

```bash
uniq file.txt               # 연속 중복 제거
uniq -c file.txt            # 중복 횟수 표시
uniq -d file.txt            # 중복된 것만
uniq -u file.txt            # 유일한 것만
uniq -i file.txt            # 대소문자 무시

# sort와 함께 사용 (연속 중복 처리를 위해)
sort file.txt | uniq
sort file.txt | uniq -c | sort -rn  # 빈도순 정렬
```

### cut - Extract Fields

```bash
cut -d: -f1 /etc/passwd          # : 구분, 1번째 필드
cut -d: -f1,6 /etc/passwd        # 1, 6번째 필드
cut -d: -f1-3 /etc/passwd        # 1~3번째 필드
cut -c1-10 file.txt              # 1~10번째 문자
cut -c1,5,10 file.txt            # 1, 5, 10번째 문자
```

### tr - Translate Characters

```bash
tr 'a-z' 'A-Z' < file.txt      # 소문자 → 대문자
tr 'A-Z' 'a-z' < file.txt      # 대문자 → 소문자
tr -d '0-9' < file.txt         # 숫자 삭제
tr -d '\n' < file.txt          # 개행 제거
tr -s ' ' < file.txt           # 연속 공백을 하나로
tr ' ' '\n' < file.txt         # 공백을 개행으로
```

### paste - Merge Lines

```bash
paste file1.txt file2.txt      # 나란히 병합
paste -d: file1.txt file2.txt  # : 구분자로
paste -s file.txt              # 한 줄로 병합
```

## 📏 Counting and Comparing

### wc - Word Count

```bash
wc file.txt                 # 줄, 단어, 바이트
wc -l file.txt              # 줄 수만
wc -w file.txt              # 단어 수만
wc -c file.txt              # 바이트 수만
wc -m file.txt              # 문자 수만
wc -L file.txt              # 가장 긴 줄 길이

# 여러 파일
wc -l *.txt
```

### diff - Compare Files

```bash
diff file1.txt file2.txt           # 차이 표시
diff -u file1.txt file2.txt        # Unified format
diff -y file1.txt file2.txt        # Side-by-side
diff -r dir1/ dir2/                # 디렉토리 비교
diff -q file1.txt file2.txt        # 다른지만 확인
```

### comm - Compare Sorted Files

```bash
comm file1.txt file2.txt           # 3열: 1만, 2만, 공통
comm -12 file1.txt file2.txt       # 공통 줄만
comm -23 file1.txt file2.txt       # file1에만 있는 것
```

## 💡 Real-World Scenarios

### 시나리오 1: 로그 분석

```bash
# 에러 개수
grep -c "ERROR" /var/log/app.log

# 에러 유형별 통계
grep "ERROR" /var/log/app.log | awk '{print $4}' | sort | uniq -c | sort -rn

# 특정 시간대 에러
sed -n '/2025-01-01 10:00/,/2025-01-01 11:00/p' /var/log/app.log | grep ERROR

# IP별 접속 횟수
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10
```

### 시나리오 2: CSV 데이터 처리

```bash
# 특정 컬럼 추출
cut -d, -f2,4 data.csv

# 필터링
awk -F, '$3 > 1000 {print $0}' data.csv

# 합계 계산
awk -F, '{sum += $3} END {print sum}' data.csv

# 정렬
sort -t, -k3,3n data.csv
```

### 시나리오 3: 텍스트 정제

```bash
# 주석과 빈 줄 제거
sed '/^#/d; /^$/d' config.conf

# 앞뒤 공백 제거
sed 's/^[ \t]*//; s/[ \t]*$//' file.txt

# 중복 줄 제거
sort file.txt | uniq

# 소문자로 변환
tr 'A-Z' 'a-z' < file.txt
```

## 🔗 연결 문서 (Related Documents)

- [file-operations-commands](file-operations-commands.md) - 파일 작업
- [system-monitoring-commands](system-monitoring-commands.md) - 로그 모니터링
