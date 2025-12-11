# 14. 명령/옵션 레퍼런스 & 패턴 사전

> 시험에서 바로 떠올리기 쉽게 명령 옵션과 사용 예시를 묶었다. 각 섹션마다 "실수 주의"와 "기억 공식"을 넣었다.

## 내장 명령(builtin)
- `cd -- path`: `set -e` 상태에서는 실패 시 종료되지 않으므로 `cd -- "$dir" || exit 1` 사용.
- `pushd/popd`: 디렉터리 스택. 스크립트에서 재귀적 경로 이동할 때 유용하나, `set -e` 시 실패 체크 필요.
- `echo`: 이식성 불안. 개행 억제는 `printf '%s'`. `echo -n`/`-e` 동작이 셸마다 다름.
- `printf`: 포맷 안전. `%q`로 셸 이스케이프된 형태 출력 가능.
- `read`: `-r`로 백슬래시 무시, `-d ''`로 NUL 종단. `-t` 타임아웃, `-n` 글자수, `-s` silent.
- `test`/`[`: POSIX 조건. `[[ ]]`는 Bash 확장.
- `declare`/`typeset`: 변수 속성 부여, `-p`로 덤프. `-a/-A/-i/-r/-x` 등.
- `set`: 옵션 관리. `set -euo pipefail` 조합은 스크립트 첫 줄에서.
- `shopt`: Bash 전용 옵션. `nullglob`, `dotglob`, `extglob`, `globstar`, `lastpipe` 등.
- `trap`: 시그널/EXIT 처리. `trap -p`로 현재 등록된 핸들러 표시.

## 파일 시스템/디렉터리 관리
- `mkdir -p dir/sub`: 상위 디렉터리 자동 생성. `-m 700`으로 권한 지정 가능.
- `rm -rf dir`: 파괴적. 안전을 위해 `rm -i`/`-I` 또는 `trash` 대체. 시험에서는 실수 위험 언급.
- `cp -a src dst`: 속성 보존, 디렉터리 재귀. BSD/macOS에서는 `-a`가 `-RpP`와 유사.
- `mv src dst`: 동일 파일시스템에서 rename, 타 FS는 복사 후 삭제.
- `find`: `-type f/d/l`, `-name`, `-mtime +N`, `-size +1M`, `-maxdepth`. `-exec ... {} +`로 배치 실행.
- `realpath`/`readlink`: 심링크 해석. 휴대성 문제 있으므로 대안 언급.

## 프로세스/시스템
- `ps -ef`(SysV) / `ps aux`(BSD) → 프로세스 목록. `-o pid,ppid,command` 등으로 커스텀.
- `pgrep/-f pattern`: 프로세스 이름/명령줄 매칭. `pkill`은 종료.
- `kill -SIGTERM pid`: 종료 요청. `-0`으로 존재 여부 확인.
- `time cmd`: 실행 시간. `/usr/bin/time` 옵션 풍부(`-v` 등). bash 내장 `time`도 있음.
- `ulimit -n 4096`: FD 제한. `ulimit -t` CPU 시간, `-v` 가상 메모리.

## 네트워킹
- `curl -fsSL URL -o file`: 조용히 실패, 리다이렉트 따라감, stdout/파일 저장. `-H` 헤더, `-d` POST, `-X` 메서드.
- `wget -qO- URL`: stdout 출력. cron에서 PATH 없을 때 절대경로.
- `nc -z host port`: 포트 오픈 체크(TCP). `-u` UDP. 일부 구현은 `-z` 지원 X.
- `/dev/tcp/host/port`: Bash 확장. `echo > /dev/tcp/localhost/22`로 포트 테스트.

## 텍스트 필터 핵심 옵션 표
- `grep`: `-n`(번호), `-H`(파일명), `-r`(재귀), `-i`(대소문자 무시), `-v`(부정), `-o`(매칭만), `-mN`(N개 후 종료), `-F`(고정 문자열), `-E`(ERE), `-P`(PCRE).
- `sed`: `-n`(출력억제), `-e`(스크립트), `-f`(파일), `-i[.bak]`(인플레이스), 주소 범위 `1,5`, `/pat/`, `,/pat/`, 명령 `p,d,s///,a\,i\,c\`.
- `awk`: `-F`(입력 구분자), `-v name=val`(외부 변수), 내장변수 `NR,NF,FNR,FS,RS,OFS,ORS`, 함수 `length,substr,split,gsub,match,strftime`.
- `sort`: `-n` 숫자, `-r` 역순, `-k2,2` 키 범위, `-t,` 구분자, `-u` 고유, `-h` 사람친화 숫자, `-V` 버전 정렬.
- `uniq`: `-c` 카운트, `-d` 중복만, `-u` 고유만. 정렬된 입력 필요.
- `cut`: `-d` 구분자, `-f` 필드, `-c` 문자 범위. 탭이 기본 구분자.
- `tr`: 변환/삭제. `-d` 삭제, `-s` squeeze, 클래스 `[:upper:]`, `[:digit:]`.
- `xargs`: `-0` NUL, `-n` 인자 수, `-P` 병렬, `-I{}` 치환 문자열.

## 실전 조합 레시피 (명령 흐름)
1. **로그에서 오류 건수 상위 5개 코드 추출**  
   `grep -E 'ERROR|WARN' app.log | awk '{count[$2]++} END{for(k in count) printf "%s %d\n", k, count[k]}' | sort -k2,2nr | head -n5`
2. **여러 파일에서 특정 문자열을 찾아 줄번호/파일명 포함 출력**  
   `grep -Rni --color=auto 'pattern' src/`
3. **CSV 2열 평균 구하기(헤더 제외)**  
   `awk -F, 'NR>1 {sum+=$2; n++} END{printf "%.2f\n", sum/n}' data.csv`
4. **파일 이름에 공백이 있어도 안전한 삭제 전 백업**  
   `find . -name '*.tmp' -print0 | tar --null -T - -czf /tmp/tmpfiles.tgz` 후 삭제.
5. **JSON 파싱**  
   `jq -r '.items[] | select(.active==true) | .name' config.json` (jq 미존재 시 python 대안 준비).
6. **라인 번호 재주기**  
   `nl -ba file` 또는 `awk '{printf "%6d %s\n", NR, $0}' file`

## 옵션 암기 mnemonics
- grep `-n`(Number), `-i`(Ignore case), `-v`(invert), `-o`(Only match).
- sed `-n`(No auto-print), `-i`(In-place), `p`(print), `d`(delete), `s`(substitute).
- xargs `-0`(zero), `-P`(parallel), `-n`(number), `-I`(Insert placeholder).

## Bash 확장 기능 빠른 요약
- **Brace expansion**: `{a,b}`, `{1..5}`, `{00..10..2}`.
- **Tilde**: `~`, `~user`, `~+`(PWD), `~-`(OLDPWD).
- **Parameter expansion**: `${var:-d}`, `${var:=d}`, `${var:+a}`, `${var:?msg}`, `${var%pat}`, `${var#pat}`, `${var^^}`, `${var,,}`.
- **Arithmetic**: `$((i+=1))`, `(( i && j ))`.
- **Command substitution**: `$(cmd)`.
- **Process substitution**: `<(cmd)`, `>(cmd)`.

## 모범 패턴 스니펫 모음
- **필수 인자 검증**
  ```bash
  [[ $# -ge 1 ]] || { echo "usage: $0 FILE" >&2; exit 2; }
  ```
- **의존성 확인**
  ```bash
  for dep in curl jq; do command -v "$dep" >/dev/null || { echo "missing $dep" >&2; exit 127; }; done
  ```
- **임시 디렉터리**
  ```bash
  TMPDIR=$(mktemp -d) || exit 1
  trap 'rm -rf "$TMPDIR"' EXIT
  ```
- **배열 기반 옵션 조립**
  ```bash
  args=(--silent --location)
  [[ -n ${TOKEN:-} ]] && args+=(--header "Authorization: Bearer $TOKEN")
  curl "${args[@]}" "$url"
  ```
- **에러 로깅 후 종료**
  ```bash
  die(){ printf 'ERROR: %s\n' "$*" >&2; exit 1; }
  ```

## 시험에서 자주 나오는 트릭/함정
- `echo $((08))` → 8진수 해석으로 오류. `10#08` 사용.
- `for f in $(ls)` → 단어 분리/글로브 위험. `for f in *; do ...; done` 또는 find 사용.
- `cat file | grep` → UUOC 경고. `grep pattern file`.
- `rm -rf /tmp/$user`에서 `$user` 비어있을 때 대참사 → `${user:?}` 사용.
- `[[ $var == foo|bar ]]`는 잘못된 정규식. `[[ $var == foo || $var == bar ]]` 또는 `[[ $var =~ ^(foo|bar)$ ]]`.

## 정리용 테이블: 표현식 비교
- **문자열 비교**: `[ "$a" = "$b" ]`, `[[ $a == $b ]]`
- **산술 비교**: `[ "$a" -lt "$b" ]`, `(( a < b ))`
- **파일 비교**: `[ -f file ]`, `[ -d dir ]`, `[ file1 -nt file2 ]`
- **조건 조합**: `[[ cond1 && cond2 ]]`, `[[ cond1 || cond2 ]]`, `! cond`

## 정리용 테이블: 리디렉션
- `>` 덮어쓰기, `>>` 추가, `<` 입력, `2>` stderr, `&>` stdout+stderr(Bash), `>|` noclobber 무시
- `<<<` 히어스트링, `<<EOF` 히어독, `<<'EOF'` 리터럴 히어독, `<<-EOF` 탭 제거
- `cmd >file 2>&1` 합치기, `cmd 2>&1 | grep` stderr 파이프(오류 포함)

## 흔한 코드 블록 템플릿
- **메인 함수 패턴**
  ```bash
  main(){
    parse_args "$@"
    init
    run
  }
  main "$@"
  ```
- **재시도 루프**
  ```bash
  for attempt in {1..5}; do
    cmd && break
    sleep 1
  done
  ```
- **시간 제한**
  ```bash
  end=$((SECONDS+30))
  until (( SECONDS > end )); do
    do_work && break
    sleep 2
  done
  ```
- **색상 있는 로깅**
  ```bash
  if test -t 1; then green='\e[32m'; reset='\e[0m'; fi
  echo -e "${green}OK${reset}" >&2
  ```

## 기억해 둘 번호/코드
- 종료 코드: 0 성공, 1 일반, 2 사용법, 126 실행 불가, 127 명령 없음, 128+N 시그널
- 시그널: 1 HUP, 2 INT, 9 KILL, 13 PIPE, 15 TERM
- 파일 권한: 644 일반 파일, 755 실행 파일, 600 비밀, 700 개인 디렉터리

## 마무리 요약
- 명령은 **인자 순서**와 **인용 여부**로 결정된다. 시험 문제 대부분은 인자 순서/확장/환경 차이를 노린다.
- 옵션을 외워두되, 항상 `--help`/man을 확인하는 습관을 서술형 답안에 적으면 신뢰감을 준다.
- 실무 상황(네트워크 없음, cron, macOS/BSD, BusyBox 등)을 가정한 대안을 제시하면 가산점.

## 추가: 빈출 원라이너 20선
1. **디렉터리 용량 상위 10개**: `du -sh * | sort -h | tail -n 10`
2. **최근 수정 파일 5개**: `ls -lt | head -n 5`
3. **포트 열림 여부**: `bash -c 'echo > /dev/tcp/host/port' && echo open || echo closed`
4. **환경 변수 키만 정렬**: `env | cut -d= -f1 | sort`
5. **기능별 grep**: `grep -RIn --exclude-dir=.git pattern .`
6. **중복 줄 제거(순서 유지)**: `awk '!seen[$0]++' file`
7. **컬럼 합계**: `awk '{sum+=$1} END{print sum}' numbers`
8. **파일명 일괄 치환**: `for f in *.txt; do mv \"$f\" \"${f%.txt}.log\"; done`
9. **NUL 안전 basename**: `find . -type f -print0 | xargs -0 -n1 basename`
10. **HTTP 상태만 보기**: `curl -o /dev/null -w '%{http_code}\\n' -s https://example.com`
11. **tar 스트리밍 압축**: `tar -czf - dir | ssh host 'tar -xzf - -C /dest'`
12. **디렉터리 차이**: `diff -qr dir1 dir2`
13. **빈 줄/주석 제거**: `grep -Ev '^#|^$' file`
14. **컬럼 스와프**: `awk '{print $2, $1}' file`
15. **랜덤 비밀번호**: `LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c 20`
16. **CPU 코어 수**: `getconf _NPROCESSORS_ONLN` 또는 `nproc`(GNU)
17. **로그 tail + 필터**: `tail -F app.log | stdbuf -oL grep ERROR`
18. **파일 개수 카운트**: `find . -type f | wc -l`
19. **JSON 경로 테스트**: `jq -r 'path(..)|join(\".\")' sample.json | head`
20. **cron PATH 확인**: `* * * * * env > /tmp/cron.env` 후 검사

## 추가: GNU/BSD/BusyBox 차이표(요약)
- `sed -i`: GNU `sed -i 's/a/b/' file`, BSD `sed -i '' 's/a/b/' file`.
- `date`: GNU `-d`, BSD `-v`, BusyBox 일부만 지원. 휴대성 필요 시 python/perl 사용.
- `readlink -f`: GNU만. BSD `greadlink` 또는 python 대체.
- `xargs -r`: GNU만. BSD는 빈 입력도 명령 실행 → `test -s file || exit 0`.
- `tail -n +3`: GNU/BSD 동일. BusyBox도 대체로 지원.
- `mktemp -d`: 모두 지원하나 템플릿 형식 다름(일부 BusyBox는 `XXXXXX` 필수).
- `timeout`: GNU coreutils, BusyBox는 `timeout` 앱렛 제공할 수 있음, BSD 없음.

## 추가: 시험식 서술 템플릿
- **문법 차이 언급**: 이 구문은 Bash 확장으로 POSIX sh에서는 지원되지 않습니다. POSIX 호환이 필요하면 대안을 사용합니다.
- **안전성 언급**: 공백/개행 파일명을 처리하기 위해 NUL-종단(find -print0/xargs -0)을 사용합니다.
- **에러 핸들링 언급**: 실패 시 종료하도록 set -e/pipefail을 설정했으며, 해당 줄은 `|| true`로 의도적으로 무시했습니다.
- **포터빌리티 언급**: macOS에서는 `readlink -f`가 없으므로 python 대체를 제공합니다와 같이 OS별 케이스를 나열합니다.

## 추가: 서술형 답안 샘플
- **문제**: Bash 스크립트에서 JSON을 파싱하는 가장 안전한 방법은?  
  - **답안**: 가능하면 `jq` 사용. 의존성 검사 후 `command -v jq >/dev/null || { echo 'jq required' >&2; exit 127; }`. `jq -r '.key' file`로 파싱. jq 미설치 환경에서는 python의 `json` 모듈 원라이너를 대안으로 제시.  
- **문제**: 파일 이름에 공백이 있을 때 `for f in $(ls)`가 왜 위험한가?  
  - **답안**: 단어 분리/글로브 확장으로 파일명이 쪼개짐. `for f in *; do` 또는 `find ... -print0 | while IFS= read -r -d '' f; do` 패턴 사용.  
- **문제**: cron에서 PATH 문제를 방지하려면?  
  - **답안**: crontab 상단에 `SHELL=/bin/bash`와 `PATH=/usr/local/bin:/usr/bin:/bin` 지정. 외부 명령은 절대경로 사용. 로그/메일 경로를 명시.  
- **문제**: `set -e`를 사용해도 괜찮은가?  
  - **답안**: 예외를 이해하고 사용하면 좋다. 조건문/파이프라인 예외를 설명하고 pipefail/ERR trap을 함께 사용. 명령 치환/`local var=$(cmd)`의 함정과 대안을 제시.  

## 자가 점검 표
- [ ] 명령 옵션의 기본값과 흔한 조합을 암기했다.
- [ ] 각 도구의 확장/제한(GNU/BSD/BusyBox)을 구분해 설명할 수 있다.
- [ ] 공백/개행/비ASCII 파일명에 안전한 패턴을 적용할 수 있다.
- [ ] 원라이너를 목적에 따라 빠르게 조합할 수 있다.
- [ ] 서술형 답안을 3~4줄로 구조화하는 연습을 했다.
