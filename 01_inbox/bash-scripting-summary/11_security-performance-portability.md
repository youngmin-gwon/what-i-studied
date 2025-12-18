# 11. 보안, 성능, 포터빌리티

## 시험 포인트
- `set -euo pipefail` 사용 시 함정과 보완책
- 입력 검증, 경로 정규화, 임시 파일/디렉터리 안전 작성(`mktemp`)
- `sudo`/권한 분리, umask, 파일 권한
- 포터빌리티: POSIX sh 호환 문법과 Bash 확장 구분, OS별 차이(sed -i, readlink vs greadlink)
- 성능: 서브프로세스 최소화, 파이프라인 대신 내장 사용, `mapfile`/`readarray` 활용

## 보안 기본
- **입력 검증**: 정규식으로 허용 목록(whitelist) 검사. 예: `[[ $user =~ ^[a-z_][a-z0-9_-]*$ ]] || exit 1`
- **임시 파일**: `mktemp` 사용. 예: `tmp=$(mktemp -d) || exit 1; trap 'rm -rf "$tmp"' EXIT`
- **경로 주의**: 상대경로 대신 절대경로 사용, `cd -- "$dir" || exit` 후 작업
- **권한**: `umask 077`로 민감 파일 권한 제한. 크리덴셜은 600/700 유지.
- **sudo**: 필요 최소 권한. `sudo -u user cmd`로 역할 분리.

## set -e 함정
- `if cmd; then` 조건에서 실패해도 종료되지 않음. `cmd || exit $?` 필요 시 명시.
- `command1 | command2`에서 앞 명령 실패를 감지하려면 `set -o pipefail`.
- 함수 내 `local var=$(cmd)`에서 cmd 실패하면 함수 전체 종료. `if ! var=$(cmd); then ...; fi` 패턴 사용.

## 포터빌리티 체크포인트
- `/bin/sh`가 dash인지 Bash인지 확인 불가 → POSIX 문법만 사용해야 함.
- Bash 확장: 배열, `[](../.md)`, `[=~](../../=~.md)`, `function`, `(( ))`, `echo -e` 동작 차이.
- `readlink -f`는 BSD/macOS 없음 → `perl -MCwd=realpath -e 'print realpath($ARGV[0])' file` 또는 `python - <<'PY'` 대체. macOS는 `greadlink`(coreutils) 설치.
- `sed -i` 백업 옵션 차이(BSD: `-i ''`). `date`의 `-d` vs `-v` 옵션 차이.
- `timeout` 명령 GNU만. POSIX 대체 스크립트 필요.

## 성능 팁
- 루프 내 외부 명령 호출 최소화. 문자열 조작은 파라미터 확장/내장 사용.
- `mapfile -t arr < file`로 전체 파일을 배열에 읽기(Bash). 큰 파일엔 주의.
- `printf`는 `echo`보다 예측 가능. `cat file | cmd` 대신 `cmd < file` 또는 `while read` 패턴.
- `xargs -P`/`GNU parallel`로 병렬화 가능 여부 확인.
- `LC_ALL=C`로 정렬/grep 속도 향상.

## 로깅/감사
- 에러는 stderr, 감사 로그는 별도 파일. 민감 데이터(비밀번호 등)는 로그에 남기지 않는다.
- 스크립트 시작 시 주요 환경 변수 기록: `log_info "USER=$USER PWD=$PWD PATH=$PATH"`(비밀은 제외).

## 5분 실습
1. `set -euo pipefail` 상태에서 `var=$(false)`와 `if var=$(false); then :; fi` 차이 확인
2. `mktemp -d`로 임시 디렉터리 만들고 trap으로 정리하는 스니펫 작성
3. macOS에서 `readlink -f` 대안 찾기(`perl -MCwd=realpath`)
4. `time seq 1 100000 | wc -l` vs `i=0; while ((i<100000)); do ((i++)); done` 비교

## 체크리스트
- [ ] 입력값을 허용 리스트로 검증, 에러 시 명확한 메시지와 종료 코드
- [ ] 임시 파일/디렉터리는 `mktemp` 사용, trap으로 정리
- [ ] POSIX 호환이 필요한지 명확히 하고, Bash 확장을 사용할 때 주석으로 의도 기록
- [ ] OS별 명령 옵션 차이를 문서화하고 대안을 함께 제공
- [ ] 성능 임계 구간에서 외부 프로세스 수, 데이터 크기, 로케일 설정 점검

## 심화: 보안 설계 체크포인트
- **권한 상승 최소화**: 스크립트 자체를 sudo로 실행하기보다, 필요한 부분만 `sudo cmd`로 감싸기.
- **입력 경로 정규화**: `realpath`(또는 대안)로 심볼릭 링크/상대경로 정리 후 처리. `cd -- "$dir"` 후 작업하면 간단.
- **명령 주입 방지**: 변수 값을 그대로 명령에 삽입하지 않기. 허용 목록으로 제한하거나, 배열에 옵션을 쌓아서 실행.
- **파일 잠금**: 동시 실행을 막으려면 `flock` 사용(플랫폼 의존). 대안으로 lock 파일 디렉터리를 `mkdir`로 만들고 성공 여부 확인.
- **환경 변수 공격**: `IFS`, `PATH`, `LD_PRELOAD` 등을 신뢰하지 말고 스크립트 시작 시 재설정.

## 포터빌리티 사례별 해법
- **날짜 계산**: GNU `date -d 'yesterday'` vs BSD `date -v -1d`. 휴대성 필요시 `perl -MPOSIX -e 'print strftime(\"%F\", localtime(time-86400))'`.
- **inotify vs kqueue**: 파일 감시는 OS별로 상이. 휴대성 확보하려면 폴링 또는 python 라이브러리 사용.
- **`readlink -f` 대체**: macOS `python - <<'PY'` 스니펫이나 `perl -MCwd=realpath`.
- **`sed -r` vs `-E`**: GNU는 `-r`, BSD는 `-E`. 두 옵션 모두 지원 여부를 감지하거나 `-E`를 우선 사용.

## 성능 튜닝 사례
- **대량 치환**: `tr`/`sed`/`awk` 중 목적에 맞는 최소 도구 사용. 단순 치환은 `tr`이 빠름.
- **배열 캐싱**: 반복적으로 작은 리스트를 재계산하지 말고 배열에 캐싱 후 재사용.
- **병렬화**: CPU 코어 수만큼 `xargs -P$(nproc)` 또는 `sysctl -n hw.ncpu`(BSD) 사용.
- **I/O 감소**: 한 번에 읽기 `mapfile`, 다중 출력을 `tee`로 조합. 필요 없는 로그는 `/dev/null`로.
- **셸 vs 다른 언어**: 복잡한 문자열/JSON 처리, 긴 루프는 `python`/`jq`로 위임하는 것이 오히려 성능+가독성↑.

## 짧은 예제: 안전한 임시 작업 + 오류 전파
```bash
#!/usr/bin/env bash
set -Eeuo pipefail
tmp=$(mktemp -d) || exit 1
cleanup(){ rm -rf "$tmp"; }
trap cleanup EXIT

process() {
  local src=${1:?file required}
  cp -- "$src" "$tmp/input"    # POSIX: cp "$src" "$tmp/input"
  sed 's/secret/****/g' "$tmp/input" >"$tmp/output" || return 1
  mv -- "$tmp/output" "${src%.log}.sanitized.log"
}
process "$@"
```
- 포인트: `mktemp`, trap 정리, `local` 입력 검증, 외부 명령 실패 시 즉시 반환. POSIX 필요 시 `local` 제거.

## 연습 문제
1. 사용자가 제공한 파일 경로를 처리할 때 심볼릭 링크 공격을 예방하는 패턴을 작성하라.  
2. `set -euo pipefail`이 켜진 상태에서 `var=$(cat missing)`를 실행하면 어떤 일이 발생하는지 설명하라.  
3. macOS에서 GNU coreutils가 없는 상태로 `readlink -f` 대신 사용할 수 있는 한 줄 명령을 작성하라.  
4. `flock`이 없는 환경에서 lock 파일을 구현하는 간단한 방법을 제시하라.  
5. `LC_ALL=C` 설정이 grep/sort 성능에 미치는 영향을 예시와 함께 설명하라.
