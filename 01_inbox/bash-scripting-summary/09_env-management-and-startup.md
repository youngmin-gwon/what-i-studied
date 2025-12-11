# 09. 환경 관리, 시작 스크립트, 스케줄러

## 시험 포인트
- 로그인/비로그인, 인터랙티브/비인터랙티브 로딩 순서(`.bash_profile`, `.bashrc`, `$BASH_ENV`)
- PATH, LD_LIBRARY_PATH 등 환경 변수 설계와 오염 방지
- alias, shell option 관리(`shopt`), 프롬프트 `PS1` 구성 요소
- cron, systemd timer, at 비교: 환경/로그/워크디렉터리 차이
- `.profile` vs `.bash_profile` vs `.bash_login` 우선순위

## 시작 파일 로딩 순서
- **로그인 셸**: `/etc/profile` → `~/.bash_profile`(없으면 `.bash_login`, `.profile` 순) → `~/.bashrc`를 보통 여기서 source
- **인터랙티브 비로그인**: `~/.bashrc`
- **비인터랙티브**: `$BASH_ENV`가 설정된 경우 해당 파일을 읽음. cron/systemd는 기본 비로그인·비인터랙티브
- macOS는 GUI 터미널이 로그인 셸을 여는 경우가 많아 `.bash_profile`이 실행됨.

## PATH 관리
- 선호: `PATH="/usr/local/bin:$PATH"`처럼 앞쪽에 추가. 중복 제거는 함수로 관리: `path_prepend()`
- 스크립트 내부에서 PATH 바꿀 때는 지역화: `( PATH=/opt/app/bin:$PATH; cmd )`
- `secure_path`(sudoers) 등으로 sudo 시 PATH가 달라질 수 있음.

## alias와 옵션
- alias는 비인터랙티브에서 기본 비활성. 스크립트에서 사용하지 않는 것이 안전.
- `shopt -s nullglob` 등 옵션은 스크립트 시작부에서 명시하고 주석으로 이유 기록.

## 프롬프트(PS1) 핵심
- `\u` 사용자, `\h` 호스트, `\w` 현재 디렉터리, 색상 코드는 `\[\e[31m\]\[\e[0m\]` 형태
- 루트/원격 세션 구분, git branch 표시 등은 시험보다 실무 팁.

## cron과 systemd timer
- cron 환경은 PATH 짧음(`/usr/bin:/bin`), 셸은 `/bin/sh`일 가능성 높음 → 풀 경로 사용
- 표준 출력/오류는 메일 또는 `/var/log/cron`에 기록. `MAILTO` 설정으로 수신.
- `@reboot`, `@hourly` 등 매크로, 분 시 일 월 요일 순서(0 또는 7=일요일).
- systemd timer는 서비스 유닛과 짝, `systemd-run --on-calendar='*-*-* 03:00:00' cmd` 등. 환경은 유닛 파일에서 설정.

## at/batch
- `at 03:00`으로 일회성 작업 예약. 입력 끝은 Ctrl+D. 환경/워크디렉터리/umask를 명시하는 습관.

## 환경 파일 버전 관리
- 개발 기기에서는 `~/.config/bash/` 등 별도 디렉터리로 관리 후 `.bashrc`에서 include
- 민감 정보는 별도 파일에 두고 권한 600 유지. `set -a`로 export 일괄 적용 가능하지만 주의.

## 5분 실습
1. `BASH_ENV=/tmp/env.sh bash -c 'echo from non-interactive'`로 비인터랙티브 로딩 확인
2. cron에서 `echo $PATH > /tmp/cron.path` 수행 후 PATH 차이 확인
3. `PATH=/tmp/bin:$PATH bash -lc 'echo $PATH'`로 로그인셸 PATH 확인

## 체크리스트
- [ ] 로그인/비로그인, 인터랙티브 여부에 따른 초기화 파일을 구분해 설정 배치
- [ ] PATH 추가 시 앞/뒤 위치와 중복 제거를 고려
- [ ] cron/systemd/at 실행 시 기본 셸과 환경을 명시적으로 설정
- [ ] alias에 의존하지 않고 함수 또는 스크립트로 구현
- [ ] 민감 정보/크리덴셜 파일 권한을 600으로 제한

## 심화: 환경 변수 관리 전략
- **중복 제거 함수**: `path_prepend(){ case :$PATH: in *:$1:*) ;; *) PATH=$1:$PATH ;; esac; }`
- **프로필 모듈화**: `~/.bashrc.d/*.sh`를 순서대로 source하는 패턴으로 설정 분할. `for f in ~/.bashrc.d/*.sh; do [ -r "$f" ] && . "$f"; done`
- **비밀 관리**: `.env` 파일 권한 600, `set -a; source .env; set +a`로 export 일괄 적용. 로그에는 값 출력 금지.
- **프록시/locale**: `HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`, `LANG`, `LC_ALL` 등 기본값 명시.

## 실행 환경별 주의
- **SSH 원격**: 기본이 로그인 셸. 단, `ssh host cmd`는 비인터랙티브 로그인 셸 → `.bashrc` 읽지 않음. 필요 시 `~/.ssh/config`의 `PermitUserRC` 등 확인.
- **sudo**: `sudo -E`로 환경 유지, 기본은 제한된 PATH/환경. `/etc/sudoers`의 `env_keep` 설정 확인.
- **컨테이너**: 베이스 이미지에 따라 `/bin/sh`가 dash/busybox일 수 있음. 엔트리포인트 스크립트에서 명시적 shebang 사용.

## cron/systemd 세부 비교
- **cron**: 기본 워크디렉터리 `/`, PATH 짧음, TZ는 시스템 설정 따름. `SHELL=/bin/bash`, `PATH=...`를 crontab 상단에 지정 가능.
- **systemd**: `WorkingDirectory=`, `Environment=`, `EnvironmentFile=`로 환경 설정. `StandardOutput=append:/var/log/app.log` 등으로 로그 관리.
- **at**: 실행 시점의 환경 대부분 복사하지만 umask/limit는 따를 수 있음. 스크립트 내부에서 필요한 값 재설정 권장.

## 연습 문제
1. `.bash_profile`에서 `.bashrc`를 호출하는 이유와, 순환 호출을 피하는 방법을 설명하라.  
2. cron에서 `python`을 찾지 못하는 상황을 재현하고, PATH를 수정하는 crontab 예시를 작성하라.  
3. sudo 실행 시 `$HOME`이 바뀌는 이유와, 이를 원래 사용자 홈으로 유지하는 옵션을 설명하라.  
4. 컨테이너 ENTRYPOINT 스크립트에서 `/bin/sh`가 dash인 경우 Bash 전용 문법이 실패하는 예를 들고, 대안을 적으라.  
5. `BASH_ENV`를 이용해 비인터랙티브 셸에 공통 환경을 주입하는 예시를 작성하라.
