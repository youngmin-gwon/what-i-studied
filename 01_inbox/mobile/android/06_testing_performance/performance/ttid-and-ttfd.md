---
title: ttid-and-ttfd
tags: ["android", "android/testing-performance", "performance", "launch", "ttid", "ttfd", "metrics"]
aliases: ["TTID", "TTFD", "Time To Initial Display", "Time To Fully Drawn", "앱 시작 성능 지표"]
date modified: 2026-08-24 18:10:00 +09:00
date created: 2026-08-06 18:25:00 +09:00
---

# TTID & TTFD (안드로이드 앱 시작 성능 2대 지표)

> [!NOTE]
> 이 문서는 [Android 시작 성능은 TTID와 TTFD로 나눈다](startup-performance-metrics.md)로 통합(Consolidated)되었습니다. 단일 정본(SSOT) 문서를 참조하십시오.

## 정본 문서 안내

Android 앱 시작 성능의 2대 핵심 지표인 **TTID (Time To Initial Display)** 와 **TTFD (Time To Fully Drawn)** 의 상세 메커니즘, Compose 및 View 코드 예시, Logcat/ADB 측정 명령, 비교 매트릭스는 아래 정본 노트에서 유지 관리됩니다.

👉 **정본 문서 바로가기**: [Android 시작 성능은 TTID와 TTFD로 나눈다](startup-performance-metrics.md)

---

### 핵심 요약 (Summary)

* **TTID (Time To Initial Display)**: 앱 아이콘 탭 후 첫 윈도우 프레임 표출 시점 (OS 자동 수집)
* **TTFD (Time To Fully Drawn)**: 비동기 데이터 로딩 완료 및 실제 상호작용 가능 시점 (`reportFullyDrawn()` / `ReportDrawnWhen` 호출)

### 관련 문서 (Related Links)

- [Android 시작 성능은 TTID와 TTFD로 나눈다](startup-performance-metrics.md) (SSOT)
- [Startup mode와 reportFullyDrawn이 시작 측정 기준을 정한다](../benchmark/startup-measurement-reportfullydrawn.md)
- [런타임 성능 계약](performance.md)
- [앱 실행 경로 계약](../../00_foundations/overview/foundation/app-launch-crosses-launcher-system-server-zygote-and-activitythread.md)

