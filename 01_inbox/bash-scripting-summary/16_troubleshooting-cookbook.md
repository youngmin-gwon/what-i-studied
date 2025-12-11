# 16. 트러블슈팅 & 오류 메시지 사전

> 실무와 시험에서 자주 만나는 오류 메시지와 해결법을 짝지었다. 메시지 원문을 기억해 두면 즉석에서 원인을 추론하기 쉽다.

## 셸/문법 관련
- `syntax error near unexpected token 'fi'` → if/for/case 블록의 `then/do/esac/fi` 짝이 안 맞음, 줄 끝에 `;` 누락.
- `command not found` → PATH 문제, 실행비트 없음, CRLF(`^M`) 포함, shebang 잘못.
- `bad substitution` → Bash 확장(`${var^^}` 등)를 `/bin/sh`에서 사용했을 때. shebang 수정 또는 POSIX 문법 사용.
- `binary operator expected` → `[ $a -lt $b ]`에서 인용 누락으로 빈 문자열 비교. `"$a"`로 인용.
- `unbound variable` → `set -u` 상태에서 unset 변수 접근. `${var:-default}`로 방어.
- `too many arguments` → `rm $files` 등에 단어 분리/글로브 폭발. 배열/인용 사용.

## 파일/경로/권한
- `Permission denied` → 실행비트 없음(`chmod +x`), 디렉터리 검색 권한(X) 없음, 파일시스템 마운트 옵션(ro) 확인.
- `No such file or directory` → 상대경로 오류, 심링크 깨짐, CRLF 인한 숨은 문자. `ls -l`/`od -c`로 확인.
- `Text file busy` → 실행 중인 바이너리/스크립트를 덮어쓰려 함. 임시 파일에 작성 후 mv로 교체.
- `Device or resource busy` → 마운트 해제 실패. 열린 파일 핸들 확인(`lsof`).

## 파이프/입출력
- `write error: Broken pipe` → 파이프 수신자가 먼저 종료(SIGPIPE). `set -o pipefail`로 실패 감지, 송신자에서 에러 무시하려면 `| true` 또는 `|| true`.
- `cannot overwrite existing file` with noclobber → `set -C`가 켜짐. 의도적이면 `>| file` 사용.
- 히어독에서 `$var`가 확장돼 버릴 때 → 구분자를 인용 `<<'EOF'` 사용.

## 명령별 자주 보는 오류와 대응
- `grep: binary file matches` → 바이너리 감지. `-a`로 텍스트 취급 또는 `-I`로 바이너리 건너뜀.
- `sed: command garbled` → 슬래시 포함 치환식에서 이스케이프 누락. 다른 구분자 사용 `s|/path|/new|`.
- `awk: syntax error near line ...` → BSD/GNU 문법 차이(`tolower` 등은 동일). `awk -F'	'`처럼 인용 확인.
- `curl: (6) Could not resolve host` → DNS 실패. 프록시/네트워크 점검. `curl -v`로 디버그.
- `curl: (22) The requested URL returned error: 403` → HTTP 상태코드. 헤더/인증/메서드 확인.
- `tar: Removing leading '/' from member names` → 보안상 루트 절대경로 제거 안내. 무시 가능.
- `find: paths must precede expression` → 옵션/경로 순서 문제. `find DIR -type f ...` 순서 준수.

## cron/systemd 관련
- cron: PATH 짧음 → crontab 상단에 PATH 지정. 셸 `/bin/sh` → Bash 문법 실패 가능.
- cron: 메일 폭탄 → stdout/stderr을 파일로 보내거나 `MAILTO=""` 설정.
- systemd: `Exec format error` → shebang 누락/실행비트 없음. 유닛 파일에서 `ExecStart=/bin/bash -c '...'` 대안.
- systemd: 환경 변수 미적용 → `Environment=`/`EnvironmentFile=` 설정, 또는 `ExecStart=/usr/bin/env VAR=... cmd`.

## Git/버전 관리 스크립트
- `fatal: not a git repository` → 스크립트 실행 디렉터리 문제. `git -C /path` 사용.
- `detached HEAD` 경고 → 체크아웃 상태 설명 후 `git switch -` 등 제공.
- 후킹 스크립트에서 PATH 문제 → `PATH=/usr/bin:/bin:/usr/local/bin` 재설정.

## 포터빌리티 문제 사례와 해결
- **`readlink -f` 없음**: `python - <<'PY'` 대체 또는 `perl -MCwd=realpath`.
- **`date -d` 없음**: BSD `date -v`, 아니면 `python - <<'PY'`로 계산.
- **`sed -i` 차이**: macOS는 `-i ''`. GNU/BSD를 감지해 분기하거나, 임시 파일 생성 후 mv.
- **`timeout` 없음**: `perl -e 'alarm 5; exec @ARGV' cmd`.
- **`xargs -r` 없음**: BSD에서는 디폴트로 빈 입력에도 실행. 실행 전 `test -s file || exit 0` 등 방어.

## 성능/자원 관련 에러
- `Argument list too long` → 글로브/명령 인자 길이 제한. `find ... -print0 | xargs -0` 또는 루프 사용.
- `fork: Resource temporarily unavailable` → 프로세스 남발. 병렬 수 제한(`xargs -P`), `ulimit -u` 확인.
- `Cannot allocate memory` → 대용량 파이프라인/`mapfile` 사용 시 메모리 부족. 스트리밍 처리로 변경.

## 디버깅 팁 모음
- **문제**: 어디서 종료했는지 모른다 → `trap 'echo ERR at $BASH_SOURCE:$LINENO' ERR`.
- **문제**: 특정 함수만 디버그 → 함수 시작/끝에 `set -x`/`set +x` 삽입 또는 `BASH_XTRACEFD`로 분리.
- **문제**: 변수 값 확인 → `declare -p var`는 타입과 인용을 포함해 출력.
- **문제**: 파이프라인 중 어느 단계가 느린지 → 각 단계 앞에 `time` 붙이거나, `pv`로 처리량 확인.

## 오류-원인-대응 매핑 예시
| 메시지/증상 | 가능한 원인 | 대응 |
| --- | --- | --- |
| `[: =: unary operator expected` | 인용 없는 빈 변수 | `[ "${var:-}" = value ]`로 인용 |
| `bad array subscript` | 배열 인덱스가 비정수/비어 있음 | `${arr[${i:?}]}`로 확인 또는 조건 검사 |
| `cannot open: No such file` (tar) | 경로 앞에 `./` 필요, 글로브 실패 | `tar -cf a.tar -T <(find ...)` 등 경로 확인 |
| `Value too great for base` | `08`/`09` 8진수 해석 | `10#08`처럼 진법 지정 |
| `line XX: fg: no job control` | 스크립트에서 `fg` 사용, 비인터랙티브 | `set -m` 필요 여부 검토, 가능하면 `wait` 사용 |
| `Broken pipe` 로그 다발 | 수신자 종료 | SIGPIPE 무시/처리, `set -o pipefail` |
| `Assignment to invalid subscript range` | `${arr[@]:start:len}`에 음수/범위 문제 | 값 검증 후 사용 |

## 체크리스트: 문제 발생 시 대응 순서
1. **증상 기록**: 오류 메시지/종료 코드/재현 명령을 로그에 남긴다.
2. **환경 확인**: `$0`, `$SHELL`, `set -o`, `shopt`, `uname -a`, `bash --version` 등 캡처.
3. **입력/경로 검증**: `printf '%q\n'`으로 인자/경로를 재확인, CRLF 여부 확인.
4. **실패 지점 좁히기**: 파이프라인을 나누고 `set -x` 부분 적용, `return` 값 로깅.
5. **포터빌리티 여부 판단**: `/bin/sh` 사용? GNU 도구? BusyBox? 환경에 맞춰 문법/옵션 조정.
6. **대체 경로 제시**: 해당 환경에서 동등한 명령 또는 짧은 스크립트로 우회.
7. **사후 조치**: 원인/조치/재현 절차를 문서화하여 시험 답안이나 팀 위키에 남긴다.

## 로그/디버그 절차 예시
1. **재현 스크립트 최소화**: 문제가 되는 부분만 남긴 10줄 내외의 스크립트 작성. 입력 데이터도 최소화.  
2. **추적 켜기**: `PS4='+$LINENO ' bash -x repro.sh 2>trace.log`, 로그에서 첫 실패 지점 찾기.  
3. **환경 덤프**: `env | sort`, `declare -p`로 의심 변수 출력. `set -o`, `shopt` 상태 기록.  
4. **외부 의존성 확인**: `command -v` 결과와 버전(`--version`/`-V`). 버전 차이가 문제를 일으키는지 비교.  
5. **입력/출력 샘플 저장**: 실패한 입력/출력을 파일로 저장해 회귀 테스트 데이터로 활용.  
6. **정리**: 트랩/임시 파일 해제 후 다시 실행해도 동일한지 확인. 일회성 상태(캐시/락) 문제排除.  

## FAQ 스타일 Q&A
- **Q:** `set -e` 상태에서 `grep pattern file || true`가 로그에 에러를 남긴다. 어떻게 조용히 처리할까?  
  **A:** `grep -q pattern file 2>/dev/null || true`처럼 stderr를 버리거나, 미매치가 정상 케이스임을 주석으로 명시.  
- **Q:** 파이프라인 중간 명령이 `SIGPIPE`로 죽을 때 스크립트가 성공으로 간주된다.  
  **A:** `set -o pipefail` 설정 또는 `PIPESTATUS` 확인. 필요 시 `|| exit` 추가.  
- **Q:** `readlink -f`가 없는 환경에서 심링크를 절대경로로 바꾸고 싶다.  
  **A:** `python3 - <<'PY'`로 `pathlib.Path(...).resolve()` 사용. macOS는 coreutils `greadlink` 설치 대안.  
- **Q:** `mktemp`가 실패한다.  
  **A:** `/tmp` 권한/공간 부족, 템플릿 형식 오류. 다른 디렉터리 지정 `TMPDIR=/var/tmp mktemp -d`, 템플릿에 `XXXXXX` 포함.  
- **Q:** `Permission denied`가 계속 발생한다.  
  **A:** SELinux/AppArmor, 파일시스템 마운트 옵션(noexec), 디렉터리 x 권한, sudo PATH 차이 등을 순서대로 점검.  

## 추가 케이스: 시간/타임존 이슈
- **증상**: 로그 타임스탬프가 미래/과거로 찍힘, cron이 엉뚱한 시간에 실행.  
- **원인**: `TZ` 설정 누락, 컨테이너와 호스트 시간대 불일치, `date -d`/`-v` 동작 차이.  
- **대응**: `TZ=UTC` 또는 원하는 TZ 명시, `/etc/localtime` 마운트 확인, `date +%s`로 epoch 기반 계산, `python - <<'PY'`로 표준화.  

## 추가 케이스: locale/인코딩 문제
- **증상**: `sort` 결과가 기대와 다름, `tr '[:upper:]' '[:lower:]'` 동작 이상, `grep`이 멀티바이트에서 깨짐.  
- **원인**: `LC_ALL`/`LANG` 값에 따른 로케일 차이.  
- **대응**: 로케일을 명시적으로 설정(`LC_ALL=C` 또는 `LC_ALL=en_US.UTF-8`), 입력 파일 인코딩 확인(`file --mime`), iconv로 변환.  

## 실습: 트러블슈팅 체크
1. 실패한 스크립트를 `bash -n`으로 돌려 문법 오류 여부부터 확인.  
2. `/bin/sh`로 실행했을 때와 `/bin/bash`로 실행했을 때의 차이를 기록.  
3. BusyBox 환경에서 동일 스크립트를 실행해보고 실패한 부분을 표시.  
4. `env -i PATH=/usr/bin:/bin bash -c '...'`로 깨끗한 환경에서 재현.  
5. `strace -f -e execve`(가능한 환경에서)로 어떤 명령을 호출하는지 확인.  
