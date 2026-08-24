---
title: app-shortcuts
tags: ["android", "android/system-services"]
aliases: ["App Shortcuts 접근 계약"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## App Shortcuts 접근 계약

이 지도는 앱 아이콘을 길게 누르거나 시스템 검색을 통해 특정 화면/기능으로 즉시 진입하도록 지원하는 **App Shortcuts**(앱 단축 경로)를 소유권과 생명주기(lifecycle), 개수/호출 빈도 제약(rate limit) 두 가지 핵심 계약으로 나눈다. static, dynamic, pinned shortcut은 이름은 유사하지만 선언 위치, 갱신 주체, 삭제 가능 여부가 모두 다르며, 시스템 서비스인 **ShortcutManager**(dynamic/pinned shortcut의 등록·갱신·삭제 및 시스템 rate limit 제어를 총괄하는 시스템 서비스)는 이 셋을 하나의 카운트 상한과 rate limit 기준 아래 통합 관리한다.

### 읽는 순서

1. [static/dynamic/pinned shortcut은 소유권과 lifecycle이 다르다](shortcut-ownership-lifecycles.md)에서 세 종류가 각각 누구에 의해 만들어지고 누구만 지울 수 있는지 본다.
2. [ShortcutManager는 동적 shortcut 개수를 제한하고 백그라운드 갱신에 rate limit을 건다](shortcut-manager-rate-limits.md)에서 개수 상한과 rate limiting 조건, 디버깅 명령을 본다.

### 문제 분류

| 증상 또는 질문 | 먼저 확인할 경계 |
| --- | --- |
| 사용자가 홈 화면에 고정한 shortcut을 앱 코드로 지우려 해도 안 지워진다 | pinned shortcut은 앱이 disable만 할 수 있고 launcher에서 직접 제거할 수 없다는 소유권 계약 |
| 특정 조건에서만 동적 shortcut이 갱신되지 않는다 | 앱이 background 상태에서 rate limiting에 걸렸는지, `isRateLimitingActive()` 결과를 확인했는지 |
| shortcut을 여러 개 추가했는데 일부가 안 보인다 | `getMaxShortcutCountPerActivity()` 상한을 넘겼는지 |
| 개발 중 rate limit 때문에 테스트가 막힌다 | `adb shell cmd shortcut reset-throttling` 또는 개발자 옵션으로 초기화했는지 |

### 책임 경계

- 이 지도는 `ShortcutManager`/`ShortcutManagerCompat`을 통한 shortcut 선언·갱신·소유권 계약만 다룬다. 런처 UI가 shortcut을 어떻게 렌더링하는지의 세부는 런처 구현체마다 다르므로 다루지 않는다.
- **App Widget**(런처 홈 화면에 상주하며 실시간 정보나 컨트롤 UI를 지속적으로 제공하는 별도의 뷰 컴포넌트)은 별도 계약이며 이 지도가 다루지 않는다. shortcut은 "탭하면 앱의 특정 화면/동작으로 진입하는 진입점"이고, widget은 "홈 화면에서 지속적으로 콘텐츠를 보여주는 표면"이라는 점에서 목적이 다르다.
- shortcut이 실행할 Intent가 유효한 target(Activity)을 가리키는지에 대한 일반적인 Intent/Task 계약은 `00_foundations/learning-spine/04-manifest-to-component-execution.md`가 다룬다.

### 노트 목록

- [static/dynamic/pinned shortcut은 소유권과 lifecycle이 다르다](shortcut-ownership-lifecycles.md)
- [ShortcutManager는 동적 shortcut 개수를 제한하고 백그라운드 갱신에 rate limit을 건다](shortcut-manager-rate-limits.md)

검증일: 2026-08-04. [Shortcuts overview](https://developer.android.com/develop/ui/views/launch/shortcuts), [Manage shortcuts](https://developer.android.com/develop/ui/views/launch/shortcuts/managing-shortcuts)를 기준으로 확인했다.
