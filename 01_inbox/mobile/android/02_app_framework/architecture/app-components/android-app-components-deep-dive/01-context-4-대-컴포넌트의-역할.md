---
title: 01-context-4-대-컴포넌트의-역할
tags: []
aliases: []
date modified: 2026-07-31 16:29:40 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## 💡 Context: 4 대 컴포넌트의 역할

상위 노트: [android-app-components-deep-dive](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive.md)

안드로이드 앱은 진입점이 하나가 아닙니다. 사용자의 요청, 시스템 이벤트, 프로세스 간 통신에 따라 다양한 방식으로 활성화됩니다. 각 컴포넌트의 특성을 정확히 파악하여 안전하고 효율적인 앱을 설계해야 합니다.

---

>[!CAUTION] **Devil's Advocate : 앱 컴포넌트에 대한 맹신 주의**
>과거 4 대 컴포넌트는 안드로이드 개발의 전부였지만, 현대의 순수 앱(App) 개발 환경에서는 위상이 크게 떨어졌습니다.
> - **Activity**: 화면마다 찍어내던 과거와 달리, 이제는 껍데기(Single Activity) 1 개만 존재합니다.
> - **Service // BroadcastReceiver**: 안드로이드 8.0 이후의 강력한 백그라운드 제약으로 인해 직접 구현할 일이 거의 사라졌으며, 대부분 **`WorkManager`**로 대체되었습니다.
