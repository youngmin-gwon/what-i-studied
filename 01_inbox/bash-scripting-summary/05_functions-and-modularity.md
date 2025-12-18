# 05. 함수, 모듈화, 재사용

## 시험 포인트
- 함수 선언 두 가지: `name() { ...; }` 와 `function name { ...; }`(POSIX 아님)
- 함수는 종료 코드로 성공/실패 전달. `echo`로 값 반환하지 않도록 구분.
- 네임스페이스: 접두사/파일 분리, `readonly -f`로 보호 가능
- `source`로 모듈 로딩, `set -o errexit` 환경에서의 로딩 실패 처리
- 라이브러리 함수 작성 시 입력 검증, 로깅, 실패 시 exit vs return 기준

## 함수 기본 패턴
```bash
my_func() {
  local msg=${1:?"message required"}
  printf '%s\n' "$msg"
}
```
- `local`은 함수 스코프 변수. 상위 변수와 이름 충돌 방지.
- 인자 읽기는 `$1`, `$#`, `$@` 동일 규칙. 필요시 `shift`.
- 함수 정의는 실행 전에 읽혀야 하므로 스크립트 상단 또는 source 파일에서 정의.

## 반환값과 종료 처리
- 함수의 `return N`은 0-255. 문자열을 반환하려면 `echo` 또는 전역 변수/명령 치환 사용.
- 길이가 긴 데이터는 전역 변수 대신 stdout을 통해 파이프/명령 치환 사용.
- 실패 시 `return 1`하고 호출부에서 `||` 처리. 라이브러리 함수는 직접 `exit`하지 않는 것이 일반적.

## 모듈 분리와 로딩
- 공통 함수는 `lib/strings.sh`, `lib/fs.sh` 등으로 분리하고 `source "$(dirname "$0")/lib/strings.sh"`로 로딩.
- `set -e` 상태에서 `source` 실패하면 스크립트 종료. 파일 존재 여부 체크: `[ -r "$lib" ] || { echo "missing $lib" >&2; exit 1; }`
- 동일 함수 재정의 방지: `declare -F funcname >/dev/null || funcname() { ...; }`

## 네임스페이스와 충돌 방지
- 접두사 규칙: `fs_list`, `str_trim`, `log_info`처럼 영역을 명시
- 전역 변수는 대문자+접두사: `APP_ROOT`, `LOG_LEVEL`
- `readonly -f log_error`로 핵심 함수 보호 가능(테스트 시 불편 주의)

## 로깅/에러 헬퍼 예시
```bash
log() { local lvl=$1 msg=${2:-}; printf '%s [%s] %s\n' "$(date +%F_%T)" "$lvl" "$msg"; }
log_err() { log ERROR "$1" >&2; }
abort() { log_err "$1"; exit 1; }
```
- 표준 오류 사용을 분리해 파이프라인에 쓰레기 출력이 섞이지 않도록 함.
- 시험 문제에서 "조용한" 함수 작성 시 stdout을 오염하지 않는 것이 중요.

## 인자 파싱 스켈레톤
```bash
parse_args() {
  local OPTIND opt
  while getopts ':f:o:hv' opt; do
    case $opt in
      f) FILE=$OPTARG ;;
      o) OUTPUT=$OPTARG ;;
      h) usage; exit 0 ;;
      v) VERBOSE=$((VERBOSE+1)) ;;
      :) echo "option -$OPTARG requires an argument" >&2; return 1 ;;
      \?) echo "unknown option -$OPTARG" >&2; return 1 ;;
    esac
  done
  shift $((OPTIND-1))
  REMAINING=($@)   # 남은 인자 보관
}
```
- `getopts`는 POSIX 호환. `OPTIND`는 글로벌이므로 함수 안에서 `local OPTIND` 선언해야 재사용 가능.

## 테스트 가능성 확보
- 순수 함수처럼 stdout만 사용하는 유틸은 별도 파일로 추출 → 셸체크/단위테스트 가능
- 상태 변경(파일 작성/삭제)은 별도 함수로 분리하고 임시 디렉터리를 인자로 받게 설계
- 외부 명령 의존성은 상단에서 `command -v`로 검증

## 5분 실습
1. `local OPTIND=1`을 빼고 함수 두 번 호출했을 때 옵션 파싱이 망가지는지 확인
2. `source missing.sh`에서 `set -e`와 `set +e` 상태 비교
3. `return 2`한 함수를 `if my_func; then ...; fi`로 감싸 종료 코드 흐름 관찰

## 체크리스트
- [ ] 함수 내 변수는 기본적으로 `local`, 필요한 경우에만 전역
- [ ] 함수는 데이터를 stdout으로, 상태는 종료 코드로 반환
- [ ] `getopts` 사용 시 `local OPTIND OPTARG` 선언
- [ ] 공통 함수는 별도 파일로 두고, 로딩 실패 시 명확한 오류 메시지/종료 코드
- [ ] 로깅/에러 출력은 stderr, 정상 출력은 stdout으로 분리

## 심화: 구조화와 재사용성
- **라이브러리 구조 제안**: `lib/log.sh`, `lib/fs.sh`, `lib/str.sh` 등 기능 단위 분리. 각 파일 상단에서 의존성 확인.
- **네임스페이스**: `log::info`, `fs::ensure_dir`처럼 구분해 충돌 방지(구두점은 단순 이름). Bash에서는 `function log::info { ...; }` 가능.
- **계약(Contract)**: 함수 입력/출력/종료 코드 정의를 주석으로 남김. 시험 답안에서 \"0:success, 1:usage, 2:runtime\" 등 명시하면 깔끔.
- **모킹**: 테스트 시 `PATH` 앞에 `tests/fakes`를 추가하여 외부 명령을 대체. 함수는 항상 `command -v`로 존재 확인 후 실행.

## 상태 관리와 에러 전파
- **옵션 전파**: 라이브러리 로딩 전에 `set -Eeuo pipefail` 선언 시, 라이브러리 내부에서도 동일 옵션이 적용됨. 예외가 필요한 부분은 `set +e` 블록으로 감싼 뒤 복원.
- **return vs exit**: 라이브러리 함수에서는 `return`으로만 실패를 알리고, 최상위 `main`에서 exit 결정. 시험 문제에서 이 구분을 묻는 경우가 많음.
- **함수 포인터 흉내**: `callback=$1; shift; "$callback" "$@"` 패턴으로 함수를 인자로 전달 가능.

## 실무 예제: 설정 로더
```bash
load_env_file() {
  local file=$1
  [-r $file](../../-r $file.md) || { log_err "missing $file"; return 1; }
  while IFS='=' read -r k v; do
    [[ $k =~ ^[A-Z0-9_]+$ ]] || continue
    printf -v "$k" '%s' "$v"
    export "$k"
  done < <(grep -vE '^(#|$)' "$file")
}
```
- `printf -v`를 사용해 서브프로세스 없이 값 설정 → 성능과 set -e 안전성 향상.

## 연습 문제
1. `getopts`를 함수 안에서 두 번 호출했을 때 OPTIND를 초기화하지 않으면 어떤 문제가 생기는가?  
2. `source` 실패를 잡는 패턴 두 가지를 작성하라(`set -e` on/off 상황 모두).  
3. `log::info` 같은 네임스페이스 함수 이름이 가독성/충돌 방지에 왜 유리한지 설명하라.  
4. 외부 명령에 의존하는 함수를 테스트할 때 PATH를 어떻게 조작하면 좋은지 예를 들어라.  
5. 함수가 stdout으로 로그를 찍으면 어떤 문제가 생기는가? 파이프라인 연결성 관점에서 설명하라.
