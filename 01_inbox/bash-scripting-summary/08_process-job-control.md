# 08. 프로세스, 잡 제어, 시그널

## 시험 포인트
- 포그라운드/백그라운드 실행 `cmd &`, 잡 목록 `jobs`, 제어 `fg`/`bg`
- 시그널 기본: SIGINT(2), SIGTERM(15), SIGHUP(1), SIGKILL(9), SIGCHLD(17/18/20)
- `trap` 구문과 종료 시 정리: `trap 'cleanup' EXIT`, 특정 시그널 핸들링
- 타임아웃 실행: `timeout 5s cmd`(GNU coreutils) 또는 `perl/sleep &` 대체
- 서브셸/백그라운드에서의 변수 가시성, `wait`로 동기화

## 잡 제어 기본
- 인터랙티브 셸에서 Ctrl+Z로 일시정지(SIGTSTP), `bg`로 백그라운드 재개, `fg`로 포그라운드 복귀.
- 스크립트에서는 잡 제어가 기본 비활성화(`set +m`). 백그라운드 잡을 직접 관리해야 함.
- `jobs -l` PID 포함 목록, `%1` 등 잡 사양으로 참조.

## 백그라운드 실행과 wait
```bash
long_task &
pid=$!
# ... 다른 일 수행 ...
if wait $pid; then echo ok; else echo fail; fi
```
- `$!`는 최근 백그라운드 잡 PID. 여러 개면 배열 사용: `pids=(); cmd1 & pids+=($!); cmd2 & pids+=($!)`
- `wait`는 지정 PID 종료 코드 반환. 인자 없으면 모든 백그라운드 잡을 기다림.

## 시그널과 trap
- 구문: `trap 'handler' SIGINT SIGTERM EXIT`
- `trap - SIGINT`로 기본 동작 복원, `trap -p`로 현재 핸들러 확인
- `EXIT`는 스크립트 종료 시 항상 실행(심지어 `set -e`로 실패해도). `ERR`는 오류 발생 시(Bash 확장).
- 핸들러 내부에서 `set +e` 고려: 실패 시 무한 루프/즉시 종료 방지.

## 정리/정돈 패턴
```bash
cleanup() {
  rm -rf "$TMPDIR"
}
trap 'cleanup' EXIT
trap 'echo interrupted >&2; exit 130' INT
```
- 임시 파일/디렉터리 정리, 잠금파일 제거, 백그라운드 잡 종료 등에서 사용.
- `trap`은 자식 프로세스에는 자동 전파되지 않으므로, 자식에게는 별도 설정 필요.

## 타임아웃과 제한
- `timeout 10s cmd`(GNU). 종료코드 124(타임아웃), 125(사용법), 126/127 실행 문제.
- 휴대용 방법: `perl -e 'alarm 5; exec @ARGV' cmd ...` 또는 `python - <<'PY'` 등.
- `ulimit -t` CPU 시간, `ulimit -v` 가상 메모리 제한. 시험에서 자주 언급.

## 데몬화/노후화된 nohup
- `nohup cmd >log 2>&1 &`로 SIGHUP 무시하며 실행. 현대 시스템에서는 systemd/tmux가 더 안전.
- `disown`으로 현재 셸의 잡 테이블에서 제거 가능.

## 프로세스 트리와 부모자식
- `$PPID` 부모 PID. `ps -o ppid= -p $$`로 확인 가능.
- 서브셸 `(...)`은 새 프로세스. `{ ...; }` 그룹은 현재 셸 그대로.

## 5분 실습
1. `sleep 5 & pid=$!; kill -0 $pid`로 실행 상태 확인 후 `wait $pid`
2. `trap 'echo bye' EXIT; ( trap 'echo child' EXIT; exit 0 ); echo done`으로 트랩 전파 확인
3. `timeout 1s sh -c 'sleep 2'` 종료 코드 확인
4. `set -m; sleep 100 &; jobs -l; fg %1; Ctrl+Z; bg %1` 잡 제어 흐름 실습

## 체크리스트
- [ ] 백그라운드 잡 PID를 저장하고 `wait`로 종료 코드 확인
- [ ] `trap`에서 정리 로직 구현, `EXIT`/`INT`/`TERM` 최소 처리
- [ ] 타임아웃/리소스 제한 필요 여부 검토(특히 외부 명령 호출 시)
- [ ] 서브셸 vs 현재 셸 그룹 사용을 구분해 부작용 관리
- [ ] nohup/systemd/cron 등 실행 환경에 따라 SIGHUP 처리 여부 고려

## 심화: 시그널 세부
- **동작**: 시그널은 프로세스/프로세스 그룹에 전달. 포그라운드 프로세스 그룹은 터미널의 Ctrl+C(CSIGINT), Ctrl+Z(SIGTSTP) 등 수신.
- **무시 불가**: SIGKILL(9), SIGSTOP(19)은 trap/무시 불가. 종료 정리는 EXIT trap에 의존해야 함.
- **SIGHUP**: 터미널 종료 시 전송. `nohup` 또는 `disown`으로 회피. systemd 서비스는 기본적으로 HUP 없이 종료/재시작.
- **SIGPIPE**: 파이프 수신자가 종료되면 송신자가 SIGPIPE로 죽을 수 있음. `set -o pipefail`과 함께 종료 코드 141(128+13) 확인.

## 병렬 실행 패턴
- **간단 병렬**: `pids=(); for f in *.log; do process \"$f\" & pids+=($!); done; for p in \"${pids[@]}\"; do wait $p || exit $?; done`
- **리소스 제한**: 병렬 4개만 실행: `sem=4; running=0; for task in ...; do ...; ((running++)); ((running==sem)) && { wait -n; ((running--)); }; done` (Bash 5 `wait -n`).
- **타임아웃+kill**: `timeout 10s cmd || { rc=$?; [[ $rc -eq 124 ]] && echo timeout; }`

## 실전 트랩 설계 사례
```bash
cleanup() {
  [[ -n ${pids[*]:-} ]] && kill "${pids[@]}" 2>/dev/null || true
  rm -rf "$TMPDIR"
}
trap cleanup EXIT
trap 'echo \"stopping\" >&2; exit 130' INT TERM
```
- kill 시 `2>/dev/null`로 이미 종료된 프로세스 에러 억제.
- EXIT trap은 함수/서브셸마다 별도. 필요 시 상위에서만 설정.

## 연습 문제
1. `wait -n`이 없는 Bash 4.x에서 가장 먼저 끝난 잡의 종료를 확인하려면 어떻게 해야 하는가?  
2. SIGPIPE가 발생하는 예를 들고, 이를 예방/처리하는 방법을 설명하라.  
3. `trap 'echo err' ERR`과 `set -E` 조합이 없는 경우 함수 내부 오류가 잡히지 않는 이유를 설명하라.  
4. `nohup cmd >/dev/null 2>&1 &`가 하는 일을 단계별로 설명하라.  
5. `pids=($(jobs -p))`로 모든 백그라운드 PID를 가져왔을 때, 그 사이에 종료될 수 있다는 점을 어떻게 보완할 수 있는가?
