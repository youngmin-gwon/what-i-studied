---
title: "백그라운드 실행 수단은 실패 비용으로 결정한다"
tags: ["android", "android/system-services"]
---

# 백그라운드 실행 수단은 실패 비용으로 결정한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [백그라운드 작업 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)

## 한 문장 결정표

| 질문 | 우선 검토할 수단 |
| --- | --- |
| 화면이 살아 있는 동안 끝나는 짧은 작업인가? | 코루틴과 화면 생명주기 |
| 지연되어도 되지만 결국 수행되어야 하는가? | WorkManager |
| 사용자가 진행 중임을 계속 알아야 하는가? | foreground service |
| 특정 시각에 깨우는 것이 기능의 본질인가? | AlarmManager |

## 상세 판별

- 즉시성이 중요하지만 작업이 짧다면 현재 화면의 scope에서 실행하고 취소를 연결한다.
- 즉시성이 중요하고 작업이 길며 사용자가 상태를 봐야 한다면 foreground service를 검토한다.
- 완료 시점이 유연하고 네트워크나 충전 조건이 있다면 WorkManager에 제약을 부여한다.
- 시각 오차가 허용되지 않는 사용자 약속이면 AlarmManager와 exact alarm 요건을 확인한다.
- 알람이 트리거한 후의 동기화는 별도의 Worker로 위임할 수 있다.
- WorkManager가 시작한 사용자 가시 장시간 작업은 foreground worker를 검토할 수 있다.

## 설계 질문

- 앱 프로세스가 종료되어도 작업이 남아야 하는가?
- 기기 재부팅 후에도 예약이 유지되어야 하는가?
- 네트워크가 없을 때 재시도할 수 있는가?
- 중복 실행이나 순서 변경이 발생해도 결과가 올바른가?
- 사용자가 취소하거나 중단할 수 있는가?
- 시스템 및 Play 정책상 이 실행 수단의 사용 목적이 정당한가?

## 최소 테스트 세트

- 화면 종료, 프로세스 회수, 기기 재부팅 뒤 상태 복구를 확인한다.
- 네트워크 단절, 배터리 부족, Doze 상태에서 지연과 재시도를 확인한다.
- 권한 거부와 target SDK 변경 시 시작 실패를 확인한다.
- 동일 작업을 여러 번 예약했을 때 중복 결과가 생기지 않는지 확인한다.
- 알림에서 사용자가 작업을 중지할 수 있는지 확인한다.

## 결정 기록

- 선택한 API와 함께 제외한 대안, 허용 지연, 재시도 정책을 기록한다.
- 기능 요구가 바뀌면 실행 수단도 다시 평가하고 기존 예약을 마이그레이션한다.
- 정확한 시각과 높은 배터리 효율이 동시에 필요한 경우 우선순위를 제품 요구로 확정한다.
- 백그라운드 실행이 실패해도 사용자가 데이터를 잃지 않도록 로컬 상태를 먼저 저장한다.
- 네트워크 서버가 중복 요청을 안전하게 처리하는지 클라이언트 재시도 전에 확인한다.
- 알림이 필요한 작업은 알림 채널, 권한 거부, 중지 액션까지 기능 범위에 포함한다.
- 최종 검증은 최신 Android 버전뿐 아니라 지원 최소 버전과 대표 제조사 환경에서 수행한다.

## 공식 문서

- [백그라운드 작업 선택 가이드](https://developer.android.com/develop/background-work/background-tasks)
- [서비스 개요](https://developer.android.com/develop/background-work/services)
