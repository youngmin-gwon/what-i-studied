# 04. 조건, 제어구조, 종료 코드 설계

## 시험 포인트
- `test`/`[ ]` vs `[[ ]]` 차이: 단어 분리/글로브/패턴 매칭
- 문자열 비교 `=`/`==`(패턴), `[[ ... =~ regex ]]` 정규식 사용법
- 산술 비교 `-eq -ne -lt -le -gt -ge`와 `(( ))` 표현식 차이
- `if/elif/else`, `case/esac` 패턴, `for/while/until` 루프 구문 암기
- `break`, `continue`, `select`, `shift` 등 루프 제어
- `exit`와 함수의 `return`(0-255), 종료 코드 설계 원칙

## 테스트 표현식 요약
- `test expr` 또는 `[ expr ]`: 공백 필수, `[`는 `]` 필요.
- 문자열: `-z` 빈 문자열, `-n` 비어있지 않음, `=` 동등, `!=` 다름, `<`/`>`는 사전순
- 파일: `-e` 존재, `-f` 일반파일, `-d` 디렉터리, `-x` 실행 가능, `-r/-w` 읽기/쓰기, `-s` 비어있지 않음, `-nt/-ot` 새로움 비교, `-ef` 동일 inode
- `[[ ... ]]`: 단어 분리/글로브 억제, `==` 패턴 매칭, `=~` 정규식(POSIX ERE). 좌변 인용 필요 없음.
- `(( expr ))`: 산술 평가, 0이 아닌 값이면 true, 변수를 `$` 없이 사용 가능.

## if/case 예시
```bash
if [[ -z ${1:-} ]]; then
  echo "usage: $0 file" >&2; exit 2
elif [[ ! -f $1 ]]; then
  echo "not a file: $1" >&2; exit 1
fi

case "$1" in
  start) do_start ;;
  stop)  do_stop  ;;
  restart|reload) do_restart ;;
  *) echo "unknown command" >&2; exit 1 ;;
esac
```

## 루프 패턴
- **for-in**: `for x in a b c; do ...; done`. 글로브 주의, 항상 인용.
- **C 스타일**: `for ((i=0; i<10; i++)); do ...; done`. 산술 평가.
- **while**: `while read -r line; do ...; done < file` → 파일 읽기 표준 패턴
- **until**: 조건이 거짓일 동안 반복. 잘 쓰지 않지만 시험 범위.
- **select**: PS3 프롬프트 사용 메뉴 루프. 입력값은 `$REPLY`.
- **break/continue**: `break 2`로 중첩 레벨 지정.

## 파일/라인 루프 주의
- `cat file | while read ...`는 하위 서브셸 → 루프 종료 후 변수 반영 안 됨.
- 추천: `while IFS= read -r line; do ...; done < file`
- `IFS= read -r line || [[ -n $line ]]` 패턴으로 마지막 줄 개행 없음 케이스 처리 가능.

## `set -e`와 제어 흐름
- `if cmd; then`에서 `cmd` 실패해도 `set -e` 무시(조건맥락). `cmd || exit $?` 패턴이 필요한 경우 있음.
- 파이프라인은 기본적으로 마지막 명령의 종료 코드 사용. `set -o pipefail`로 어느 단계 실패도 감지.
- `trap 'cleanup' EXIT`로 일괄 정리. `EXIT`는 함수 return과 exit 모두에서 호출.

## 함수와 종료 코드
- 함수 내 `return N`은 0-255. `return` 없는 경우 마지막 명령 종료 코드.
- 스크립트의 최종 종료 상태는 마지막 명령의 종료 코드 또는 `exit N`으로 명시.
- 관례: 0 성공, 1 일반 오류, 2 사용법 오류, 64~78(FreeBSD sysexits)도 자주 활용.

## 5분 실습
1. `[[ $var =~ ^[0-9]+$ ]]` 정규식 테스트 시 인용 유무에 따른 동작 확인
2. `for f in *.txt; do echo "$f"; done`에서 nullglob 설정 차이 관찰
3. `while IFS= read -r line; do echo "[$line]"; done < <(printf 'a\nb')`와 파이프 버전 비교
4. `set -e; false; echo alive` 결과와 `set -e; if false; then :; fi; echo alive` 비교

## 체크리스트
- [ ] test/`[[ ]]`/`(( ))` 중 상황에 맞는 표현식 선택
- [ ] 파일 테스트 연산자는 조합할 때 `[` `-a/-o` 대신 `[[ ... && ... ]]` 사용
- [ ] 루프 내 변수 활용이 필요하면 서브셸을 피하고 리디렉션 사용
- [ ] `set -e` 사용 시 예외 케이스(조건문, `|| true`, 파이프라인) 문서화
- [ ] 종료 코드 설계: 성공/실패/사용법/외부 에러를 구분해 상수 또는 enum처럼 관리

## 심화: 조건과 패턴 매칭
- `[[ $str == foo* ]]`는 glob 매칭, 대소문자 구분. `nocasematch` 옵션을 켜면 대소문자 무시.
- `[[ $str =~ ^foo(bar)?$ ]]` 사용 시, regex에 괄호가 있다면 `${BASH_REMATCH[1]}`로 캡처값 활용 가능. 인용하면 정규식이 리터럴이 되므로 주의.
- `case` 패턴에서 `|`로 여러 케이스 묶기, `*)` 기본 분기 필수. `;;&`(다음 패턴도 검사)와 `;&`(다음 패턴 실행) 등 Bash 확장 존재.
- `(( expr ))` 내부에서는 C 스타일 연산자 사용 가능(`++`, `--`, `<<`, `>>`, `&`, `|`, `^`). 조건식이 0이 아니면 true.

## 실무 루프 패턴
- **파일 목록 처리**: `while IFS= read -r -d '' f; do ...; done < <(find . -print0)` → NUL 안전.
- **재시도 로직**: `for ((i=1; i<=5; i++)); do cmd && break; sleep 1; done; [[ $i -le 5 ]] || exit 1`
- **타임아웃 루프**: `end=$((SECONDS+10)); while ((SECONDS<end)); do ...; done`
- **메뉴/프롬프트**: `select opt in start stop quit; do case $opt in quit) break;; start) ... ;; esac; done`

## 자주 틀리는 부분
- `[ -n $var ]`에서 var가 비어있으면 `[`가 인자 부족으로 오류. 항상 `[ -n "$var" ]`처럼 인용.
- `[ $a -eq $b ]`에서 비정수 입력이면 오류. 숫자 비교는 정수만 가능 → 문자열이면 `[[ $a == $b ]]`.
- `if cmd1 && cmd2; then`은 cmd1 실패 시 cmd2는 실행되지 않음. 순서 기반 의존성을 명확히 해야 함.
- `until cmd`는 cmd가 성공할 때 종료. 시험에서 부정형 의미를 물을 수 있음.

## 연습 문제
1. `[[ foo =~ ^f(o+) ]]` 실행 후 `${BASH_REMATCH[1]}` 값은 무엇인가? 인용 여부에 따라 어떻게 달라지는가?  
2. `case $1 in (start|stop) ;; (*) exit 1;; esac`에서 `;;&`와 `;&`의 차이를 설명하라.  
3. `for file in $(ls)`가 위험한 이유와, 대안 패턴을 작성하라.  
4. `while read line; do ...; done < file`에서 마지막 줄이 개행이 없을 때 누락되는 이유와 해결책을 적으라.  
5. `set -e` 상태에서 `cmd || true`와 `cmd || exit`의 효과를 비교하라.
