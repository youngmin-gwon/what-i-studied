---
title: localization-contracts
tags: ["android", "android/app-framework"]
aliases: ["Android 지역화와 RTL 계약"]
date modified: 2026-08-04 18:00:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## Android 지역화와 RTL 계약

Android 지역화는 문자열을 여러 언어로 번역하는 작업 자체가 아니라, "지금 어떤 값을 보여줄지"를 로케일에 따라 자동으로 고르고 뒤집는 세 개의 서로 다른 계약으로 이뤄진다: 리소스 선택, 앱별 언어 override, 레이아웃 방향 미러링.

### 이 클러스터가 다루는 범위

- 리소스 qualifier(`values-ko`, `values-fr` 등)로 문자열이 런타임 로케일에 따라 선택되는 메커니즘과 폴백 순서
- Android 13+ 앱별 언어 설정이 시스템 로케일과 별개로 앱 언어를 바꾸는 계약
- RTL 미러링이 자동 적용되는 속성과 아이콘처럼 수동 대응이 필요한 예외

### 다루지 않는 범위

- 번역 워크플로우, 문자열 추출/번역 관리 도구(예: 서드파티 번역 플랫폼 연동).
- `plurals`, `ICU` MessageFormat 같은 복수형/포맷 규칙의 세부 문법.
- 날짜/통화/숫자 형식 지역화(`java.text`/`java.time` 포맷터 사용법).

### 정본 노트

- [리소스 Qualifier는 런타임 로케일에 따라 문자열을 선택한다](./resource-qualifiers-select-strings-by-runtime-locale.md)
- [Android 13+ 앱별 언어 설정으로 setApplicationLocales가 시스템 로케일과 별개로 앱 언어를 바꾼다](./per-app-language-with-setapplicationlocales-overrides-system-locale.md)
- [RTL 미러링은 start/end 속성에서는 자동이고 아이콘에서는 수동이다](./rtl-mirroring-is-automatic-for-start-end-but-manual-for-icons.md)

### 읽는 순서

1. 리소스 qualifier 노트로 문자열이 로케일에 따라 선택되는 기본 메커니즘을 이해한다.
2. 앱별 언어 노트로 "어떤 로케일 값을 기준으로 선택할지" 자체가 시스템 전체가 아니라 앱 단위로 바뀔 수 있다는 점을 확인한다.
3. RTL 미러링 노트로 문자열 선택과 별개로 레이아웃 방향이 어떻게, 어디까지 자동으로 뒤집히는지 확인한다.

관련 지도: [Android UI System](../android-ui-system.md), [Android UI System Contracts](../ui-system-contracts/ui-system-contracts.md)
