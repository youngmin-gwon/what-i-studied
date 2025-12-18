# 03. 변수, 문자열, 배열/연관배열

## 시험 포인트
- **스코프**: 기본은 글로벌, `local`은 함수 내부, `export`는 자식 프로세스에만 전파
- **읽기전용**: `readonly var=value`, `declare -r`, 이미 set된 변수는 재할당 불가
- **배열**: 인덱스 배열(`declare -a`), 연관배열(`declare -A`), 전체 확장 시 인용 패턴
- **문자열 치환**: 파라미터 확장 패턴, 대소문자 변환 `${var^^}`, `${var,,}` (Bash 4)
- **특수 변수**: `$?`, `$0`, `$#`, `$*`, `$@`, `$-`, `$$`, `$!`, `$IFS`

## 변수 선언과 속성
- `name=value`로 선언. 공백 없음.
- `declare`/`typeset`로 속성 부여: `-i`(정수), `-l/-u`(소문자/대문자), `-a`(배열), `-A`(연관배열)
- 환경 변수는 `export VAR=value` 또는 `VAR=value` `export VAR`. 자식 프로세스에만 전달, 부모로는 안 올라감.

## 특수 변수 요약
- `$0`: 현재 스크립트 이름(경로 포함 가능). sourced일 때는 셸 이름.
- `$1..$9`, `${10}`: 위치 인자. 함수에서도 동일 개념.
- `$#`: 인자 개수. `$@`/`$*`: 모든 인자. `"$@"`는 각 인자를 별도 단어로 확장, `"$*"`는 IFS 첫 글자로 join.
- `$?`: 직전 명령 종료 상태. 파이프라인에서는 마지막 명령 기준.
- `$!`: 직전 백그라운드 잡 PID. `$$`: 현재 셸 PID.
- `$-`: 현재 셸 옵션 목록(`set -o` 관련). `$_`: 직전 명령의 마지막 인자(약간 다름). `$IFS`: 단어 분리 구분자.

## 문자열 다루기
- 부분 문자열: `${var:offset:length}`. 음수 offset은 끝 기준.
- 치환: `${var/pat/repl}`(첫), `${var//pat/repl}`(모두), `${var/#pat/repl}`(접두사), `${var/%pat/repl}`(접미사)
- 대소문자 변환: `${var^^}`, `${var,,}`, `${var^}`(첫 글자), `${var,}`(첫 글자 소문자)
- 길이: `${#var}`

## 인덱스 배열
```bash
declare -a nums=(10 20 "30 40")
nums[5]=50
printf '%s\n' "${nums[@]}"    # 각 요소 개별 확장
printf '%s\n' "${!nums[@]}"   # 사용 중인 인덱스 목록
unset 'nums[1]'                 # 특정 요소 삭제
```
- 미지정 인덱스는 마지막+1. sparce array 허용.
- `"${array[@]}"`와 `"${array[*]}"` 차이 기억. 전자는 요소별, 후자는 IFS join.

## 연관배열
```bash
declare -A cfg=( [env]=prod [region]=ap-northeast-2 )
cfg[debug]=true
for key in "${!cfg[@]}"; do
  printf '%s=%s\n' "$key" "${cfg[$key]}"
done
```
- Bash 4+ 기능. POSIX sh 미지원.
- 키/값에 공백 가능. 항상 인용.

## 위치 인자 재설정
- `set -- arg1 arg2`로 현재 위치 인자 재설정.
- `shift`로 첫 인자를 제거하며 앞으로 당김. `shift 2` 가능. 인자 부족 시 비정상 종료.

## 변수의 수명과 안전 설정
- `set -u`(`nounset`): unset 변수 참조 시 오류. `${var:-default}`로 안전하게 다룰 것.
- `set -o pipefail`: 파이프라인의 어느 한 명령 실패 시 전체 실패로 취급.
- `IFS` 조작 시 `local IFS=$'\n\t'`처럼 지역화. 스크립트 끝까지 영향을 끌고 가지 않도록 주의.

## 입력 받기: read
- `read var`는 한 줄 읽어 var에 저장(공백 분리). `IFS` 기준.
- 옵션: `-r`(백슬래시 무시), `-p` 프롬프트, `-s` silent(비밀번호), `-a` 배열로 받기, `-n` 글자수 제한, `-t` 타임아웃.
- 종료 상태: 입력 성공 0, EOF 1, 타임아웃 >128+SIGALRM(또는 1) 등 구현차.

## export와 서브셸
- `VAR=1 cmd`는 해당 명령 환경에만 VAR 적용. 다중 할당 가능 `VAR=1 OTHER=2 cmd`.
- `( VAR=1; other )` 서브셸 내부 변경은 부모에 영향 없음.
- `source file` 또는 `. file`은 현재 셸에서 실행 → 변수/함수/옵션 그대로 유지.

## 5분 실습
1. `set -- a "b c" d` 후 `$#`, `"$@"`, `$*` 결과 비교
2. `set -u` 켠 상태에서 `${x:-default}`와 `$x` 차이 관찰
3. 배열에서 `"${arr[@]}"` vs `"${arr[*]}"` 출력 차이 실험
4. `export VAR=foo; (VAR=bar; echo "$VAR"); echo "$VAR"` 결과 비교

## 체크리스트
- [ ] 스크립트 상단에 필요 옵션(`set -Eeuo pipefail` 등) 선언 여부 확인
- [ ] 위치 인자 사용 전 `$#` 검증, `${1:?usage}`로 필수 인자 체크
- [ ] 배열 확장 시 반드시 더블 쿼트, 인덱스/키는 `${array[index]}` 형태로 감싸기
- [ ] `IFS` 변경은 지역화 또는 사용 후 복원
- [ ] `readonly`/`export` 등 변수 속성을 명시적으로 선언

## 심화: 변수와 메모리 모델
- Bash 변수는 타입이 느슨하지만 속성을 줄 수 있다(`declare -i` 등). `-i`는 산술 평가 후 저장 → 문자열 손실 주의.
- 배열은 희소(sparse) 가능. 인덱스 최대값은 `${#array[@]}`가 아니라 `${!array[@]}`의 최대값을 확인해야 함.
- `printf -v var '%s' "$value"`로 서브프로세스 없이 변수에 포맷 적용 가능. 파이프/명령 치환보다 빠름.
- 문자열 결합은 단순 인접 배치(`prefix${var}suffix`). `+=`도 지원: `str+=" more"`, 배열에도 사용 가능.

## 실무 빈출 패턴
- **기본값 주입**: `: "${CONFIG_DIR:=${HOME}/.config/app}"`로 한 번만 설정 후 재사용.
- **불리언 처리**: `case ${DEBUG,,} in (1|true|yes|on) DEBUG=1 ;; (*) DEBUG=0 ;; esac` → 소문자 변환 후 패턴 매칭.
- **배열 필터링**: `filtered=(); for x in "${arr[@]}"; do [$x == pat*](../../$x == pat*.md) && filtered+=("$x"); done`.
- **연관배열 설정을 텍스트로**: `while IFS='=' read -r k v; do conf[$k]=$v; done < config.env` (공백/주석 처리 추가 필요).

## 자주 틀리는 부분
- `${array[0]}` 없이 `$array`만 쓰면 첫 요소가 아님: `"$array"`는 `${array[0]}`로 확장되지만 인용 없이 쓰면 단어 분리/글로브 위험.
- `local var=$(cmd)`는 `set -e` 상태에서 cmd 실패 시 함수 즉시 종료. `if ! var=$(cmd); then ...; fi`로 감싸기.
- `export arr=...`는 배열을 직접 export 불가. 필요 시 문자열로 join해서 전달.
- `read`로 배열 받기에서 `-a`는 기본 IFS 기준. 공백 포함 요소는 다른 구분자 또는 NUL 기반 처리 필요.

## 연습 문제
1. `set -- "a b" c` 후 `${#@}`와 `${#*}`의 차이를 설명하라.  
2. `declare -i n=08`을 실행하면 어떻게 되는지, 이유를 8진수 처리 관점에서 설명하라.  
3. 연관배열에 키가 없는 경우 `${map[key]:-default}`가 어떻게 동작하는지, set -u가 켜져 있을 때의 차이를 설명하라.  
4. `mapfile -t arr < <(printf 'a\nb\n')` 이후 `"${arr[*]}"`와 `"${arr[@]}"`의 차이를 보여주는 예를 작성하라.  
5. `${foo^^}`와 `${foo^}`의 차이를 예시와 함께 설명하라.
