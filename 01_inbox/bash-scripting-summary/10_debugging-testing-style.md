# 10. 디버깅, 테스트, 스타일 가이드

## 시험 포인트
- Bash 옵션: `set -x`(trace), `-e`(errexit), `-u`(nounset), `-o pipefail`, `-E`(함수/서브셸에서도 ERR), `-T`(functrace)
- `PS4` 커스터마이징으로 추적 로그 가독성 향상
- `shellcheck` 정적 분석 사용법과 빈출 경고 해결 패턴
- 단위 테스트 프레임워크 개요: `bats`, 간단한 self-test 함수 작성법
- 포매팅/스타일: 인용 규칙, 함수/변수 네이밍, 에러 핸들링 일관성

## 디버깅 옵션
- `set -x`: 실행되는 명령을 STDERR로 출력. `PS4='+${LINENO}: '` 등으로 위치 표시.
- `set -e`: 실패 시 종료. 예외 규칙이 많으므로 신중히 사용, 필요 시 `set +e` 블록 활용.
- `set -u`: unset 변수 사용 시 오류. 디폴트값 패턴 `${var:-}` 활용.
- `set -o pipefail`: 파이프라인 실패 감지.
- `set -E`: 함수/서브셸에서도 ERR 트랩 전파.

## 디버깅 테크닉
- 부분 실행: 입력 데이터를 `head`, `tail`, `sed -n '1,20p'`로 축소해 재현
- `printf` 디버깅: `printf 'DEBUG %s=%q\n' "$var" "$other" >&2`
- `trap 'echo "ERR at $BASH_SOURCE:$LINENO" >&2' ERR`로 오류 위치 추적
- 임시로 `exec 3>&1 4>&2` 후 로깅을 별도 FD로 분리해 파이프라인 영향 제거

## shellcheck 활용
- 설치 후 `shellcheck script.sh`. 경고 ID(SC2086 등)를 보고 해결.
- 빈출 해결: 단어 분리 경고 → 인용, `[](../.md)` 사용, `read`에 `-r`, 임시 파일은 `mktemp`.
- disable 필요 시 `# shellcheck disable=SC2086` 주석 추가(정당한 이유와 함께).
- 실행 팁: `shellcheck -x script.sh`로 소스 포함 추적, 여러 스크립트는 `shellcheck **/*.sh`(globstar 지원 환경) 또는 `find . -name '*.sh' -print0 | xargs -0 shellcheck`.

## 테스트 스켈레톤(bats 없이)
```bash
test_eq() { ["$1" == "$2"](../../"$1" == "$2".md) || { echo "FAIL: $1 != $2" >&2; return 1; }; }
run_tests() {
  output=$(echo foo | tr a-z A-Z)
  test_eq "$output" FOO
}
if [${RUN_TESTS:-0} -eq 1](../../${RUN_TESTS:-0} -eq 1.md); then run_tests; fi
```
- 외부 의존성은 `command -v`로 모킹 가능: `PATH="$PWD/fakes:$PATH"`
- 테스트는 독립 실행 가능하도록 입력/출력을 고정.

## 로그/에러 핸들링 스타일
- stderr는 에러/경고, stdout은 결과만. 파이프라인 연결성을 보장.
- 에러 메시지는 `script: context: message` 형식이 읽기 좋음.
- 종료 코드는 상수화: `EXIT_USAGE=2`, `EXIT_FAIL=1` 등.

## 포매팅 가이드(예시)
- 스크립트 상단: `set -Eeuo pipefail` + `IFS=$'\n\t'` 필요 시
- 함수명: 소문자+언더스코어, 전역 상수: 대문자
- 인덴트: 두 칸 또는 네 칸 일관. 파이프라인은 `\`로 이어쓰기
- 길어진 조건은 `if` 블록, `&& ||` 체이닝 최소화

## 5분 실습
1. `PS4='+$BASH_SOURCE:$LINENO: ' bash -x script.sh`로 디버그 로그 위치 확인
2. shellcheck로 기존 스크립트 검사 후 SC2086, SC2164 같은 경고 해결 연습
3. `set -e`가 켜진 상태에서 `cmd || true`와 `cmd || exit` 차이 확인
4. 임시 디렉터리를 `mktemp -d`로 만들고 trap으로 정리하는 패턴 작성

## 체크리스트
- [ ] 스크립트 시작부에 필요한 `set` 옵션과 이유를 주석으로 기록
- [ ] 디버그 시 `PS4`를 조정해 어느 파일/라인인지 보이도록 설정
- [ ] shellcheck 정적 분석을 통과하거나, 무시한 경고는 이유를 남김
- [ ] 테스트를 최소 1개라도 포함하거나, 실행 방법을 문서화
- [ ] 에러 메시지와 종료 코드 정책을 일관되게 유지

## 심화: 디버그 노이즈 관리
- `set -x` 로그를 파일로 분리: `( exec 19>trace.log; export BASH_XTRACEFD=19; set -x; main )`
- `PS4`에 시간/라인/함수명: `PS4='+[$EPOCHREALTIME][$BASH_SOURCE:$LINENO:${FUNCNAME[0]}] '`
- `set -T`(functrace)로 함수/서브셸까지 trap 전파 가능. 단, 과도한 트레이스는 성능 저하.
- `trap 'set +x' EXIT`로 디버깅 후 옵션 복원.

## 테스트 문화 구축
- **단위 테스트**: 순수 함수는 입력→출력 비교. 파일 I/O는 임시 디렉터리를 `mktemp -d`로 생성 후 테스트.
- **통합 테스트**: 주요 시나리오를 쉘 스크립트로 재현하고 기대 종료 코드/출력을 비교.
- **회귀 테스트**: 과거 버그를 재현하는 최소 입력을 케이스로 추가.
- **CI**: `shellcheck`, `bash -n`, `bats` 등을 CI에 연결. POSIX 모드 필요 시 `dash -n`도 병행.

## 스타일 가이드 예시(요약)
- **주석**: 목적/이유 중심으로, \"왜 이렇게 했는가\"를 작성. 명령 의미 자체 설명은 지양.
- **에러 처리**: 실패 가능성이 있는 명령 뒤엔 즉시 검사. `|| { log_err \"...\"; return 1; }` 패턴.
- **포맷**: 긴 파이프라인은 백슬래시로 줄바꿈하고, 각 단계 앞에 `#`로 목적을 짧게 기재 가능.
- **네이밍**: 전역 상수 대문자(`APP_ROOT`), 내부 변수 소문자(`tmp_dir`), 함수는 동사-명사(`load_config`).

## shellcheck 빈출 ID와 해법
- **SC2086** 단어 분리/글로브 → 인용 또는 배열 사용.
- **SC2046** `$(...)` 결과를 인용 없이 전달 → 인용 또는 `xargs`/배열 사용.
- **SC2164** `cd` 실패 체크 필요 → `cd -- \"$dir\" || exit`.
- **SC2002** `cat file | cmd` → `cmd < file` 권장.
- **SC1091** source 파일 경로 검증 → 존재 확인 후 source, 또는 `# shellcheck source=/path/to/file` 힌트.

## 연습 문제
1. `BASH_XTRACEFD`를 사용해 디버그 로그를 별도 파일로 남기는 스니펫을 작성하라.  
2. shellcheck SC2086 경고를 재현하고, 이를 수정하는 두 가지 방법을 제시하라.  
3. `set -x`를 켠 상태에서 민감 정보가 노출될 수 있는 예를 들고, 이를 방지하는 방법을 설명하라.  
4. `bats`가 없는 환경에서 간단한 테스트 러너를 작성하려면 어떤 구조로 만들면 좋은가?  
5. `bash -n script.sh`와 `shellcheck`의 차이를 설명하라.
