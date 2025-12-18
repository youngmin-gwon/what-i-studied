# 셸 스크립팅

## 1. 셸 스크립트 기초

### 1.1 스크립트 작성

**기본 구조**:
```bash
#!/bin/bash
# 주석: 스크립트 설명

echo "Hello, World!"
```

**Shebang (`#!`)**:
- 스크립트 인터프리터 지정
- `#!/bin/bash`: bash 사용
- `#!/bin/sh`: POSIX 셸
- `#!/usr/bin/env python3`: Python

**실행 권한**:
```bash
chmod +x script.sh
./script.sh
```

**실행 방법**:
```bash
./script.sh         # 실행 권한 필요
bash script.sh      # 권한 불필요
source script.sh    # 현재 셸에서 실행
. script.sh         # source와 동일
```

## 2. 변수

### 2.1 변수 선언 및 사용

```bash
# 변수 선언 (공백 없이!)
NAME="John"
AGE=30
PATH_DIR="/home/user"

# 변수 사용
echo $NAME
echo ${NAME}        # 권장 (명확함)
echo "My name is $NAME"
echo "Age: ${AGE}"

# 명령 결과 저장
CURRENT_DATE=$(date)
FILES=$(ls -l)
USER_COUNT=`who | wc -l`  # 구식 문법
```

### 2.2 특수 변수

```bash
$0      # 스크립트 이름
$1-$9   # 위치 매개변수 (인수)
$#      # 인수 개수
$@      # 모든 인수 (개별)
$*      # 모든 인수 (하나의 문자열)
$?      # 마지막 명령의 종료 상태
$$      # 현재 프로세스 PID
$!      # 마지막 백그라운드 프로세스 PID
```

**예제**:
```bash
#!/bin/bash
echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Number of arguments: $#"
echo "All arguments: $@"
echo "Process ID: $$"
```

### 2.3 환경 변수

```bash
export VAR="value"  # 환경 변수로 내보내기
unset VAR           # 변수 제거

# 읽기 전용
readonly PI=3.14
declare -r CONST="constant"
```

## 3. 입출력

### 3.1 사용자 입력

```bash
# read 명령
read NAME
echo "Hello, $NAME"

# 프롬프트와 함께
read -p "Enter your name: " NAME

# 비밀번호 입력 (숨김)
read -sp "Enter password: " PASSWORD

# 타임아웃
read -t 5 -p "Enter within 5 seconds: " INPUT

# 배열로 읽기
read -a ARRAY
echo ${ARRAY[0]}
```

### 3.2 출력

```bash
echo "Text"                 # 기본 출력
echo -n "No newline"        # 줄바꿈 없이
echo -e "Line1\nLine2"      # 이스케이프 시퀀스 해석

printf "Name: %s, Age: %d\n" "$NAME" $AGE  # 형식화된 출력
printf "%.2f\n" 3.14159     # 소수점 2자리
```

## 4. 조건문

### 4.1 if 문

```bash
if [ condition ]; then
    commands
fi

if [ condition ]; then
    commands
else
    commands
fi

if [ condition1 ]; then
    commands
elif [ condition2 ]; then
    commands
else
    commands
fi
```

### 4.2 테스트 조건

**파일 테스트**:
```bash
[ -e file ]     # 파일 존재
[ -f file ]     # 일반 파일
[ -d dir ]      # 디렉토리
[ -r file ]     # 읽기 가능
[ -w file ]     # 쓰기 가능
[ -x file ]     # 실행 가능
[ -s file ]     # 크기가 0보다 큼
[ -L file ]     # 심볼릭 링크
[ file1 -nt file2 ]  # file1이 더 최신
[ file1 -ot file2 ]  # file1이 더 오래됨
```

**문자열 테스트**:
```bash
[ -z "$str" ]       # 문자열이 비어있음
[ -n "$str" ]       # 문자열이 비어있지 않음
[ "$str1" = "$str2" ]   # 같음
[ "$str1" != "$str2" ]  # 다름
[ "$str1" \< "$str2" ]  # 사전순 비교
```

**숫자 비교**:
```bash
[ $a -eq $b ]   # 같음 (equal)
[ $a -ne $b ]   # 다름 (not equal)
[ $a -lt $b ]   # 작음 (less than)
[ $a -le $b ]   # 작거나 같음 (less or equal)
[ $a -gt $b ]   # 큼 (greater than)
[ $a -ge $b ]   # 크거나 같음 (greater or equal)
```

**논리 연산**:
```bash
[ condition1 ] && [ condition2 ]  # AND
[ condition1 ] || [ condition2 ]  # OR
[ ! condition ]                   # NOT
[ condition1 -a condition2 ]      # AND (구식)
[ condition1 -o condition2 ]      # OR (구식)
```

**이중 대괄호 `[](../.md)`** (bash 확장):
```bash
[$str =~ regex](../../$str =~ regex.md)     # 정규식 매칭
[$str == pattern](../../$str == pattern.md)   # 패턴 매칭
[$a > $b](../../$a > $b.md)           # 문자열 비교 (이스케이프 불필요)
```

**예제**:
```bash
#!/bin/bash
if [ -f "/etc/passwd" ]; then
    echo "File exists"
fi

if [ $# -eq 0 ]; then
    echo "No arguments provided"
    exit 1
fi

if [[ "$1" =~ ^[0-9]+$ ]]; then
    echo "Argument is a number"
fi
```

### 4.3 case 문

```bash
case $variable in
    pattern1)
        commands
        ;;
    pattern2)
        commands
        ;;
    pattern3|pattern4)
        commands
        ;;
    *)
        default commands
        ;;
esac
```

**예제**:
```bash
#!/bin/bash
case $1 in
    start)
        echo "Starting service..."
        ;;
    stop)
        echo "Stopping service..."
        ;;
    restart)
        echo "Restarting service..."
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
        ;;
esac
```

## 5. 반복문

### 5.1 for 루프

```bash
# 리스트 반복
for item in list1 list2 list3; do
    echo $item
done

# 파일 목록
for file in *.txt; do
    echo "Processing $file"
done

# 범위
for i in {1..10}; do
    echo $i
done

# C 스타일
for ((i=0; i<10; i++)); do
    echo $i
done

# 명령 결과
for user in $(cat /etc/passwd | cut -d: -f1); do
    echo "User: $user"
done
```

### 5.2 while 루프

```bash
while [ condition ]; do
    commands
done

# 예제: 카운터
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done

# 파일 읽기
while read line; do
    echo "Line: $line"
done < file.txt

# 무한 루프
while true; do
    echo "Press Ctrl+C to stop"
    sleep 1
done
```

### 5.3 until 루프

```bash
until [ condition ]; do
    commands
done

# 예제
count=1
until [ $count -gt 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

### 5.4 루프 제어

```bash
break       # 루프 종료
continue    # 다음 반복으로

# 예제
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        continue    # 5는 건너뛰기
    fi
    if [ $i -eq 8 ]; then
        break       # 8에서 종료
    fi
    echo $i
done
```

## 6. 함수

### 6.1 함수 정의 및 호출

```bash
# 정의
function_name() {
    commands
}

# 또는
function function_name {
    commands
}

# 호출
function_name
function_name arg1 arg2
```

**예제**:
```bash
#!/bin/bash

greet() {
    echo "Hello, $1!"
}

add() {
    local result=$(($1 + $2))
    echo $result
}

# 호출
greet "John"
sum=$(add 5 3)
echo "Sum: $sum"
```

### 6.2 함수 매개변수 및 반환

```bash
my_function() {
    local arg1=$1
    local arg2=$2
    
    # 지역 변수
    local result=$(($arg1 + $arg2))
    
    # 반환 (echo 사용)
    echo $result
}

# 호출 및 결과 저장
result=$(my_function 10 20)
echo "Result: $result"

# return 사용 (종료 상태만, 0-255)
check_file() {
    if [ -f "$1" ]; then
        return 0    # 성공
    else
        return 1    # 실패
    fi
}

if check_file "/etc/passwd"; then
    echo "File exists"
fi
```

## 7. 배열

### 7.1 배열 선언 및 사용

```bash
# 배열 선언
ARRAY=(value1 value2 value3)
ARRAY[0]="first"
ARRAY[1]="second"

# 배열 요소 접근
echo ${ARRAY[0]}        # 첫 번째 요소
echo ${ARRAY[@]}        # 모든 요소
echo ${ARRAY[*]}        # 모든 요소 (하나의 문자열)
echo ${#ARRAY[@]}       # 배열 크기

# 배열 반복
for item in "${ARRAY[@]}"; do
    echo $item
done

# 인덱스와 함께
for i in "${!ARRAY[@]}"; do
    echo "Index $i: ${ARRAY[$i]}"
done

# 배열 추가
ARRAY+=(value4)

# 배열 삭제
unset ARRAY[1]
unset ARRAY
```

### 7.2 연관 배열 (bash 4.0+)

```bash
# 선언
declare -A ASSOC_ARRAY

# 할당
ASSOC_ARRAY[key1]="value1"
ASSOC_ARRAY[key2]="value2"

# 접근
echo ${ASSOC_ARRAY[key1]}

# 모든 키
echo ${!ASSOC_ARRAY[@]}

# 모든 값
echo ${ASSOC_ARRAY[@]}
```

## 8. 문자열 처리

### 8.1 문자열 연산

```bash
STRING="Hello, World!"

# 길이
echo ${#STRING}         # 13

# 부분 문자열
echo ${STRING:0:5}      # Hello
echo ${STRING:7}        # World!

# 대소문자 변환
echo ${STRING^^}        # 대문자
echo ${STRING,,}        # 소문자

# 치환
echo ${STRING/World/Bash}       # 첫 번째 매칭
echo ${STRING//o/O}             # 모든 매칭

# 삭제
echo ${STRING#Hello, }          # 앞에서부터 최소 매칭 삭제
echo ${STRING%!}                # 뒤에서부터 최소 매칭 삭제
```

## 9. 산술 연산

### 9.1 산술 확장

```bash
# (( )) 사용
((a = 5 + 3))
echo $a             # 8

((a++))             # 증가
((a--))             # 감소
((a += 5))          # 복합 할당

# $((  )) 사용
result=$((5 + 3))
echo $result        # 8

result=$((10 * 2 + 5))
echo $result        # 25

# let 사용
let "a = 5 + 3"
let a++

# expr 사용 (구식)
result=$(expr 5 + 3)
```

**연산자**:
```bash
+   # 덧셈
-   # 뺄셈
*   # 곱셈
/   # 나눗셈
%   # 나머지
**  # 거듭제곱
```

## 10. 디버깅 및 에러 처리

### 10.1 디버깅

```bash
#!/bin/bash -x      # 디버그 모드
set -x              # 디버그 활성화
set +x              # 디버그 비활성화

set -e              # 에러 시 즉시 종료
set -u              # 미정의 변수 사용 시 에러
set -o pipefail     # 파이프라인 에러 감지

# 조합
set -euo pipefail
```

### 10.2 에러 처리

```bash
# 종료 상태 확인
command
if [ $? -eq 0 ]; then
    echo "Success"
else
    echo "Failed"
fi

# 또는
if command; then
    echo "Success"
else
    echo "Failed"
fi

# trap으로 에러 처리
trap 'echo "Error occurred"; exit 1' ERR

# 정리 작업
trap 'rm -f /tmp/tempfile' EXIT

# 시그널 처리
trap 'echo "Interrupted"; exit' INT TERM
```

## 11. 실용 예제

### 11.1 백업 스크립트

```bash
#!/bin/bash
set -euo pipefail

BACKUP_DIR="/backup"
SOURCE_DIR="/data"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="backup_${DATE}.tar.gz"

echo "Starting backup..."
tar -czf "${BACKUP_DIR}/${BACKUP_FILE}" "${SOURCE_DIR}"

if [ $? -eq 0 ]; then
    echo "Backup completed: ${BACKUP_FILE}"
else
    echo "Backup failed!"
    exit 1
fi

# 7일 이상 된 백업 삭제
find "${BACKUP_DIR}" -name "backup_*.tar.gz" -mtime +7 -delete
```

### 11.2 시스템 모니터링

```bash
#!/bin/bash

# CPU 사용률
CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)

# 메모리 사용률
MEM=$(free | grep Mem | awk '{print ($3/$2) * 100.0}')

# 디스크 사용률
DISK=$(df -h / | tail -1 | awk '{print $5}' | cut -d'%' -f1)

echo "CPU: ${CPU}%"
echo "Memory: ${MEM}%"
echo "Disk: ${DISK}%"

# 임계값 확인
if (( $(echo "$CPU > 80" | bc -l) )); then
    echo "Warning: High CPU usage!"
fi
```

## 12. 시험 대비 핵심 요약

### 기본
- **Shebang**: `#!/bin/bash`
- **실행**: `chmod +x script.sh`
- **변수**: `VAR=value`, `$VAR`, `${VAR}`

### 특수 변수
- `$0`: 스크립트 이름
- `$1-$9`: 인수
- `$#`: 인수 개수
- `$?`: 종료 상태

### 조건문
- **if**: `if [ condition ]; then ... fi`
- **case**: `case $var in pattern) ... ;; esac`

### 반복문
- **for**: `for i in list; do ... done`
- **while**: `while [ condition ]; do ... done`

### 함수
- **정의**: `func() { ... }`
- **호출**: `func arg1 arg2`
- **반환**: `echo result` 또는 `return status`

### 테스트
- **파일**: `-f`, `-d`, `-e`, `-r`, `-w`, `-x`
- **문자열**: `-z`, `-n`, `=`, `!=`
- **숫자**: `-eq`, `-ne`, `-lt`, `-le`, `-gt`, `-ge`

---

**이전 챕터**: [시스템 서비스 및 데몬](09-services-daemons.md)  
**다음 챕터**: [시스템 모니터링 및 로그](11-monitoring-logs.md)
