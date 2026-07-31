---
title: "Navigation 3 route key는 UI 클래스가 아니라 안정적인 직렬화 식별자다"
tags: [android, android/navigation, android/navigation3]
aliases: ["Navigation 3 route key는 UI 클래스가 아니라 안정적인 직렬화 식별자다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Navigation 3 route key는 UI 클래스가 아니라 안정적인 직렬화 식별자다

Navigation 3의 key는 특정 Composable class가 아니라 destination을 식별하는 navigation state다. key는 equality가 안정적이어야 하고, 필요한 argument만 포함해야 하며, 저장/복원과 deep link 변환을 견딜 수 있어야 한다.

화면 구현 객체, Repository, ViewModel, callback 같은 runtime object를 key에 넣으면 저장과 비교가 깨진다. route key는 domain identifier와 primitive/serializable argument 중심으로 설계한다.

## 판단 기준

- key는 process death 뒤에도 다시 만들 수 있는 값만 포함한다.
- 화면 표시용 객체나 callback은 entry content에서 주입한다.
- deep link parser가 URI를 typed key로 변환할 수 있어야 한다.
- versioning이 필요한 argument는 기본값과 migration/fallback을 함께 고려한다.

관련 노트: [Navigation 3 back stack은 저장 가능한 navigation state로 복원해야 한다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-back-stack-needs-saveable-restoration.md)

공식 문서: [Navigation 3 basics](https://developer.android.com/guide/navigation/navigation-3/basics)
