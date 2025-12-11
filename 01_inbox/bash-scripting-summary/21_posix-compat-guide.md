# 21. POSIX sh 호환 가이드

> `/bin/sh`로 실행되는 스크립트나 BusyBox/대시 환경을 위한 최소 문법/도구 가이드. Bash 전용 기능을 피하고 대안을 제시한다.

## 핵심 원칙
- **배열/연관배열 없음**: 공백 포함 데이터는 NUL-종단(find -print0) 또는 구분자+while read 패턴으로 다룬다.
- **`[[ ]]`, `(( ))`, `function`, `local`, `<<<`, process substitution 없음**: `[ ]`, `$(( ))`, POSIX 함수 `name(){ ...; }`, 전역 변수 사용.
- **확장 글로브/brace 없음**: `{1..3}`, `@( )`, `**` 미지원. 단순 패턴(`*`, `?`, `[...]`)만 사용.
- **내장 echo 옵션 불확실**: `printf` 사용. `echo -e`, `-n` 동작이 구현마다 다르다.
- **옵션 차이**: `readlink -f`, `sed -i`, `date -d`, `timeout` 등은 없다. 대안 사용.

## 사용 패턴 (POSIX)
- **필수 인자 검사**: `[ $# -ge 1 ] || { echo "usage: $0 arg" >&2; exit 2; }`
- **문자열 비교**: `[ "x$var" = "xval" ]`, `[ -n "$var" ]`, `[ -z "$var" ]`
- **숫자 비교**: `[ "$a" -lt "$b" ]`, `[ "$a" -eq "$b" ]`
- **파일 테스트**: `[ -f "$f" ]`, `[ -d "$d" ]`, `[ "$f1" -nt "$f2" ]`
- **조건 조합**: `[ cond1 ] && do_something` / `[ cond1 ] || handle_error`
- **루프/읽기**:
  ```sh
  while IFS= read -r line; do
    printf '%s\n' "$line"
  done < "$file"
  ```
- **옵션 파싱** (`getopts`):
  ```sh
  usage(){ echo "usage: $0 [-f file] [-v]" >&2; exit 2; }
  file= verbose=0
  while getopts "f:vh" opt; do
    case "$opt" in
      f) file=$OPTARG ;;
      v) verbose=1 ;;
      h|*) usage ;;
    esac
  done
  shift $((OPTIND-1))
  ```
- **함수**:
  ```sh
  do_work() {
    cmd || return 1
  }
  ```
- **임시 파일/디렉터리**: `tmp=$(mktemp /tmp/app.XXXXXX) || exit 1`; 디렉터리는 `mktemp -d /tmp/app.XXXXXX`

## Bash 전용 기능 → POSIX 대체
- `[[ ]]` → `[ ]` + 인용, 정규식 필요 시 `grep`/`expr`/`case`
- 배열 → 파일/여러 변수/줄 단위 처리. 공백이 있으면 NUL-종단 사용.
- `(( ))` → `$(( ))` 산술 확장(지원), 또는 `expr`
- brace expansion → `seq`/`printf '%s\n' 1 2 3`/루프
- process substitution `<( )` → `mkfifo` 또는 임시 파일, `cat >tmp; cmd tmp`
- `readarray/mapfile` → `while IFS= read -r line; do list=$list"$nl$line"; done`
- `set -o pipefail` → 미지원. 파이프라인 종료 코드 확인은 `cmd1 | cmd2; status=$?;` 대신 단계별 실행/임시 파일로 분리
- `timeout` → `perl -e 'alarm 5; exec @ARGV' cmd` 또는 `python - <<'PY' ...`
- `readlink -f` → `python - <<'PY'` realpath, 또는 순차 디렉터리 이동
- `sed -i` → `sed 's/a/b/' file >file.tmp && mv file.tmp file`
- `date -d` → `python - <<'PY'` 또는 `perl -MPOSIX`

## 표준 도구/옵션 호환성 요약
- **sed**: 인플레이스 없음, ERE는 `-E`(BSD) 또는 `-r`(GNU). POSIX는 기본 BRE.
- **awk**: POSIX awk 사용. GNU 확장 함수 일부 미지원 가능. `-F`, `BEGIN/END`, `NR/NF`는 공통.
- **find**: `-print0`는 GNU/BSD 지원. `-maxdepth`는 일부 old find 미지원.
- **xargs**: BSD에 `-r` 없음(빈 입력에도 실행). `-0`는 GNU/BSD 둘 다.
- **grep**: `-E`(ERE), `-F`(fixed). `-P`(PCRE) 미지원. `-R`/`-r` 차이 주의.
- **printf**: POSIX 지원. `%b`/`%q` 등 확장은 기대하지 말 것.

## 실행 환경 체크리스트
- `/bin/sh`가 무엇인지 확인: `ls -l /bin/sh`, `echo "$0"` (dash/busybox/bash 3.x 등).
- `POSIXLY_CORRECT`나 `set -o posix`가 필요한지 결정.
- coreutils 유무: macOS/BSD는 GNU 옵션 일부 없음 → 스크립트에서 분기하거나 python 대안 준비.
- BusyBox: `timeout`/`stat` 옵션, `df -P` 등 표준 옵션으로 한정.
- 로케일: `LC_ALL=C`로 ASCII 기준 정렬/매칭. 멀티바이트 필요 시 `UTF-8` 명시.

## 예제: POSIX 호환 파일 정제
```sh
#!/bin/sh
set -eu
IFS='
	'
usage(){ echo "usage: $0 infile outfile" >&2; exit 2; }
[ $# -eq 2 ] || usage
in=$1 out=$2
[ -r "$in" ] || { echo "cannot read $in" >&2; exit 1; }
tmp=$(mktemp /tmp/clean.XXXXXX) || exit 1
trap 'rm -f "$tmp"' 0
sed 's/\r$//' "$in" | awk 'NF{print}' >"$tmp"
mv "$tmp" "$out"
```
- 포인트: `set -eu`, 인용, CR 제거+빈 줄 제거, mktemp+trap, POSIX 도구만 사용.

## 시험 대비 요약(단답)
- `/bin/sh`에서 실패하는 Bash 기능 4가지는? → 배열, `[[ ]]`, `(( ))` 확장, process substitution/brace expansion.
- `set -o pipefail`이 없는 환경에서 파이프라인 실패를 잡는 방법은? → 단계 분리, 임시 파일, 종료 코드 변수 저장.
- macOS에서 `readlink -f` 대체는? → `python3 - <<'PY'` realpath 또는 coreutils `greadlink`.
- `sed -i`가 없을 때 안전하게 덮어쓰는 절차는? → `sed ... >tmp && mv tmp file`.
- BusyBox `xargs`가 빈 입력에서도 실행되는 것을 막으려면? → 실행 전에 `test -s file || exit 0`.
