# Bash 스크립트 시험 대비 요약집 안내

## 구성 의도
- 단기간에 핵심 개념과 실전 패턴을 정리한 요약집입니다.
- 각 장은 **필수 개념 → 자주 틀리는 포인트 → 실습/예시 → 체크리스트** 흐름으로 배치했습니다.
- 총 분량은 약 10만 자 수준으로, 시험 직전 빠른 복습이 가능하도록 요약과 표로 정리했습니다.

## 읽기 순서 및 파일 목록
1. `01_overview-shell-basics.md` — Bash/쉘 개념, 인터렉티브 셸 vs 스크립트, 실행 흐름 이해
2. `02_commands-expansions.md` — 명령 구조, 인용/이스케이프, 글로브·대체·산술 확장
3. `03_variables-strings-arrays.md` — 변수 스코프, 파라미터 확장, 배열·연관배열 패턴
4. `04_control-flow-and-loops.md` — test/[](../.md) 문법, if/case, for/while, exit/status 설계
5. `05_functions-and-modularity.md` — 함수 선언/반환, 네임스페이스, 모듈화, 소스 관리
6. `06_io-redirection-pipelines.md` — 표준 입출력, 리디렉션, 파이프, 프로세스 서브스티튜션
7. `07_text-processing-toolkit.md` — grep/sed/awk/coreutils 조합, 인코딩/필터링 실전
8. `08_process-job-control.md` — 프로세스/잡 제어, 백그라운드, 시그널, 트랩, 시간 제한
9. `09_env-management-and-startup.md` — 로그인/비로그인 셸, 프로필 로딩, PATH, cron/systemd
10. `10_debugging-testing-style.md` — 디버깅 옵션, 셸체크, 단위 테스트, 스타일 가이드
11. `11_security-performance-portability.md` — 보안/권한, set -e 함정, 포터빌리티, 성능
12. `12_recipes-and-checklists.md` — 빈출 스니펫, 점검표, 모범 답안식 요약

## 활용 팁
- 각 장의 `시험 포인트` 목록을 먼저 읽고, 필요시 바로 예제로 점프하세요.
- `체크리스트`는 스크립트 작성 전/후에 빠르게 검증용으로 활용합니다.
- 실제로 이해했는지 확인하려면, 각 장의 `5분 실습` 문제를 터미널에서 풀어보세요.

## 추가
- 본 요약집은 Bash 4.x/5.x 기준이며, POSIX sh 호환성 포인트를 별도 표시합니다.
- `awk`, `sed`, `coreutils`는 GNU 기준으로 서술하되, 호환성 주의사항을 병기했습니다.

## 1주 학습 루트(예시)
1. **Day1**: 01~03 읽고 인용/확장/변수 실습 진행. shellcheck 설치.  
2. **Day2**: 04~06으로 조건/루프/리디렉션 집중. 파이프라인+pipefail 실험.  
3. **Day3**: 07~08에서 텍스트 도구와 시그널/잡 제어. 로그 파이프라인 만들기.  
4. **Day4**: 09~11로 환경/디버그/보안/포터빌리티 정리. cron/systemd 비교.  
5. **Day5**: 12~13 레시피/모의고사 풀기. 틀린 문제를 19장에 메모.  
6. **Day6**: 14~16 레퍼런스/트러블슈팅 읽고, 15장 랩 중 3개 실행.  
7. **Day7**: 17~20 옵션/케이스/회독/드릴로 종합 복습, shellcheck+테스트 스크립트 작성.

## 버전 및 의존성 메모
- Bash 4.0 이상: 연관배열, `${var,,}`/`${var^^}`, `mapfile/readarray`.  
- Bash 5.x: `wait -n`, globstar 성능 개선.  
- macOS: `/bin/sh`=`dash` 아님(bash 3.x), `sed -i ''`, `date -v`, `greadlink` 필요.  
- BusyBox: `timeout`/`stat` 옵션 다름, extglob 비활성 가능 → POSIX 모드 고려.

## 파일 구조 안내
- 본 디렉터리의 번호는 학습 순서를 나타냅니다(01~12 기본, 13~20 연습/참고).
- `14_command-reference.md`는 옵션/원라이너 사전, `15~18`은 실습/케이스/트러블슈팅을 담고 있습니다.
- 빠르게 훑을 때는 `19_quick-review-notes.md` → `20_command-drills.md` 순서로 보면 효율적입니다.
- POSIX 전용 정리는 `21_posix-compat-guide.md`에서 별도로 확인할 수 있습니다.
