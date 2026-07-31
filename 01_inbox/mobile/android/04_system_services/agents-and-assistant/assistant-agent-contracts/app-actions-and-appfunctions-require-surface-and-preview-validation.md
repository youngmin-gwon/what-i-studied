---
title: "App Actions와 AppFunctions 도입은 preview와 호출 표면을 검증해야 한다"
tags: ["android", "android/system-services"]
---

# App Actions와 AppFunctions 도입은 preview와 호출 표면을 검증해야 한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [Assistant와 에이전트 통합 계약](01_inbox/mobile/android/04_system_services/agents-and-assistant/assistant-agent-contracts/assistant-agent-contracts.md)

## 기능 분석

- [ ] 사용자의 목표를 읽기, 탐색, 생성, 변경, 공유로 분류했다.
- [ ] 기존 BII가 있는지 먼저 확인했다.
- [ ] BII에 맞지 않는 기능만 custom intent를 검토했다.
- [ ] 함수로 노출할 최소 작업 단위를 정의했다.
- [ ] UI가 필요한 작업과 UI 없이 가능한 작업을 구분했다.

## App Actions

- [ ] `shortcuts.xml`을 `res/xml`에 두었다.
- [ ] 각 `capability`에 fulfillment intent를 정의했다.
- [ ] BII parameter를 명시적 extra 또는 URL parameter에 정확히 매핑했다.
- [ ] 모호한 엔터티를 검색·선택 화면으로 보낼 수 있다.
- [ ] parameter가 없는 질의를 위한 fallback fulfillment를 검토했다.
- [ ] 지원 언어와 지역별 동작을 확인했다.
- [ ] Assistant test tool과 실제 기기에서 질의를 테스트했다.

## AppFunctions preview

- [ ] Android 16 이상 및 현재 compileSdk 요구사항을 확인했다.
- [ ] `androidx.appfunctions`와 KSP compiler 버전을 고정했다.
- [ ] preview API 변경 가능성을 릴리스 계획에 반영했다.
- [ ] KDoc, 함수명, parameter명, 결과 타입을 에이전트 관점에서 검토했다.
- [ ] 함수가 실행 가능한 상태인지와 실패 이유를 반환한다.
- [ ] 지원하지 않는 기기에서는 기능을 숨기거나 안전한 fallback을 제공한다.

## 보안과 운영

- [ ] 외부 입력을 도메인 경계에서 검증한다.
- [ ] 민감 작업은 사용자 확인·재인증·권한 확인을 거친다.
- [ ] 민감 데이터를 로그와 오류에 남기지 않는다.
- [ ] 중복 실행, 취소, timeout, 네트워크 실패를 테스트한다.
- [ ] exported component와 intent redirection을 보안 점검한다.
- [ ] 호출 성공뿐 아니라 잘못된 의도와 부분 실패도 관찰한다.

## 문서 갱신 규칙

App Actions와 AppFunctions의 API·권한·지원 범위는 플랫폼 및 preview 상태에 따라 변할 수 있다.
작성일과 공식 Android Developers 링크를 함께 기록하고, 릴리스 전에 현재 문서를 다시 확인한다.

공식 문서: [App Actions 시작하기](https://developer.android.com/develop/devices/assistant/get-started), [AppFunctions 추가](https://developer.android.com/ai/appfunctions/add-appfunctions), [보안 모범 사례](https://developer.android.com/privacy-and-security/security-best-practices)
