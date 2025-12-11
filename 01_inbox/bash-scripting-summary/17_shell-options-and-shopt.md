# 17. 셸 옵션/`shopt` 심층 정리

> `set`/`shopt` 옵션은 스크립트의 행동을 크게 바꾼다. 시험에서 옵션 설명/부작용/기본값을 묻는 문제가 자주 나오므로 한 곳에 정리한다.

## `set` 주요 옵션
- `-e` (`errexit`): 명령 실패 시 종료. 조건문/파이프라인/`!`/`||` 예외 존재. `trap ERR` 또는 명시적 `|| exit`로 보완.
- `-u` (`nounset`): unset 변수 사용 시 오류. `${var:-}` 패턴으로 방어. 배열/연관배열 키 체크에 주의.
- `-o pipefail`: 파이프라인 내 어느 단계라도 실패하면 전체 실패. `PIPESTATUS` 배열과 함께 사용.
- `-x` (`xtrace`): 실행되는 명령 추적. `PS4` 커스텀으로 라인/파일 표시. 민감 정보 노출 주의.
- `-E` (`errtrace`): 함수/서브셸에서도 ERR trap 전파.
- `-T` (`functrace`): DEBUG/RETURN/ERR trap을 함수/서브셸로 전파. 디버깅에 유용하지만 성능 영향.
- `-C` (`noclobber`): `>file` 덮어쓰기 방지. 덮어쓰려면 `>|file`.
- `-f` (`noglob`): 글로브 비활성화. 필요한 부분에서만 켰다가 끄기.
- `-b` (`notify`): 백그라운드 잡 종료 시 즉시 알림(인터랙티브용).
- `-m` (`monitor`): 잡 제어 켜기. 비인터랙티브 스크립트에서 예상치 못한 동작 유발 가능.
- `-o posix`: POSIX 호환 모드. `echo`/`export` 등 동작이 POSIX에 맞게 변경. Bash 확장 일부 비활성화.

### 옵션 세트 예시
```bash
set -Eeuo pipefail
IFS=$'\n\t'
shopt -s nullglob
trap 'echo "ERR at $BASH_SOURCE:$LINENO" >&2' ERR
```
- `IFS` 변경은 단어 분리 영향. 필요 없으면 기본값 유지.
- `set -e`와 `trap ERR` 조합 시, ERR trap에서 `set +e`를 잠시 켰다가 끄는 패턴이 안전할 수 있음.

## `shopt` 옵션
- `nullglob`: 글로브 매칭 실패 시 빈 리스트. 기본은 패턴 그대로 남음. 파일 없음 상태 루프에서 안전.
- `failglob`: 글로브 매칭 실패 시 오류. 실수 예방용. 스크립트 초기에 켜고 필요 시 끌 수 있음.
- `dotglob`: `*`에 점파일 포함. `.git` 등 포함 여부 조심.
- `globstar`: `**`가 재귀 디렉터리 매칭. `shopt -s globstar` 후 `**/*.sh` 사용 가능.
- `extglob`: `@(pat|pat2)`, `!(pat)` 등 확장 글로브 활성화. `shopt -u extglob`로 해제.
- `lastpipe`: 파이프라인 마지막 명령이 서브셸 대신 현재 셸에서 실행(비인터랙티브에서만). `while read` 결과를 부모 변수에 반영할 때 유용.
- `cmdhist`/`histappend`: 히스토리 관련. 시험보다는 실무 팁.
- `direxpand`: `echo ~user` 입력 시 즉시 확장(인터랙티브). 스크립트에는 영향 X.
- `checkwinsize`: 프롬프트 표시 후 터미널 크기 자동 갱신.

## 옵션 조합별 동작 요약
- **`set -e` + 파이프라인**: 기본은 마지막 명령 종료 코드 기준. `pipefail` 없으면 앞선 실패 무시. `set -o pipefail` 필수.
- **`set -e` + `if/while` 조건**: 조건문 맥락에서는 실패해도 종료 안 함. 조건 안에서 실패를 놓칠 수 있음.
- **`set -e` + `$(cmd)`**: 명령 치환 내부 실패는 즉시 종료(함수 전체). `if ! var=$(cmd); then ...; fi` 패턴으로 감싸기.
- **`set -u` + 배열/연관배열**: 존재하지 않는 키 접근 시 종료. `${arr[$key]:-}` 패턴 사용.
- **`lastpipe` 사용**: `shopt -s lastpipe; set +m` 필요. `printf 'a\nb' | while read -r line; do arr+=($line); done; declare -p arr` 결과가 부모에 반영.

## POSIX 모드에서 달라지는 점(발췌)
- `set -o posix` 또는 `/bin/sh` 실행 시 적용 가능. 주요 차이:
  - `echo`가 `-e`/`-n`을 옵션으로 인식하지 않을 수 있음. `printf` 사용 권장.
  - `local` 키워드, 배열, 연관배열, `[[ ]]`, `==` 패턴 매칭, `<<<` 히어스트링, 프로세스 서브스티튜션 `<( )` 미지원.
  - `source` 대신 `.` 사용. `function` 키워드 비권장.
  - `set -o pipefail` 지원 여부 환경에 따라 다름(dash 없음).

## 옵션 설정 관례
- **위치**: 스크립트 최상단(주석/셔뱅 바로 아래). 이유와 영향 주석으로 기록.
- **범위 한정**: 위험한 변경은 블록 안에서만 적용하고 복원. `set -e; { ...; }; set +e` 패턴 또는 서브셸 `( set -e; ... )` 사용.
- **팀 규칙**: 기본 옵션 세트(예: `set -Eeuo pipefail` + `shopt -s nullglob`)를 템플릿에 포함시키고, 예외 필요 시 주석 추가.

## 실전 Q&A
- **Q:** `set -u`가 켜진 상태에서 `for f in ${FILES[@]}; do` 실행 시 FILES가 unset이면?  
  **A:** 즉시 종료. `${FILES[@]+"${FILES[@]}"}` 패턴 또는 `FILES=()` 초기화 필요. 배열 존재 여부 확인은 `${#FILES[@]}` 대신 `${FILES+x}` 사용.
- **Q:** `set -e`에서 `cmd1 && cmd2 || cmd3`는 어떻게 평가되는가?  
  **A:** `cmd1` 성공 시 `cmd2` 실행, `cmd2` 실패하면 `cmd3` 실행(마지막 명령 실패로 간주되어 전체 종료될 수도). 확실한 분기에는 `if` 사용 권장.
- **Q:** `lastpipe` 사용 시 주의점은?  
  **A:** 비인터랙티브에서만 적용, `set +m` 필요. 파이프 마지막 명령이 현재 셸에서 실행되므로 변수 반영 가능하지만, 함수 내에서는 영향 제한.
- **Q:** `set -o posix`가 필요한 경우는?  
  **A:** 시스템 스크립트 호환성 테스트, `/bin/sh`로 실행될 코드를 Bash에서 시험할 때. Bash 확장이 무시될 수 있으므로 코드 차이를 검출.
- **Q:** `shopt -s extglob`을 켜면 어떤 패턴을 쓸 수 있는가?  
  **A:** `@(pat1|pat2)`, `?(pat)`, `*(pat)`, `+(pat)`, `!(pat)` 등. 예: `[[ $file == @(*.jpg|*.png) ]]`.

## 옵션 디폴트 값 요약
- `set -e`: 기본 off
- `set -u`: 기본 off
- `set -o pipefail`: 기본 off
- `shopt -s lastpipe`: 기본 off
- `nullglob/dotglob/failglob`: 기본 off
- `extglob`: 기본 off(Bash 4에서는 일부 on 가능), POSIX 모드에서는 off
- `nocaseglob`: 기본 off

## 실습 과제
1. `set -Eeuo pipefail` 켜진 상태와 껐을 때, 동일 스크립트가 어떻게 다르게 종료되는지 비교 보고서 작성.  
2. `shopt -s failglob` 후 존재하지 않는 패턴을 사용하는 스크립트를 작성하고, try/catch처럼 오류를 처리하는 함수를 만들어라.  
3. `lastpipe` 옵션을 켜고 끈 상태에서 `printf 'a\\nb' | while read -r line; do arr+=($line); done; declare -p arr`를 실행해 배열 내용 차이를 기록.  
4. `set -o posix`에서 배열/연관배열/`[[ ]]`를 사용해보고 나오는 오류 메시지를 캡처.  
5. `shopt -s globstar`와 `find`를 비교해 장단점을 표로 작성.  

## 옵션별 빠른 실습 가이드
- **pipefail**: `false | true` 실행 후 `$?` 확인. pipefail off면 0, on이면 1.
- **nounset**: `set -u; echo $UNSET` → 종료 코드 확인. `${UNSET:-ok}` 패턴으로 회피.
- **errexit**: `set -e; false; echo after` → 실행되지 않아야 함. `if false; then :; fi` 예외 확인.
- **extglob**: `shopt -s extglob; [[ abc == @(ab|abc) ]] && echo match` → off면 패턴 인식 실패.
- **nullglob/failglob**: 빈 디렉터리에서 `for f in *.zzz; do echo $f; done` → nullglob이면 출력 없음, failglob이면 오류.
- **globstar**: `shopt -s globstar; printf '%s\\n' **/*.sh`로 재귀 목록.
- **lastpipe**: `shopt -s lastpipe; set +m; printf 'a\\nb' | while read -r line; do out=$line; done; echo $out` → lastpipe off면 빈 출력.

## 실행 메모(실습 결과)
- `false | true` → pipefail off일 때 종료코드 0, `set -o pipefail` 후 1.
- `set -u; echo \"${UNSET:-ok}\"` → 기본값 패턴으로 종료 없이 `ok` 출력.
- macOS 기본 `/bin/bash`(3.x)에서는 `shopt -s lastpipe`가 `invalid shell option name` 오류(미지원). Bash 4+ 필요.
- `shopt -s failglob; for f in *.definitely_not_exist; do ...; done` → `bash: no match: ...` 메시지와 종료코드 1.

## 시험에 자주 나오는 옵션 설명 한 줄 정리
- `errexit`: 실패 시 종료하지만 조건문/파이프라인 예외가 있으니 pipefail·명시적 처리 필요.
- `nounset`: unset 변수 접근 시 종료, `${var:-}`로 기본값 주기.
- `pipefail`: 파이프 어느 단계 실패도 감지, 종료 코드 확인을 용이하게 함.
- `nullglob`: 글로브 미매칭 시 빈 리스트, for 루프 안전성↑.
- `failglob`: 글로브 미매칭 시 즉시 오류, 오타 방지용.
- `extglob`: 확장 글로브 패턴 활성화, POSIX 아님.
- `lastpipe`: 파이프 마지막 명령을 현재 셸에서 실행(비인터랙티브), 변수 반영 가능.
- `posix`: Bash를 POSIX 동작에 가깝게, 확장 일부 비활성화.

## 체크리스트
- [ ] 스크립트 템플릿에 기본 옵션 세트와 주석을 포함했는가?
- [ ] 위험 옵션(`set -e`, `set -u`, `pipefail`) 사용 시 예외 케이스를 코드/주석에 명시했는가?
- [ ] 글로브 동작(nullglob/failglob/dotglob/globstar/extglob)을 의도대로 설정했는가?
- [ ] POSIX 호환성 요구 여부를 결정하고 옵션/문법을 맞췄는가?
- [ ] 디버깅 시 `set -x`/`PS4`/`BASH_XTRACEFD` 등을 적절히 켜고 종료 후 복원하는가?

## 암기 카드 추가
- `PROMPT_COMMAND`: 프롬프트 표시 전 실행되는 명령. 로깅/타임스탬프에 활용. 스크립트에는 영향 거의 없음.
- `HISTCONTROL`: `ignorespace`, `ignoredups`, `ignoreboth` 등. 민감 명령은 선행 공백으로 히스토리 제외 가능.
- `COMP_WORDBREAKS`: 탭 완성 구분자. 시험보다는 실무 팁.
- `GLOBIGNORE`: 매칭에서 제외할 패턴. nullglob와 동시 사용 시 동작 주의.
- `SHELLOPTS`: 현재 셸 옵션을 콤마로 나열. 하위 셸에 전파.
- `set -o functrace`/`set -T`: 함수까지 trap 전파. 디버깅 전용.

## 마무리
옵션은 스크립트의 기본 행동을 바꾸므로 **의도와 이유를 항상 주석으로 남긴다**. 시험에서는 옵션 이름을 정확히 적고, 기본값(on/off)과 대표적인 부작용/예외를 한 줄로 설명하면 가산점을 받을 수 있다.
