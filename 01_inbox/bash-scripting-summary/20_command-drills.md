# 20. 커맨드 드릴 세트 (손에 익히기)

> 시험/면접 준비용으로 1~2줄씩 바로 실행해볼 수 있는 드릴을 모았다. 각 드릴은 목표, 커맨드, 기대 결과, 변형 아이디어로 구성된다.

## Drills: 파일/디렉터리
1. **숨김 포함 파일 개수 세기**  
   `shopt -s dotglob; echo * | wc -w`  
   변형: `find . -maxdepth 1 | wc -l`
2. **확장자별 개수**  
   `find . -type f -name '*.log' -printf '%f\n' | sed 's/.*\.//' | sort | uniq -c`  
   변형: macOS `-print`+`awk -F. '{print $NF}'`
3. **가장 큰 5개 파일**  
   `find . -type f -printf '%s %p\n' | sort -nr | head -n 5`  
   변형: `du -ah . | sort -hr | head -n 5`
4. **권한 일괄 변경**  
   `find . -type f -name '*.sh' -exec chmod 750 {} +`  
   변형: `-perm /111` 실행 파일만

## Drills: 텍스트 처리
1. **특정 컬럼 평균**  
   `awk '{sum+=$3} END{print sum/NR}' data.txt`  
   변형: 구분자 `-F,` 추가
2. **문자열 치환 확인**  
   `sed -n 's/foo/bar/gp' file` (치환된 줄만 출력)  
   변형: `-i.bak` 인플레이스
3. **정규식 캡처 연습**  
   `grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' log`  
   변형: `awk 'match($0,/([0-9]{4})-([0-9]{2})-([0-9]{2})/,m){print m[1],m[2],m[3]}'`
4. **UTF-8 아닌 파일 찾기**  
   `find . -type f -maxdepth 2 -print0 | xargs -0 -n1 file --mime | grep -v 'charset=utf-8'`

## Drills: 네트워킹/프로세스
1. **열려 있는 포트 확인**  
   `ss -tlnp | head` 또는 `netstat -tlnp`  
   변형: macOS `lsof -iTCP -sTCP:LISTEN`
2. **HTTP 헤더 보기**  
   `curl -I https://example.com`  
   변형: `-k`(검증 끔), `-H 'User-Agent: test'`
3. **프로세스별 FD 수**  
   `ls /proc/$(pgrep -n sshd)/fd | wc -l`  
   변형: `lsof -p PID | wc -l`
4. **PID 존재 여부**  
   `kill -0 $pid && echo alive || echo dead`

## Drills: Bash 문법
1. **파라미터 확장 패턴**  
   `path=/tmp/app.log; echo "${path%/*}" "${path##*/}"`  
   변형: 접두사 제거 `${var#prefix}`
2. **배열 슬라이싱**  
   `arr=(a b c d); echo "${arr[@]:1:2}"`  
   변형: 음수 오프셋 `${arr[@]: -2}`
3. **정규식 매칭**  
   `s=abc123; [[ $s =~ ^[a-z]+([0-9]+)$ ]] && echo "num=${BASH_REMATCH[1]}"`
4. **산술 루프**  
   `for ((i=0;i<5;i++)); do echo $i; done`

## Drills: 안전성/보안
1. **mktemp 사용**  
   `tmp=$(mktemp -d) || exit 1; echo $tmp; rm -rf "$tmp"`  
   변형: 파일 템플릿 `mktemp /tmp/app.XXXXXX`
2. **입력 검증**  
   `name=$1; [[ $name =~ ^[a-z_][a-z0-9_-]*$ ]] || exit 2`
3. **PATH 오염 방지**  
   `PATH=/usr/bin:/bin:/usr/local/bin; export PATH`  
   변형: 함수로 prepend/append
4. **sudo 최소 사용**  
   `sudo -u appuser cmd`  
   변형: `sudo -E` 환경 유지 주의

## Drills: 디버깅
1. **PS4 추적**  
   `PS4='+$LINENO ' bash -x script.sh`  
   변형: `BASH_XTRACEFD=3 bash -x script.sh 3>trace.log`
2. **ERR 위치 로그**  
   `trap 'echo ERR at $LINENO' ERR; set -e; false`  
   변형: `set -E`로 함수 내부까지
3. **PIPESTATUS 확인**  
   `false | true | cat; echo "${PIPESTATUS[@]}"`
4. **shellcheck**  
   `shellcheck script.sh` (없으면 `docker run --rm -v "$PWD":/mnt koalaman/shellcheck script.sh`)

## Drills: 크론/systemd 대비
1. **cron PATH 확인**  
   `* * * * * /usr/bin/env > /tmp/cron.env` (crontab)  
   변형: `SHELL=/bin/bash` 설정
2. **systemd 환경파일**  
   `EnvironmentFile=/etc/app.env` 사용 예시 작성  
   변형: `Environment=KEY=VALUE`
3. **워킹디렉터리 설정**  
   `WorkingDirectory=/srv/app`  
   변형: 스크립트에서 `cd -- "$SCRIPT_DIR" || exit`

## 빠른 체크리스트
- [ ] 드릴을 직접 터미널에서 실행해봤다.
- [ ] 동일 드릴을 POSIX sh 문법으로도 시도했다.
- [ ] 실패/성공 시 출력과 종료 코드가 어떻게 달라지는지 기록했다.
- [ ] 변형 아이디어를 추가로 작성하며 손에 익혔다.
- [ ] 드릴 중 익숙하지 않은 옵션은 man page로 확인했다.

## 추가 미션(심화)
- **에러 처리 체감**: `set -Eeuo pipefail`을 켜고 끄며 동일 드릴 실행, 어디서 멈추는지 비교 로그 작성.
- **포터빌리티 실험**: macOS/BSD/BusyBox 환경에서 Drills를 반복 실행, 실패한 명령/옵션을 표로 정리.
- **성능 측정**: `time`/`/usr/bin/time -v`로 텍스트 처리 드릴의 처리량 비교, `LC_ALL=C` 영향 기록.
- **테스트 데이터 생성**: `seq`/`yes`/`python - <<'PY'` 등을 활용해 대용량 샘플을 만들고 드릴을 적용.
- **스크립트화**: 자주 쓰는 드릴을 함수로 모아 `drills.sh`로 저장 후 `source`하여 재사용.

## 실행 메모(샘플 결과)
- **pipefail 드릴**: `false | true` → 0, `set -o pipefail` 후 동일 명령 → 1.
- **nounset 드릴**: `set -u; echo \"${UNSET:-ok}\"` → `ok` 출력 후 정상 종료.
- **failglob 드릴**: `shopt -s failglob; for f in *.definitely_not_exist; do :; done` → `bash: no match: ...`, 종료코드 1.
- **lastpipe 드릴**: macOS 기본 bash 3.x에서는 `shopt -s lastpipe` 미지원(`invalid shell option name`). Bash 4+ 필요.
