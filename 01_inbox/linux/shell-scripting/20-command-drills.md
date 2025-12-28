---
title: 20. 커맨드 드릴 세트
tags: [linux, shell, drill, training, commands]
---

# 20. 커맨드 드릴 세트 (Drills)

손에 익을 때까지 반복 연습해야 할 핵심 명령어들의 동작을 빠르게 훈련합니다.

## 1. 기초 드릴 (Basic Drills)
| 목표 | 커맨드 (Command) |
| :--- | :--- |
| **숨김파일 포함 개수** | `shopt -s dotglob; echo * | wc -w` |
| **큰 파일 5개 찾기** | `du -ah . | sort -hr | head -n 5` |
| **사용자 입력 받기** | `read -rp "Name: " NAME; echo "Hello $NAME"` |
| **문자열 치환 테스트** | `path="/tmp/test.log"; echo "${path##*/}"` (파일명만 추출) |

## 2. 텍스트 가공 드릴 (Text Processing)
| 목표 | 커맨드 (Command) |
| :--- | :--- |
| **CSV 3열 합계** | `awk -F, '{sum+=$3} END{print sum}' data.csv` |
| **실패 로그 실시간 감시** | `tail -f app.log | grep --line-buffered "ERROR"` |
| **특정 단어 빈도 순위** | `cat file | tr ' ' '\n' | sort | uniq -c | sort -nr` |
| **NUL 안전 파일 처리** | `find . -type f -print0 | xargs -0 ls -l` |

## 3. 시스템 및 프로세스 드릴
| 목표 | 커맨드 (Command) |
| :--- | :--- |
| **포트 오픈 여부** | `nc -z -w 1 localhost 22 && echo "Open"` |
| **백그라운드 잡 종료** | `cmd & pid=$!; kill $pid` |
| **리소스 제한 확인** | `ulimit -a` |
| **특정 유저 프로세스** | `ps -u username -f` |

## 4. 안전 및 디버깅 드릴
| 목표 | 커맨드 (Command) |
| :--- | :--- |
| **xtrace 추적 실행** | `bash -x script.sh` |
| **파이프 실패 감지** | `set -o pipefail; false | true; echo $?` (결과 1 나와야 함) |
| **정적 분석** | `shellcheck script.sh` |
| **임시 공간 생성** | `tmp=$(mktemp -d); ls -d "$tmp"; rm -rf "$tmp"` |

---
## 🔗 연결 문서
- [[19-quick-review]] - 초압축 회독 노트
- [[21-posix-compat]] - POSIX sh 호환 가이드
