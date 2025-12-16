# Boot Flow & System Images #apple #boot #images

기기가 켜질 때부터 앱이 돌기까지 과정을 간단히 정리했다. 용어는 [[apple-glossary]].

## 부팅 순서(요약)
1) 부트 ROM: 하드웨어가 첫 코드(신뢰할 수 있는 루트)를 실행.
2) LLB/iBoot: 서명 검증, Secure Boot 체인. 올바른 OS 이미지를 고르고 검증한다.
3) 커널/램디스크 로드: [[apple-glossary#XNU|XNU]] 커널과 초기 파일 시스템을 올린다.
4) launchd: 모든 데몬/서비스의 부모. plist를 읽어 서비스 시작.
5) SpringBoard/WindowServer: UI를 띄우는 기본 서비스 실행.
6) 사용자가 잠금 해제 → 앱 실행.

## 이미지와 파티션
- APFS 컨테이너 안에 시스템/데이터 볼륨이 따로 있다. 시스템 볼륨은 read-only, 서명/봉인(sealing)되어 있다.
- macOS는 Signed System Volume(SSV)로 무결성을 확인한다.
- iOS는 ramdisk+시스템 이미지가 OTA로 교체된다.

## Secure Boot/무결성
- 모든 단계에서 이전 단계가 다음 단계의 서명을 확인한다.
- 커널/커널 확장도 서명되어야 하며, SIP/키보드 보안 등으로 무결성을 유지한다.

## 복구/DFU
- Recovery OS: macOS/iOS 복구 모드에서 시스템을 복원/재설치.
- DFU: 더 낮은 수준(장치 펌웨어 업데이트)에서 이미지를 다시 플래시.

## OTA 업데이트
- delta/full 패치를 내려받아 검증 후 적용. iOS는 보통 다음 부팅 때 적용된다.
- macOS는 시스템 볼륨을 스냅샷으로 만들어 빠르게 롤백할 수 있다.

## 진단 로그
- 부팅 문제는 panic log, baseband 로그(휴대폰), iBoot 로그에서 확인.
- sysdiagnose를 수집하면 부팅 후 상태도 함께 담긴다.

## 링크
[[apple-architecture-stack]], [[apple-build-and-distribution]], [[apple-sandbox-and-security]], [[apple-history-and-evolution]].
