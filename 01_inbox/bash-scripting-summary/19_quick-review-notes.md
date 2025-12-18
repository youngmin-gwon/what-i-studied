# 19. 초압축 회독 노트 (시험 직전용)

> 각 장의 핵심만 다시 모아 10분 안에 훑을 수 있도록 구성했다. 추가로 빈출 암기 포인트, 짧은 문제, 하루 전 점검표를 포함했다.

## 1) 챕터별 3줄 요약
- **쉘 개요**: 셔뱅/로그인·비로그인/인터랙티브 구분, PATH 탐색과 해시. shebang 없으면 `/bin/sh`로 실행될 수 있음.
- **인용·확장**: 확장 순서(브레이스→틸드→파라미터→명령→산술→글로브→단어분리), 항상 `"$var"`, `${var:?msg}`로 필수 인자 검증.
- **변수·배열**: `local/export/readonly`, 배열/연관배열 인용, `${var/pat/repl}` 패턴, 특수변수 `$?/$#/$@/$*`.
- **조건·루프**: `[](../.md)` vs `[ ]`, 정규식 `=~`, `(( ))` 산술, `while read` 패턴, `set -e` 예외 인지.
- **함수/모듈**: `local`, `return` vs `exit`, `getopts`에 `local OPTIND`, source 시 경로/존재 확인.
- **I/O/파이프**: `> >> < 2> &>` 차이, 히어독 인용, pipefail/PIPESTATUS, 프로세스 서브스티튜션.
- **텍스트 툴**: grep/sed/awk/coreutils 옵션, 인코딩/CRLF 주의, NUL-종단 처리.
- **프로세스/시그널**: `trap EXIT/INT/TERM`, `wait`로 종료 코드 회수, `timeout`, `/dev/tcp`.
- **환경/스타트업**: `.bashrc/.bash_profile/.profile`, BASH_ENV, cron/systemd 환경 차이.
- **디버깅/테스트**: `set -x`, `PS4`, shellcheck, 간단 테스트 러너, 로깅/stderr 분리.
- **보안/성능**: 입력 검증, `mktemp`, umask, 포터빌리티(sed/date/readlink), 서브프로세스 최소화.
- **레시피**: 인자 파싱, 로그/임시 처리, 병렬 실행, 체크리스트.

## 2) 즉답 문제집 (15문제)
1. `set -e`가 작동하지 않는 3가지 맥락은?  
2. `${var:=default}`와 `${var:-default}` 차이는?  
3. 파일명에 공백이 있을 때 안전한 루프는?  
4. `/bin/sh`에서 `[-f file](../../-f file.md)`가 실패하는 이유와 대안은?  
5. `PIPESTATUS`가 무엇을 담는지 예시와 함께 설명하라.  
6. `mapfile` 대신 `arr=($(cmd))`가 위험한 이유는?  
7. `trap '...' EXIT`와 `trap '...' ERR`의 차이점은?  
8. `read -r -d '' var <<'EOF'` 패턴의 장점은?  
9. cron에서 PATH 문제를 해결하는 방법 두 가지는?  
10. macOS에서 `readlink -f` 대안은?  
11. `timeout` 종료 코드 124의 의미는?  
12. `set -C`가 켜진 상태에서 덮어쓰려면 어떻게 하는가?  
13. `extglob`을 켜면 사용할 수 있는 패턴 예시는?  
14. `grep -E`와 `grep -F`의 차이는?  
15. `nohup`과 `disown`의 차이를 설명하라.

## 3) 암기 카드 (키워드 → 설명)
- **PIPESTATUS**: 파이프라인 각 명령의 종료 코드 배열(Bash). `echo "${PIPESTATUS[@]}"`.
- **ERR trap**: `set -E`로 함수/서브셸 전파. `set -e`와 다름.
- **nullglob/failglob**: 글로브 매칭 실패 시 빈/오류. 파일 없을 때 루프 안전성.
- **lastpipe**: 마지막 파이프 명령을 현재 셸에서 실행(비인터랙티브, `set +m` 필요).
- **`[=~](../../=~.md)`**: 정규식 매칭, 인용하면 리터럴. `BASH_REMATCH`에 캡처.
- **`<<<`**: 히어스트링, 한 줄을 stdin으로. POSIX 아님.
- **`mapfile/readarray`**: 파일을 배열로. Bash 4+, `-t`로 개행 제거.
- **`getopts`**: POSIX 옵션 파서, `OPTIND`는 함수마다 `local` 필요.
- **`mktemp`**: 안전한 임시 파일/디렉터리 생성. 템플릿 필요, 권한 700/600.
- **`shopt -s globstar`**: `**` 재귀 글로브. `find` 대체 가능.
- **`command -v`**: 실행 대상 확인(함수/빌트인 포함). `which`보다 신뢰도 높음.
- **`set -o posix`**: Bash를 POSIX 모드로, 확장 일부 비활성화.
- **`flock`/lockdir**: 동시 실행 방지. BusyBox/OS별 지원 여부 확인.
- **`LC_ALL=C`**: ASCII 정렬/매칭, 속도 ↑, 로케일 의존 제거.
- **`BASH_ENV`**: 비인터랙티브 셸 초기화 파일 경로.

## 4) 하루 전 점검표
- [ ] 시험 환경(배포판/Bash 버전/`/bin/sh` 구현) 확인
- [ ] 옵션 세트, 히어독/인용/글로브/IFS 개념 재점검
- [ ] POSIX vs Bash 차이 암기(`[](../.md)`, 배열, `<<<`, process substitution)
- [ ] `grep/sed/awk` 옵션 숙지, macOS/BSD 차이(`sed -i`, `date -v`)
- [ ] `trap`/시그널 흐름, `timeout`/`wait`/`jobs` 명령 사용법 복습
- [ ] cron/systemd 실행 환경 차이와 PATH 설정법 숙지
- [ ] shellcheck 경고 ID 몇 개 외워두기(SC2086/2164/2046 등)

## 5) 60초 스니펫 모음
- **필수 인자**: `: "${1:?usage: $0 <arg>}"`
- **안전한 루프**: `while IFS= read -r -d '' f; do ...; done < <(find . -print0)`
- **로그**: `log(){ printf '%s [%s] %s\n' "$(date +%F_%T)" "$1" "$2"; }`
- **타임아웃 없이 kill**: `sleep 5 & pid=$!; wait $pid || echo "fail $?"`
- **JSON 파싱**: `value=$(jq -r '.key' file || true)`
- **POSIX 조건**: `[ -n "$var" ] && [ -f "$file" ] || exit 1`
- **NUL join**: `printf '%s\0' "${arr[@]}" | xargs -0 -n1`

## 6) 빈출 실수 → 바로잡기
- `for f in $(ls *.txt)` → **올바른 예**: `shopt -s nullglob; for f in *.txt; do ...; done`
- `echo -e`로 개행/이스케이프 처리 → **올바른 예**: `printf 'line\n'`
- `rm -rf /tmp/$user`에서 `$user` 빈 값 → **올바른 예**: `rm -rf "/tmp/${user:?missing user}"`
- `cat file | grep pattern` → **올바른 예**: `grep pattern file`
- `sed -i 's/a/b/'` macOS 실패 → **올바른 예**: `sed -i '' 's/a/b/' file`
- `read`에서 `-r` 빠짐 → **올바른 예**: `while IFS= read -r line; do ...; done`
- `curl URL | sh` 무검증 실행 → **올바른 예**: 해시 검증, `set -euo pipefail`, 서명 확인 후 실행.

## 7) 초간단 요약 슬로건
- **인용**: 모르면 `"$var"`
- **조건**: 문자열 `[](../.md)`, 파일 `[ -f ]`, 산술 `(( ))`
- **입력**: `while IFS= read -r` + `mapfile` 기억
- **오류**: `set -Eeuo pipefail` + `trap` + 명시적 종료 코드
- **휴대성**: Bash 확장 vs POSIX, GNU vs BSD 옵션 차이 명시

## 8) 더 풀어볼 연습 과제
1. `set -euo pipefail`가 켜진 상태와 아닌 상태에서 동일 파이프라인(`false | true`)을 실행하고 차이를 설명하는 리포트를 작성하라.  
2. cron과 systemd timer에 동일 스크립트를 배치했을 때 환경 차이(PATH, 워킹디렉터리, 셸)를 실험하고 표로 정리하라.  
3. BusyBox `sh`에서 Bash 스크립트를 실행했을 때 실패하는 부분을 나열하고, POSIX 대안을 제시하라.  
4. `awk`와 `jq`로 동일 JSON 변환 작업을 수행하고, 성능/가독성/의존성 측면에서 비교하라.  
5. 테스트가 없는 기존 스크립트에 최소 단위 테스트 3개를 추가하고, shellcheck를 통해 사전 버그를 제거하라.
