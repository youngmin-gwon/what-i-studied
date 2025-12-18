# 15. 실습 랩 워크스루

> 시험/면접 대비로 직접 따라 해볼 수 있는 랩 6개를 단계별로 서술했다. 각 랩은 "목표 → 준비물 → 단계 → 검증 → 확장 미션" 구조를 따른다.

## Lab 1. 인용/확장 완전 정복
- **목표**: 단어 분리, 글로브, 명령 치환, 파라미터 확장의 미묘한 차이를 체감한다.
- **준비**: `tmp/lab1` 디렉터리, 특수 문자 포함 파일명 생성: `touch "a b" 'c*d' file{1..3}.txt`.
- **단계**:
  1. `set -x`로 추적 켜기. `echo $*`와 `echo "$*"`, `printf '%s\n' "$@"` 차이 관찰.
  2. `foo="a b*c"; echo $foo; echo "$foo"; echo $foo*; set -f; echo $foo*` 실행 후 글로브/단어 분리 비교.
  3. `printf '%s\n' {1..3}`와 `printf '%s\n' '{1..3}'`의 차이 확인.
  4. `var=$(printf 'x\n'); echo "${var}y"`로 개행 제거 효과 확인.
- **검증**: 각 명령의 종료 코드와 출력이 기대한 대로인지 `set +x` 후 정리한다.
- **확장 미션**: `IFS=$'\n\t'`로 변경 후 `for x in $list; do ...; done`가 어떻게 달라지는지 기록.

## Lab 2. 안전한 파일 처리 루프
- **목표**: 공백/개행/비ASCII 파일명을 안전하게 순회하고 필터링한다.
- **준비**: `mkdir -p tmp/lab2 && cd tmp/lab2; printf 'a\0b c\0d\n' > list.bin` 등 임의 파일.
- **단계**:
  1. `find . -type f -print0 | while IFS= read -r -d '' f; do printf '%q\n' "$f"; done`
  2. `while IFS= read -r line; do ...; done < file` vs `cat file | while ...` 차이 재현.
  3. `mapfile -t arr < <(find . -type f -maxdepth 1)`으로 배열 채우고, `${#arr[@]}` 확인.
  4. `shopt -s nullglob dotglob` 설정 후 `for f in *.txt; do ...; done` 동작 비교.
- **검증**: 각 파일명이 손상 없이 출력되는지, 서브셸 유무에 따른 변수 값 변화를 체크.
- **확장 미션**: `find ... -exec`와 `xargs -0` 성능/가독성 비교를 표로 정리.

## Lab 3. 파이프라인 + 에러 처리
- **목표**: pipefail, PIPESTATUS, tee를 활용해 중간 실패를 탐지한다.
- **준비**: `printf 'ok\nfail\n' > data`; 실패하는 필터 `fail(){ grep impossible; }` 정의.
- **단계**:
  1. `set +o pipefail; cat data | fail | wc -l; echo $?` → 마지막 명령 성공 여부만 반영됨.
  2. `set -o pipefail; cat data | fail | wc -l; echo $?` → 중간 실패 감지.
  3. `cat data | fail | tee /tmp/out | wc -l; printf '%s\n' "${PIPESTATUS[@]}"`로 각 종료 코드 확인.
  4. stderr를 별도 파일에 저장: `{ cmd1 2>err.log; } | cmd2`. 순서 차이도 실험.
- **검증**: 예상한 종료 코드가 맞는지, `/tmp/out` 내용이 일치하는지 확인.
- **확장 미션**: GNU `stdbuf -oL`로 버퍼링 조정 시 로그 실시간성이 어떻게 변하는지 기록.

## Lab 4. 시그널/잡 제어
- **목표**: 백그라운드 잡, trap, timeout을 조합해 안정적으로 정리한다.
- **준비**: `sleep 100` 같은 장기 명령, `long(){ sleep 30; }` 함수.
- **단계**:
  1. `long & pid=$!; echo $pid; kill -0 $pid`로 실행 확인 후 `wait $pid`.
  2. `trap 'echo cleaning; kill $pid 2>/dev/null; rm -f /tmp/lab4' EXIT INT TERM` 등록 후 Ctrl+C로 종료 반응 확인.
  3. `timeout 2s long; echo $?`로 종료 코드 124 확인(없는 환경에서 perl 대안 작성).
  4. `pids=(); for i in {1..3}; do sleep 5 & pids+=($!); done; for p in "${pids[@]}"; do wait $p; done` 동시 실행.
- **검증**: 인터럽트 후에도 임시 파일이 삭제되고, 고아 프로세스가 남지 않는지 `ps`/`pgrep`로 확인.
- **확장 미션**: `set -m`으로 잡 제어 켜고 `bg/fg` 테스트. 스크립트에서 켤 때의 부작용 기록.

## Lab 5. 인자 파싱과 설정 로딩
- **목표**: `getopts`와 `.env` 로딩 패턴을 숙달한다.
- **준비**: 샘플 `.env` 파일(`API_KEY=abc123`, `DEBUG=true` 등)과 옵션 요구 스크립트 뼈대.
- **단계**:
  1. `parse_args(){ local OPTIND opt; while getopts ':k:o:h' opt; do ...; done; shift $((OPTIND-1)); }` 작성.
  2. 필수 옵션 검사: `[ -n "$key" ] || { echo "-k required" >&2; exit 2; }`.
  3. `.env` 로딩: `set -a; source .env; set +a`; 존재 확인 후 권한(600) 점검.
  4. 인자 파싱 후 남은 인자 배열 `REMAIN=($@)` 저장, `for x in "${REMAIN[@]}"; do ...; done` 확인.
- **검증**: 잘못된 옵션/누락 시 종료 코드 2, 도움말 출력 정상 확인.
- **확장 미션**: GNU `getopt`와 POSIX `getopts` 비교, 긴 옵션을 추가해보며 호환성 기록.

## Lab 6. 디버깅/테스트 자동화
- **목표**: `set -x`, `PS4`, `shellcheck`, 간단 테스트 러너를 연습한다.
- **준비**: 오류가 있는 샘플 스크립트(`unquoted.sh` 등)와 bats 없는 테스트 함수.
- **단계**:
  1. `PS4='+${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]} ' bash -x unquoted.sh 2>trace.log` 실행 후 로그 분석.
  2. `shellcheck unquoted.sh` 결과를 보고 SC2086, SC2164 등을 수정.
  3. 간단 테스트 함수: `assert_eq(){ [$1 == $2](../../$1 == $2.md) || { echo "FAIL $1/$2" >&2; return 1; }; }` 작성 후 케이스 추가.
  4. `RUN_TESTS=1 bash script.sh` 패턴으로 테스트 실행 플래그 도입.
- **검증**: 수정 후 shellcheck 경고 0, 테스트 전부 통과.
- **확장 미션**: CI에서 실행될 수 있도록 `Makefile` 또는 `justfile`에 lint/test 타겟 추가.

## Lab 7. 텍스트 파이프라인 실전
- **목표**: `grep/sed/awk/coreutils` 조합으로 로그/CSV/설정 파일을 가공한다.
- **준비**: `access.log`(nginx), `data.csv`, `config.ini` 샘플 파일.
- **단계**:
  1. `grep -E ' 5[0-9]{2} ' access.log | awk '{count[$7]++} END{for(k in count) print count[k], k}' | sort -nr | head` → 5xx 상위 URL.
  2. `awk -F, 'NR==1{next} {sum[$3]+=$4} END{for(k in sum) printf "%s,%d\n", k, sum[k]}' data.csv` → 그룹별 합계.
  3. `sed -n '/^\[/,/^\[/{/^[^[]/p}' config.ini` → 특정 섹션 추출. 인플레이스 수정 예제도 추가.
  4. `cut -d' ' -f1 access.log | sort | uniq -c | sort -nr | head` → IP별 요청수.
- **검증**: 결과가 기대와 일치하는지 샘플 데이터에 대해 계산.
- **확장 미션**: `jq`를 사용해 JSON 로그도 동일하게 처리하고, jq 미설치 환경 대안 작성.

## Lab 8. 포터빌리티 체크 세트
- **목표**: GNU/BSD 차이를 실제로 비교해 기록한다.
- **준비**: macOS(또는 BSD)와 리눅스 환경 1개씩.
- **단계**:
  1. `date -d 'next monday'` vs `date -v +1monday` 결과 비교.
  2. `sed -i '' 's/a/b/' file`와 `sed -i 's/a/b/' file` 차이 관찰.
  3. `readlink -f` 부재 시 `python - <<'PY'` 대체 명령 실행.
  4. `/bin/sh -c 'echo $((1+2))'`가 두 환경에서 동일하게 동작하는지 확인.
- **검증**: 각 차이를 표로 작성(명령, GNU 결과, BSD 결과, 대안).
- **확장 미션**: BusyBox 셸에서 Bash 스크립트를 실행하며 호환되지 않는 부분을 체크.

## Lab 9. 성능/병렬화 미션
- **목표**: 외부 명령 호출을 최소화하고 병렬로 작업을 분산한다.
- **준비**: 1~5GB 대용량 텍스트 파일 하나, CPU 4코어 이상.
- **단계**:
  1. `time grep -c pattern bigfile` vs `LC_ALL=C time grep -c pattern bigfile` 성능 비교.
  2. `split -n l/4 bigfile chunk_`로 파일 분할 후 `xargs -P4 -n1 -I{} bash -c 'grep -c pattern "$1"' _ {}` 병렬 처리.
  3. 동일 작업을 `awk`/`python`으로 구현해 속도 비교.
  4. `mapfile`로 전부 읽는 경우와 스트리밍 처리의 메모리 차이를 `ps`로 관찰.
- **검증**: wall time/CPU 사용률 측정 결과 기록. 병렬 처리 후 합산값이 단일 실행 결과와 일치하는지 확인.
- **확장 미션**: `GNU parallel` 사용 가능 시 짧은 명령으로 대체해보고, busybox 환경에서 실패하는 옵션 찾기.

## Lab 10. 보안 점검 스크립트 만들기
- **목표**: 시스템 보안 설정을 점검하는 간단한 보고서를 생성한다.
- **준비**: `/etc/passwd`, `/etc/shadow` 접근 가능한 테스트 환경(루트 권한 필요할 수 있음).
- **단계**:
  1. `awk -F: '$3==0 {print $1}' /etc/passwd`로 UID 0 계정 나열.
  2. `find / -perm -4000 -type f 2>/dev/null`로 SUID 바이너리 목록 수집.
  3. `grep -E '^PasswordAuthentication' /etc/ssh/sshd_config` 등 설정 확인.
  4. 결과를 파일로 저장하고 `tar`로 묶어 전달. 민감 정보는 권한 600 유지.
- **검증**: 보고서 파일이 적절한 권한/소유권을 가지고 있는지 `ls -l`로 확인.
- **확장 미션**: 체크 항목을 함수로 분리해 모듈화, 옵션으로 특정 항목만 실행하도록 확장.

## 랩 수행 체크리스트
- [ ] 각 랩마다 `set -Eeuo pipefail` 적용, 필요한 곳에서만 `set +e` 사용
- [ ] 입력/출력/로그 경로는 절대경로 또는 `cd` 후 상대경로 사용
- [ ] 임시 파일/디렉터리는 `mktemp` 사용 후 trap으로 정리
- [ ] 외부 의존성은 시작 시 검사, 대안 명령을 주석 또는 문서로 제시
- [ ] 실행 환경 차이(GNU/BSD/BusyBox)를 표로 기록하고 대안 포함
- [ ] 성능 실험은 wall time과 CPU, 메모리 사용량을 함께 기록
- [ ] 실패한 실습도 로그/출력 그대로 보관해 재현 가능하게 유지
