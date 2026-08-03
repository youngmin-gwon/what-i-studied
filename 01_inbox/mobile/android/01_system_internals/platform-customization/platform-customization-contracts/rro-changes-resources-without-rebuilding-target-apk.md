---
title: "RRO는 target APK를 다시 빌드하지 않고 resource를 바꾼다"
tags: [android, android/aosp, android/resources]
aliases: [RRO, Runtime Resource Overlay]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# RRO는 target APK를 다시 빌드하지 않고 resource를 바꾼다

상위 문서: [Platform customization contracts](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)

Runtime Resource Overlay(RRO)는 target package의 code를 수정하지 않고 resource 값을 바꾸는 customization 경계다. OEM theme, device-specific default value, form factor별 resource 차이를 platform image나 product image에서 제어할 때 사용된다.

RRO는 코드 patch보다 유지보수성이 좋지만, 아무 resource나 안전하게 바꿀 수 있다는 뜻은 아니다. overlayable 선언, target package, priority, partition 위치, enable state가 모두 결과에 영향을 준다.

## 실무 규칙

- 동작 로직을 바꾸려는 변경은 overlay로 숨기지 않는다.
- overlay 충돌은 priority와 partition 위치를 함께 본다.
- `cmd overlay`로 runtime state를 확인하고, build output만 보고 판단하지 않는다.
- 앱 개발자는 OEM overlay로 resource 값이 달라질 수 있음을 전제로 UI/설정을 방어적으로 설계한다.

근거: [Runtime resource overlays](https://source.android.com/docs/core/runtime/rros)
