# 기본 명령어 및 셸

## 1. 셸(Shell) 개요

### 1.1 셸의 역할
- **명령어 해석기**: 사용자 명령을 커널에 전달
- **프로그래밍 환경**: 스크립트 작성 가능
- **사용자 인터페이스**: CLI 제공

### 1.2 주요 셸 종류
- **bash (Bourne Again Shell)**: 가장 널리 사용, 리눅스 기본
- **sh (Bourne Shell)**: 전통적 유닉스 셸
- **csh/tcsh**: C 언어 스타일 문법
- **zsh**: 강력한 기능, 플러그인 지원
- **fish**: 사용자 친화적, 자동 완성

**현재 셸 확인**:
```bash
echo $SHELL             # 로그인 셸
echo $0                 # 현재 셸
cat /etc/shells         # 사용 가능한 셸 목록
```

## 2. 파일 및 디렉토리 명령어

### 2.1 디렉토리 탐색

```bash
pwd                     # 현재 디렉토리 경로
cd /path/to/dir         # 디렉토리 이동
cd ~                    # 홈 디렉토리
cd -                    # 이전 디렉토리
cd ..                   # 상위 디렉토리
cd ../..                # 2단계 상위
```

### 2.2 파일 목록

```bash
ls                      # 파일 목록
ls -l                   # 상세 정보 (long format)
ls -a                   # 숨김 파일 포함
ls -h                   # 사람이 읽기 쉬운 크기
ls -R                   # 재귀적 (하위 디렉토리 포함)
ls -t                   # 수정 시간 순 정렬
ls -S                   # 크기 순 정렬
ls -lh /etc/*.conf      # 와일드카드 사용
```

**ls -l 출력 해석**:
```
-rw-r--r-- 1 user group 1024 Jan 1 12:00 file.txt
│││││││││  │ │    │     │    │           │
│││││││││  │ │    │     │    │           └─ 파일명
│││││││││  │ │    │     │    └─ 수정 시간
│││││││││  │ │    │     └─ 크기 (바이트)
│││││││││  │ │    └─ 그룹
│││││││││  │ └─ 소유자
│││││││││  └─ 링크 수
│││││││││
│││││││└┴─ 기타 권한 (r--)
││││└┴┴─── 그룹 권한 (r--)
│└┴┴────── 소유자 권한 (rw-)
└───────── 파일 타입 (-)
```

### 2.3 파일 생성 및 삭제

```bash
touch file.txt          # 빈 파일 생성 또는 타임스탬프 갱신
mkdir dir               # 디렉토리 생성
mkdir -p a/b/c          # 중간 디렉토리도 생성
rm file.txt             # 파일 삭제
rm -r dir               # 디렉토리 재귀 삭제
rm -f file.txt          # 강제 삭제 (확인 안 함)
rm -rf dir              # 강제 재귀 삭제 (위험!)
rmdir dir               # 빈 디렉토리 삭제
```

### 2.4 파일 복사 및 이동

```bash
cp source.txt dest.txt          # 파일 복사
cp -r dir1 dir2                 # 디렉토리 복사
cp -p file.txt backup.txt       # 속성 보존
cp -i file.txt dest.txt         # 덮어쓰기 확인
mv old.txt new.txt              # 이름 변경
mv file.txt /path/to/dir/       # 이동
mv -i file.txt dest.txt         # 덮어쓰기 확인
```

## 3. 파일 내용 확인

### 3.1 파일 보기

```bash
cat file.txt            # 전체 내용 출력
cat file1 file2         # 여러 파일 연결
tac file.txt            # 역순 출력
head file.txt           # 처음 10줄
head -n 20 file.txt     # 처음 20줄
tail file.txt           # 마지막 10줄
tail -n 20 file.txt     # 마지막 20줄
tail -f /var/log/syslog # 실시간 모니터링
less file.txt           # 페이지 단위 보기 (q로 종료)
more file.txt           # 페이지 단위 보기 (구식)
```

### 3.2 파일 검색

**grep - 텍스트 검색**:
```bash
grep "pattern" file.txt         # 패턴 검색
grep -i "pattern" file.txt      # 대소문자 무시
grep -r "pattern" /path/        # 재귀 검색
grep -n "pattern" file.txt      # 줄 번호 표시
grep -v "pattern" file.txt      # 패턴 제외
grep -c "pattern" file.txt      # 매칭 줄 수
grep -l "pattern" *.txt         # 파일명만 출력
grep -E "regex" file.txt        # 확장 정규식 (egrep)
grep -w "word" file.txt         # 단어 단위 매칭
```

**find - 파일 찾기**:
```bash
find /path -name "*.txt"        # 이름으로 검색
find /path -iname "*.TXT"       # 대소문자 무시
find /path -type f              # 파일만
find /path -type d              # 디렉토리만
find /path -size +100M          # 100MB 이상
find /path -mtime -7            # 7일 이내 수정
find /path -user username       # 소유자로 검색
find /path -perm 644            # 권한으로 검색
find /path -name "*.log" -delete  # 찾아서 삭제
find /path -name "*.txt" -exec cat {} \;  # 찾아서 실행
```

**locate - 빠른 파일 검색**:
```bash
locate filename         # 데이터베이스에서 검색
updatedb                # 데이터베이스 업데이트 (root)
```

**which/whereis**:
```bash
which ls                # 명령어 경로
whereis ls              # 바이너리, 소스, 매뉴얼 위치
```

## 4. 리다이렉션 및 파이프

### 4.1 리다이렉션

**표준 스트림**:
- **stdin (0)**: 표준 입력
- **stdout (1)**: 표준 출력
- **stderr (2)**: 표준 에러

**출력 리다이렉션**:
```bash
command > file.txt      # 출력을 파일로 (덮어쓰기)
command >> file.txt     # 출력을 파일에 추가
command 2> error.txt    # 에러를 파일로
command &> all.txt      # 출력과 에러 모두
command > out.txt 2>&1  # 출력과 에러를 같은 파일로
command > /dev/null     # 출력 버리기
```

**입력 리다이렉션**:
```bash
command < input.txt     # 파일에서 입력
command << EOF          # Here Document
line 1
line 2
EOF
```

### 4.2 파이프

**파이프 (`|`)**: 한 명령의 출력을 다른 명령의 입력으로
```bash
ls -l | grep ".txt"             # 파일 목록에서 .txt 검색
cat file.txt | wc -l            # 줄 수 세기
ps aux | grep httpd             # 프로세스 검색
dmesg | tail -20                # 커널 메시지 마지막 20줄
cat /etc/passwd | cut -d: -f1   # 사용자 이름만 추출
```

**tee**: 출력을 파일과 화면에 동시 표시
```bash
ls -l | tee output.txt          # 화면에도 보이고 파일에도 저장
command | tee -a log.txt        # 추가 모드
```

## 5. 와일드카드 및 패턴 매칭

### 5.1 글로빙 (Globbing)

```bash
*                       # 0개 이상의 문자
?                       # 정확히 1개 문자
[abc]                   # a, b, c 중 하나
[a-z]                   # a부터 z까지
[!abc]                  # a, b, c가 아닌 것
{jpg,png,gif}           # jpg, png, gif 중 하나
```

**예제**:
```bash
ls *.txt                # 모든 .txt 파일
ls file?.txt            # file1.txt, fileA.txt 등
ls [a-c]*               # a, b, c로 시작하는 파일
ls file[0-9].txt        # file0.txt ~ file9.txt
rm *.{log,tmp}          # .log와 .tmp 파일 삭제
```

### 5.2 정규 표현식 (Regex)

**기본 메타 문자**:
```
.       # 임의의 한 문자
^       # 줄 시작
$       # 줄 끝
*       # 0회 이상 반복
+       # 1회 이상 반복 (확장)
?       # 0 또는 1회 (확장)
[]      # 문자 클래스
|       # OR (확장)
()      # 그룹화 (확장)
\       # 이스케이프
```

**예제**:
```bash
grep "^root" /etc/passwd        # root로 시작하는 줄
grep "bash$" /etc/passwd        # bash로 끝나는 줄
grep "a.c" file.txt             # a와 c 사이에 한 문자
grep -E "a+" file.txt           # a가 1개 이상
grep -E "(cat|dog)" file.txt    # cat 또는 dog
```

## 6. 텍스트 처리 명령어

### 6.1 기본 텍스트 도구

```bash
wc file.txt             # 줄, 단어, 바이트 수
wc -l file.txt          # 줄 수만
wc -w file.txt          # 단어 수만
wc -c file.txt          # 바이트 수만

sort file.txt           # 정렬
sort -r file.txt        # 역순 정렬
sort -n file.txt        # 숫자 정렬
sort -u file.txt        # 중복 제거하고 정렬

uniq file.txt           # 연속된 중복 제거
uniq -c file.txt        # 중복 횟수 표시
uniq -d file.txt        # 중복된 것만

cut -d: -f1 /etc/passwd         # : 구분자로 1번째 필드
cut -c1-10 file.txt             # 1~10번째 문자

tr 'a-z' 'A-Z' < file.txt       # 소문자를 대문자로
tr -d '0-9' < file.txt          # 숫자 삭제
```

### 6.2 sed (Stream Editor)

```bash
sed 's/old/new/' file.txt       # 첫 번째 매칭 치환
sed 's/old/new/g' file.txt      # 모든 매칭 치환
sed -i 's/old/new/g' file.txt   # 파일 직접 수정
sed '1,10d' file.txt            # 1~10줄 삭제
sed -n '5,10p' file.txt         # 5~10줄만 출력
sed '/pattern/d' file.txt       # 패턴 매칭 줄 삭제
```

### 6.3 awk

```bash
awk '{print $1}' file.txt       # 첫 번째 필드 출력
awk -F: '{print $1}' /etc/passwd  # : 구분자
awk '{print $1, $3}' file.txt   # 1, 3번째 필드
awk '$3 > 100' file.txt         # 3번째 필드가 100 초과
awk 'NR==5' file.txt            # 5번째 줄
awk 'END {print NR}' file.txt   # 총 줄 수
```

## 7. 파일 압축 및 아카이브

### 7.1 tar (Tape Archive)

```bash
tar -cvf archive.tar dir/       # 아카이브 생성
tar -xvf archive.tar            # 아카이브 추출
tar -tvf archive.tar            # 내용 확인
tar -czvf archive.tar.gz dir/   # gzip 압축
tar -cjvf archive.tar.bz2 dir/  # bzip2 압축
tar -xzvf archive.tar.gz        # gzip 압축 해제
tar -xjvf archive.tar.bz2       # bzip2 압축 해제
tar -xvf archive.tar -C /path/  # 특정 디렉토리에 추출
```

**옵션**:
- `-c`: create (생성)
- `-x`: extract (추출)
- `-t`: list (목록)
- `-v`: verbose (상세)
- `-f`: file (파일 지정)
- `-z`: gzip
- `-j`: bzip2
- `-J`: xz

### 7.2 압축 도구

```bash
gzip file.txt           # file.txt.gz 생성
gunzip file.txt.gz      # 압축 해제
gzip -d file.txt.gz     # 압축 해제

bzip2 file.txt          # file.txt.bz2 생성
bunzip2 file.txt.bz2    # 압축 해제

xz file.txt             # file.txt.xz 생성
unxz file.txt.xz        # 압축 해제

zip archive.zip file1 file2  # zip 생성
unzip archive.zip            # zip 해제
```

## 8. 명령어 히스토리 및 편집

### 8.1 히스토리

```bash
history                 # 명령어 히스토리
history 10              # 최근 10개
!100                    # 100번 명령 실행
!!                      # 직전 명령 실행
!grep                   # grep으로 시작하는 최근 명령
!$                      # 직전 명령의 마지막 인수
^old^new                # 직전 명령에서 old를 new로 치환
```

**히스토리 설정**:
```bash
HISTSIZE=1000           # 메모리 히스토리 크기
HISTFILESIZE=2000       # 파일 히스토리 크기
HISTCONTROL=ignoredups  # 중복 무시
```

### 8.2 명령줄 편집 (Bash)

**단축키**:
```
Ctrl+A      # 줄 시작으로
Ctrl+E      # 줄 끝으로
Ctrl+U      # 커서 앞 삭제
Ctrl+K      # 커서 뒤 삭제
Ctrl+W      # 단어 삭제
Ctrl+L      # 화면 지우기
Ctrl+R      # 히스토리 검색
Tab         # 자동 완성
```

## 9. 환경 변수

### 9.1 주요 환경 변수

```bash
echo $PATH              # 명령어 검색 경로
echo $HOME              # 홈 디렉토리
echo $USER              # 사용자 이름
echo $SHELL             # 셸 경로
echo $PWD               # 현재 디렉토리
echo $LANG              # 로케일 설정
```

### 9.2 변수 설정

```bash
VAR=value               # 변수 설정 (지역)
export VAR=value        # 환경 변수로 내보내기
unset VAR               # 변수 제거
env                     # 모든 환경 변수
printenv                # 환경 변수 출력
set                     # 모든 변수 (지역 포함)
```

**PATH 추가**:
```bash
export PATH=$PATH:/new/path
# ~/.bashrc에 추가하여 영구 적용
```

## 10. 시험 대비 핵심 요약

### 필수 명령어
- **파일**: `ls`, `cp`, `mv`, `rm`, `touch`, `mkdir`
- **내용**: `cat`, `head`, `tail`, `less`, `grep`, `find`
- **텍스트**: `wc`, `sort`, `uniq`, `cut`, `sed`, `awk`
- **압축**: `tar`, `gzip`, `bzip2`

### 리다이렉션
- `>`: 출력 리다이렉션 (덮어쓰기)
- `>>`: 출력 추가
- `2>`: 에러 리다이렉션
- `|`: 파이프

### 와일드카드
- `*`: 0개 이상 문자
- `?`: 정확히 1개 문자
- `[abc]`: 문자 클래스

### tar 옵션
- `-c`: 생성
- `-x`: 추출
- `-t`: 목록
- `-v`: 상세
- `-f`: 파일
- `-z`: gzip

---

**이전 챕터**: [파일 시스템 및 디렉토리 구조](03-filesystem.md)  
**다음 챕터**: [사용자 및 권한 관리](05-users-permissions.md)
