# 06. 표준 입출력, 리디렉션, 파이프

## 시험 포인트
- **표준 입출력 FD 번호**: stdin=0, stdout=1, stderr=2, `exec`로 재배치
- 리디렉션 기호: `>`, `>>`, `<`, `2>`, `&>`, `>|`(noclobber 무시), `<<<`(히어스트링)
- 히어독(`<<EOF`)과 인용된 히어독(`<<'EOF'`) 차이: 확장 여부
- 파이프라인 종료 코드: 기본 마지막 명령, `set -o pipefail`로 변경
- 프로세스 서브스티튜션 `<(cmd)` `>(cmd)` 동작과 제한(지원 셸, /dev/fd 필요)

## 표준 스트림 다루기
- `cmd >out.txt 2>err.txt` stdout/stderr 분리 저장
- `cmd >all.log 2>&1` 또는 `cmd &>all.log`(Bash)로 합치기. 순서 주의: `2>&1 >file`는 stderr만 터미널.
- `exec >file`로 스크립트 전체 stdout 재지정. 함수/블록에 한정하려면 서브셸 `( exec >file; ... )` 활용.

## 히어독/히어스트링
```
cat <<'EOH' >file.txt
literal $text with \n preserved
EOH

cat <<< "$var"   # 단일 문자열을 stdin으로 보내기
```
- 구분자 인용 시 변수/명령 치환/글로브 확장 없음. 인용 안 하면 확장됨.
- 히어독은 개행 포함 가능, 줄 끝 공백/탭을 주의(`<<-EOF`는 시작 탭 제거).

## 파이프라인과 pipefail
- 기본: `cmd1 | cmd2 | cmd3` 종료 코드는 cmd3의 것. 중간 실패를 잡으려면 `set -o pipefail`.
- `cmd1 | cmd2 || exit $?`는 pipefail 없이 중간 실패 잡기 어려움.
- `tee`를 이용해 출력 저장+전달: `cmd | tee out.log | downstream`

## 파일 디스크립터 재배치
- 별도 FD 사용: `exec 3<config.txt` 후 `read -r line <&3`
- FD 닫기: `exec 3>&-`
- stderr를 임시로 숨기기: `{ cmd 2>/dev/null; }`

## 프로세스 서브스티튜션
- `diff <(cmd1) <(cmd2)`로 두 명령 결과 비교
- `paste <(seq 3) <(printf 'a\nb\nc\n')`
- 일부 환경(엄격한 POSIX sh, busybox)에서 미지원. `/dev/fd`나 명명 파이프로 구현될 수 있음.

## NUL-종단과 안전한 파일 처리
- 공백/개행 포함 파일명을 안전하게 처리하려면 `-print0`+`xargs -0` 또는 `while IFS= read -r -d '' file; do ...; done`
- `find . -type f -print0 | while IFS= read -r -d '' f; do ...; done`

## 터미널/비터미널 구분
- `test -t 1`로 stdout이 터미널인지 체크. 터미널이면 색상/진행바, 아니면 순수 텍스트 출력 결정.

## 5분 실습
1. `cmd >out 2>&1` vs `cmd 2>&1 >out` 결과 비교
2. `set -o pipefail; false | true; echo $?`와 기본값 비교
3. 인용/비인용 히어독에서 변수/치환 동작 비교
4. `exec 3>log; echo hi >&3; exec 3>&-; cat log` 흐름으로 FD 사용 확인

## 체크리스트
- [ ] stdout/stderr 분리 또는 병합 여부를 명확히 지정
- [ ] pipefail 설정 여부와 필요성 검토
- [ ] 히어독에서 확장 여부를 의도대로 통제(`<<'EOF'` vs `<<EOF`)
- [ ] 파일명 안전 처리: NUL-종단 사용 여부 결정
- [ ] 프로세스 서브스티튜션 사용 시 지원 환경 확인

## 심화: 리디렉션 문법 세부
- `cmd 2>/tmp/err.log 1>&2` → stderr를 파일로, stdout을 stderr로. 순서에 따라 결과 달라짐.
- `cmd <<< \"text\"`는 한 줄 문자열을 stdin으로 주입하는 히어스트링. 좌변 공백 없이 사용.
- `exec 3<file` 후 `read -r line <&3` 형태로 FD를 재사용하면 여러 파일을 병렬로 읽을 때 유리.
- `:`(null command)를 이용해 리디렉션만 수행: `: >file`로 truncate.
- `>|`는 `noclobber` 옵션을 무시하고 덮어씀. 시험에서 `set -o noclobber`가 켜진 상태를 가정할 수 있음.

## 파이프라인 성능/에러 처리
- 긴 파이프라인에서 불필요한 `cat` 제거: `cmd < file | grep ...` 대신 `grep ... file | ...`.
- `set -o pipefail` 없이 중간 실패 로그를 잡으려면 `cmd1 | cmd2; status=${PIPESTATUS[*]}`(Bash 배열) 활용.
- `stdbuf -oL -eL cmd`로 버퍼링 조정하여 파이프를 통한 실시간 로그 처리 가능(GNU coreutils).
- `xargs -P`로 병렬 파이프라인 구성 시 각 명령의 종료 코드 수집을 위해 루프+wait 사용.

## 실전 사례
- **로그 모니터링**: `tail -F app.log | stdbuf -oL grep -E 'ERROR|WARN' | while read -r line; do ...; done`
- **두 리스트 비교**: `comm -3 <(sort a.txt) <(sort b.txt)` → process substitution을 이용한 정렬+비교.
- **스트림 수정**: `while IFS= read -r line; do printf '%s\\n' \"$line\"; done < <(cmd)`로 중간 가공.
- **다중 출력**: `cmd | tee >(grep ERROR >error.log) >(grep WARN >warn.log) >all.log` (Bash 확장)

## 연습 문제
1. `cmd 2>&1 >out.log`와 `cmd >out.log 2>&1`의 동작 차이를 설명하라.  
2. `PIPESTATUS` 배열의 용도와 예시를 제시하라.  
3. `<<-EOF` 히어독에서 탭과 공백의 동작 차이를 설명하라.  
4. `/bin/sh`에서 지원되지 않는 리디렉션/확장 기능을 세 가지 쓰고, 대안을 제시하라.  
5. `tee`를 이용해 stdout을 파일에 저장하면서 stderr만 화면에 남기려면 어떻게 해야 하는가?
