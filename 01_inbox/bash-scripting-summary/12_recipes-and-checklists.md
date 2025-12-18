# 12. 레시피, 빈출 스니펫, 최종 체크

## 시험 대비 한눈에 보기
- 환경 설정: `set -Eeuo pipefail; IFS=$'\n\t'` (필요 시)
- 필수 인자 검사: `${1:?"usage: $0 input"}`
- 안전한 임시 공간: `TMPDIR=$(mktemp -d) || exit 1; trap 'rm -rf "$TMPDIR"' EXIT`
- 로그/에러 분리: `log(){ printf '%s %s\n' "$(date +%F_%T)" "$*"; }; log_err(){ log "$@" >&2; }`
- 파일 루프: `while IFS= read -r line; do ...; done < file`
- 병렬 처리: `export -f worker; printf '%s\n' "${items[@]}" | xargs -P4 -I{} bash -c 'worker "$@"' _ {}`

## 빈출 스니펫 모음

### 인자 파싱 + 도움말
```bash
usage(){ cat <<'EOH'
사용법: script.sh -f FILE [-o OUT] [--] args...
옵션: -f 필수, -o 출력, -h 도움말
EOH
}
parse_args(){
  local OPTIND opt
  while getopts ':f:o:h' opt; do
    case $opt in
      f) FILE=$OPTARG ;;
      o) OUT=$OPTARG ;;
      h) usage; exit 0 ;;
      :) log_err "option -$OPTARG requires argument"; exit 2 ;;
      \?) log_err "unknown option -$OPTARG"; exit 2 ;;
    esac
  done
  shift $((OPTIND-1))
  ARGS=($@)
  [-n ${FILE:-}](../../-n ${FILE:-}.md) || { log_err "-f is required"; exit 2; }
}
```

### 텍스트 파일 정제
```bash
clean_file(){
  local src=$1 dst=$2
  [-r $src](../../-r $src.md) || { log_err "cannot read $src"; return 1; }
  sed 's/\r$//; /^#/d; /^$/d' "$src" | awk '{$1=$1; print}' >"$dst"
}
```

### JSON 한 값 추출(jq 이용)
```bash
value=$(jq -r '.items[0].name' <"$json") || exit 1
```
- jq 미설치 환경 대비: `python - <<'PY'` 등 대체 스니펫 준비.

### 시그널 안전한 정리
```bash
cleanup(){ rm -rf "$TMPDIR"; }
trap 'cleanup' EXIT INT TERM
```

### 병렬 다운로드 예시
```bash
download(){ url=$1; out=$2; curl -fsSL "$url" -o "$out"; }
export -f download
printf '%s\n' "${urls[@]}" | xargs -P4 -n1 -I{} bash -c 'download "$1" "$2"' _ {} output_dir/$(basename {})
```

### 로그 파일 롤링
```bash
rotate(){
  local file=$1 max=${2:-5}
  for ((i=max; i>=1; i--)); do
    [-e ${file}.${i}](../../-e ${file}.${i}.md) && mv -f "${file}.${i}" "${file}.$((i+1))"
  done
  [-e $file](../../-e $file.md) && mv -f "$file" "${file}.1"
}
```

### 색상 출력(터미널일 때만)
```bash
if test -t 1; then RED='\e[31m'; RESET='\e[0m'; else RED=''; RESET=''; fi
printf "${RED}ERROR${RESET}: %s\n" "message" >&2
```

## 최종 체크리스트
- [ ] 셔뱅과 필요한 Bash 버전 명시
- [ ] `set` 옵션, `shopt` 설정 이유 주석화
- [ ] 변수/경로/배열 확장 시 더블 쿼트 적용
- [ ] 실패 가능 명령 뒤에 에러 핸들링(`|| exit`, `|| return`, `|| true` 의도 명시)
- [ ] 외부 의존성(`command -v`) 검사 및 오류 메시지 제공
- [ ] 임시 파일/디렉터리 생성 시 `mktemp`, 종료 시 `trap`으로 정리
- [ ] 로케일/타임존 의존성 확인(`LC_ALL=C`, `TZ=UTC` 등)
- [ ] 크론/systemd 등 실행 환경에서 PATH·워크디렉터리 명시
- [ ] 테스트/디버그 옵션(shellcheck, `set -x`, `RUN_TESTS` 플래그) 안내
- [ ] 배포/배포 대상 OS의 포터빌리티 문제 sed/date/readlink/timeout 점검

## POSIX 전용 대안 스니펫(배포 스크립트용)
- **필수 인자**: `[ $# -ge 1 ] || { echo "usage: $0 file" >&2; exit 2; }`
- **조건/문자열**: `[ "x$var" = "xvalue" ]` 패턴으로 빈 문자열 보호.
- **루프/파일 읽기**: `while IFS= read -r line; do ...; done < "$file"` (배열 없음).
- **임시 파일**: `tmp=$(mktemp /tmp/app.XXXXXX) || exit 1` (디렉터리는 `mktemp -d /tmp/app.XXXXXX`).
- **함수/리턴**: `my_func(){ command || return 1; }` — `local`/배열 미지원, 전역 변수 사용 주의.
- **날짜 계산**: `python - <<'PY'\nimport time; import datetime; print((datetime.datetime.utcnow()-datetime.timedelta(days=1)).strftime('%F'))\nPY`
- **readlink 대체**: `python - <<'PY'\nimport pathlib,sys; print(pathlib.Path(sys.argv[1]).resolve())\nPY` file

## 마무리 요약(초단기 암기)
- 인용: **항상 `"$var"`**
- 조건: 문자열 `[](../.md)`, 산술 `(( ))`, 파일 `[-f file](../../-f file.md)`
- 흐름: `set -Eeuo pipefail`, 필요 시 `IFS` 조정, 에러는 stderr
- 데이터: 안전한 읽기 `while IFS= read -r`, 출력은 `printf`
- 정리: `trap`으로 임시 리소스/자식 프로세스 정리
- 휴대성: Bash 확장 vs POSIX 구분, OS별 옵션 차이 기억

## 실전 미니 시나리오 10선
1. **로그 파일 압축/보존**: 하루 전 로그를 gzip하고 30일 이상은 삭제. `find /var/log/app -name '*.log.*.gz' -mtime +30 -delete` + `logrotate` 대안 서술.  
2. **대량 다운로드 & 검증**: URL 목록을 읽어 병렬 다운로드, SHA256 체크. 실패 항목 재시도 로직.  
3. **서버 헬스체크**: 포트 열림 테스트(`nc -z` 또는 `bash -c 'echo > /dev/tcp/host/port'`), 실패 시 슬랙 웹훅 전송.  
4. **CSV 컬럼 추출/집계**: 특정 컬럼의 합계/평균 계산 후 JSON 형태로 출력(`jq`/`awk`).  
5. **백업 스냅샷 관리**: `rsync`로 증분 백업, 오래된 스냅샷 삭제, 오류 시 즉시 중단/알림.  
6. **cron에서 안전하게 실행**: PATH 설정, 독점 실행을 위한 lock 파일, 로그 분리, 메일 알림 설정.  
7. **임시 파일 클린업**: `mktemp -d`로 만든 작업 디렉터리에서 작업 후 trap으로 정리, 실패 시에도 확실히 삭제.  
8. **배포 스크립트**: 빌드→아티팩트 업로드→서비스 재시작 흐름. 각 단계 종료 코드 체크와 롤백 포인트 설정.  
9. **입력 파이프라인**: 다른 명령이 표준 입력으로 던져주는 데이터를 읽어 필터링 후 결과 반환. stdin 유무를 감지해 파일/tty 대응.  
10. **환경 차단 실행**: 제한된 PATH/umask로 외부 명령 실행(`env -i PATH=/usr/bin:/bin`), 예상치 못한 환경 변수 영향 제거.

## 모범 답안 템플릿(시험용 서술 가이드)
- **질문**: \"`set -e`의 문제점은?\"  
  - **핵심**: 조건문/파이프라인 예외, 함수 내 명령 치환에서 예기치 않은 종료, ERR trap/pipefail로 보완.  
  - **예시 코드**: `set -Eeuo pipefail; trap 'echo err at $LINENO' ERR; if ! output=$(cmd); then ...; fi`\n- **질문**: \"파일 이름에 공백이 있을 때 안전한 루프?\"  
  - **핵심**: NUL-종단, `while IFS= read -r -d '' f; do ...; done < <(find . -print0)`\n- **질문**: \"POSIX sh와 Bash 차이?\"  
  - **핵심**: 배열/연관배열, `[](../.md)`, `(( ))`, process substitution, brace expansion, `echo -e` 동작.  
  - **대응**: POSIX 필요 시 `set -o posix`, 호환 코드 제시.

## 자기 점검 퀴즈(단답형)
- `PIPESTATUS` 배열의 용도는?  
- `set -u`가 켜진 상태에서 `${var:-default}`는 어떻게 동작하는가?  
- `trap 'handler' EXIT`와 `trap 'handler' ERR`의 차이는?  
- `read -r`에서 `-r` 옵션이 없는 경우 어떤 문제가 발생할 수 있는가?  
- `[$a == $b](../../$a == $b.md)`와 `[$a = $b](../../$a = $b.md)`의 차이는? (Bash에서는 동일, test는 다름)

## 간단 실습 루브릭
- 각 장의 5분 실습을 모두 수행하고, 스스로 점검한다.  
- 실패/성공 조건을 명확히 기록하고 종료 코드를 확인한다.  
- 동일 작업을 POSIX sh 문법과 Bash 확장을 각각 사용해 작성해 본다.  
- shellcheck를 돌려 경고가 모두 사라지는지 확인한다.  
- 원격/cron 환경에서 한 번 실행해보고 PATH/locale 문제를 점검한다.
