# 18. 케이스 스터디 & 템플릿 모음

> 실무 상황을 가정한 예제 스크립트와 해설. 각 케이스마다 "상황 → 요구사항 → 구현 포인트 → 샘플 코드 → 시험 포인트"를 포함한다.

## Case 1. 로그 정제 후 업로드
- **상황**: 애플리케이션 로그를 필터링해 민감 정보(토큰, 이메일)를 제거하고, 압축 후 원격 서버에 전송해야 함.
- **요구사항**: 공백/비ASCII 파일명 지원, 실패 시 롤백, 전송 후 로컬 로그는 7일 보관.
- **구현 포인트**: `set -Eeuo pipefail`, `grep -Ev`로 필터, `sed -E` 치환, `tar czf`, `scp`, `find -mtime +7 -delete`. 전송 실패 시 압축본 삭제.
- **샘플 코드**:
```bash
#!/usr/bin/env bash
set -Eeuo pipefail
log_dir=${LOG_DIR:-/var/log/app}
archive=$(mktemp -p "$log_dir" filtered.XXXX.tar.gz)
trap 'rm -f "$archive"' ERR
find "$log_dir" -name '*.log' -mtime -1 -print0 \
  | xargs -0 -r tar --transform='s#.*/##' -czf "$archive" --files-from -
scp "$archive" user@backup:/data/logs/
find "$log_dir" -name '*.log' -mtime +7 -delete
```
- **시험 포인트**: `set -Eeuo pipefail`와 trap 조합, `xargs -0 -r`, `tar --files-from -` 패턴.

## Case 2. 설정 파일 병합
- **상황**: 여러 `.env` 파일을 병합해 하나의 설정을 만들고, 키 충돌 시 우선순위 적용.
- **요구사항**: 주석/빈 줄 무시, 키는 대문자+숫자+언더스코어만 허용, 후속 파일이 이전 값을 덮어씀.
- **구현 포인트**: `declare -A env`, `grep -vE '^(#|$)'`, `IFS='=' read -r k v`, `[[ $k =~ ^[A-Z0-9_]+$ ]]` 검증, 최종 출력은 `printf '%s=%s
'` 정렬.
- **샘플 코드**:
```bash
merge_env() {
  declare -gA ENV=()
  for file in "$@"; do
    while IFS='=' read -r k v; do
      [[ $k =~ ^[A-Z0-9_]+$ ]] || continue
      ENV[$k]=$v
    done < <(grep -vE '^(#|$)' "$file")
  done
  for k in "${!ENV[@]}"; do printf '%s=%s\n' "$k" "${ENV[$k]}"; done | sort
}
```
- **시험 포인트**: 연관배열, 프로세스 서브스티튜션, 정규식 검증.

## Case 3. 배포 전 헬스체크/롤백
- **상황**: 신규 바이너리 배포 후 헬스체크 실패 시 이전 버전으로 롤백.
- **요구사항**: 단계별 로그, 타임아웃, 실패 시 즉시 중단.
- **구현 포인트**: `timeout`, `systemctl restart`, `curl -fsS -m 5`, 롤백 함수, `trap 'rollback' ERR`.
- **샘플 코드**:
```bash
rollback(){ systemctl restart app@previous.service; }
trap 'rollback' ERR
systemctl restart app@candidate.service
timeout 10s curl -fsS http://localhost:8080/health
```
- **시험 포인트**: 타임아웃 종료 코드 124 처리, trap 활용.

## Case 4. CSV 처리 파이프라인
- **상황**: 대용량 CSV에서 특정 컬럼을 기준으로 집계 후 JSON으로 변환.
- **요구사항**: 헤더 건너뛰기, 결측값 0 처리, UTF-8 보장.
- **구현 포인트**: `awk -F, 'NR>1 {sum[$3]+=$4} END{...}'`, `jq -n --argjson ...` 대안, 파이프라인에서 `LC_ALL=C` 설정.
- **샘플 코드**:
```bash
LC_ALL=C awk -F, 'NR>1 {sum[$3]+=$4} END{for(k in sum) printf "%s,%d\n", k, sum[k]}' data.csv \
  | jq -R -s 'split("\n")[:-1] | map(split(",")) | map({key:.[0], value:(.[1]|tonumber)})'
```
- **시험 포인트**: `jq -R -s` 사용, 로케일 설정, awk 해시.

## Case 5. 사용자 입력 인터랙티브 스크립트
- **상황**: 메뉴 기반 스크립트에서 안전하게 입력을 받고 검증.
- **요구사항**: 시간 제한, 기본값, 잘못된 입력 반복, 비밀번호 입력 시 에코 끔.
- **구현 포인트**: `read -rp`, `read -rs`, `select` 또는 `case` 반복, `[[ $choice =~ ^[1-3]$ ]]` 검증.
- **샘플 코드**:
```bash
prompt_choice(){
  local choice
  while true; do
    read -rp "Choose [1:start 2:stop 3:quit] (default 3): " choice || return 1
    choice=${choice:-3}
    [[ $choice =~ ^[1-3]$ ]] && break
    echo "invalid" >&2
  done
  printf '%s' "$choice"
}
```
- **시험 포인트**: `read` 옵션, 정규식 검증, 기본값 처리.

## Case 6. 네트워크 상태 점검 리포트
- **상황**: 다수의 호스트/포트에 대해 연결 가능 여부와 지연시간을 측정.
- **요구사항**: 병렬 실행, 타임아웃, 결과를 표 형태로 저장.
- **구현 포인트**: `xargs -P`, `/dev/tcp`, `timeout`, `printf` 포맷팅.
- **샘플 코드**:
```bash
check(){ host=$1 port=$2
  start=$(date +%s%3N)
  if timeout 3 bash -c "</dev/tcp/$host/$port" 2>/dev/null; then
    end=$(date +%s%3N); printf '%s:%s OK %sms\n' "$host" "$port" $((end-start))
  else
    printf '%s:%s FAIL\n' "$host" "$port"
  fi
}
export -f check
paste hosts.txt ports.txt | xargs -P4 -n2 bash -c 'check "$0" "$1"' \
  | column -t >report.txt
```
- **시험 포인트**: `/dev/tcp` 사용, `column` 정렬, 병렬 실행.

## Case 7. 백업/스냅샷 관리
- **상황**: 특정 디렉터리를 날짜별 스냅샷으로 보관, 오래된 스냅샷 자동 삭제.
- **요구사항**: 증분 백업, 권한 유지, 로그 기록.
- **구현 포인트**: `rsync -a --delete --link-dest`, `date +%F`, `find -mtime +30 -delete`, `logger`로 syslog 기록.
- **샘플 코드**:
```bash
base=/backup/app
snap=$base/$(date +%F)
rsync -a --delete --link-dest="$base/latest" /data/app/ "$snap" && ln -sfn "$snap" "$base/latest"
find "$base" -maxdepth 1 -type d -name '20*' -mtime +30 -print0 | xargs -0 -r rm -rf --
logger -t backup "created snapshot $snap"
```
- **시험 포인트**: `--link-dest` 하드링크 증분, `ln -sfn` 최신 링크 갱신.

## Case 8. 텍스트 인코딩/줄바꿈 정리
- **상황**: CRLF/인코딩 혼합된 파일을 UTF-8 LF로 정리.
- **요구사항**: 바이너리 파일 제외, 백업 생성, 변경된 파일만 보고.
- **구현 포인트**: `file --mime`, `iconv`, `tr -d '\r'`, `diff` 출력.
- **샘플 코드**:
```bash
for f in "$@"; do
  mime=$(file --mime "$f")
  echo "$mime" | grep -q binary && continue
  iconv -f EUC-KR -t UTF-8 "$f" | tr -d '\r' >"$f.tmp"
  if ! cmp -s "$f" "$f.tmp"; then
    mv "$f" "$f.bak"
    mv "$f.tmp" "$f"
  else
    rm "$f.tmp"
  fi
done
```
- **시험 포인트**: 바이너리 감지, iconv 사용, cmp로 변경 여부 확인.

## Case 9. JSON 없이 로그 지표 추출
- **상황**: jq 없는 환경에서 간단한 JSON 로그에서 필드 추출.
- **요구사항**: 키/값 단순 구조, 큰따옴표 이스케이프 최소, sed/awk만 사용.
- **구현 포인트**: `sed -n 's/.*"user":"\([^"]*\)".*"status":\([0-9]*\).*/\1 \2/p'`, 또는 python 원라이너.
- **샘플 코드**:
```bash
awk 'match($0, /"user":"([^"]+)".*"status":([0-9]+)/, m){print m[1], m[2]}' app.json.log | sort | uniq -c
```
- **시험 포인트**: 정규식 캡처, awk `match()` 사용.

## Case 10. 리소스 사용량 모니터
- **상황**: 특정 프로세스 그룹의 CPU/메모리 사용률을 주기적으로 기록.
- **요구사항**: 1초 간격, 1분 후 종료, CSV 포맷.
- **구현 포인트**: `ps -o pid,ppid,pcpu,pmem,comm -C name`, `date +%s`, 루프+`sleep`.
- **샘플 코드**:
```bash
end=$((SECONDS+60))
while (( SECONDS < end )); do
  timestamp=$(date +%s)
  ps -o pid,ppid,pcpu,pmem,comm= -C myproc \
    | awk -v t=$timestamp 'NR>1{printf "%d,%s,%s,%s,%s\n", t,$1,$2,$3,$4}'
  sleep 1
done >usage.csv
```
- **시험 포인트**: ps 포맷, 시간 루프, awk 출력 포맷.

## Case 11. 안전한 삭제 스크립트
- **상황**: 사용자가 지정한 경로를 삭제하되, 루트/홈 등 위험 경로 보호.
- **요구사항**: 화이트리스트/블랙리스트 체크, 확인 프롬프트, dry-run 옵션.
- **구현 포인트**: `case`로 위험 경로 차단(`/`, `/home`, 빈 값 등), `read -rp` 확인, `rm -rf` 대신 `mv`로 격리 옵션.
- **샘플 코드**:
```bash
path=${1:?usage: cleanup PATH}
case $path in /|/*..|""|"~"|/home|/root) echo "danger" >&2; exit 2;; esac
if [${DRY_RUN:-0} -eq 1](../../${DRY_RUN:-0} -eq 1.md); then
  printf 'would remove %s\n' "$path"
else
  read -rp "Remove $path? [y/N] " ans
  [[ $ans == [Yy]* ]] || exit 0
  rm -rf -- "$path"
fi
```
- **시험 포인트**: 위험 경로 필터, confirm 프롬프트, 인용.

## Case 12. 단위 테스트 템플릿
- **상황**: bash만으로 간단한 테스트 러너 구성.
- **요구사항**: 각 테스트 이름/결과 출력, 실패 시 메시지, 종료 코드 집계.
- **구현 포인트**: `tests=(test_foo test_bar)`, 함수 반환값 체크, `set +e`로 테스트 독립 실행.
- **샘플 코드**:
```bash
tests=(test_sum test_trim)
fail=0
test_sum(){ [$((1+1)) -eq 2](../../$((1+1.md)) -eq 2.md); }
test_trim(){ [xargs) == 'a'](../../$(echo ' a '.md); }
for t in "${tests[@]}"; do
  if "$t"; then echo "PASS $t"; else echo "FAIL $t"; fail=1; fi
done
exit $fail
```
- **시험 포인트**: 함수형 테스트, 종료 코드 집계, `set +e` 고려.

## 템플릿: 스크립트 표준 헤더
```bash
#!/usr/bin/env bash
set -Eeuo pipefail
IFS=$'\n\t'
shopt -s nullglob

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
LOG_LEVEL=${LOG_LEVEL:-info}

abort(){ printf 'ERROR: %s\n' "$*" >&2; exit 1; }
log(){ printf '%s [%s] %s\n' "$(date +%F_%T)" "$1" "$2"; }
require(){ command -v "$1" >/dev/null || abort "missing $1"; }
```
- **설명**: 공통 옵션, IFS, nullglob, 스크립트 디렉터리 계산, 로깅/종료 함수 포함. 필요시 `trap`/임시 디렉터리 추가.

## 템플릿: POSIX 호환 스크립트 뼈대
```sh
#!/bin/sh
set -eu
IFS='\n\t'
usage(){ echo "usage: $0 [-f file]" >&2; exit 2; }
file=""
while getopts "f:h" opt; do
  case "$opt" in
    f) file=$OPTARG ;;
    h) usage ;;
    *) usage ;;
  esac
done
shift $((OPTIND-1))
[ -n "$file" ] || usage
```
- **설명**: POSIX `getopts`, 배열 없음, `[` 조건 사용. Bash 확장 없이 작성.

## 마무리 체크리스트
- [ ] 상황/요구사항을 먼저 명확히 정의하고, 제약사항(환경/권한/버전)을 기록했다.
- [ ] 입력 검증과 에러 처리, 롤백/정리(trap)를 포함했다.
- [ ] 공백/개행/비ASCII 안전성을 고려했다(NUL-종단, 인용, 배열 사용).
- [ ] OS/도구별 차이에 대한 대안을 서술했다.
- [ ] 실행/테스트 예시와 종료 코드 해석을 문서에 포함했다.
