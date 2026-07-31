---
title: 04-appops-fine-grained-monitoring
tags: []
aliases: []
date modified: 2026-07-31 17:11:53 +09:00
date created: 2026-07-31 16:26:40 +09:00
---

## ⚙️ AppOps (Fine-grained Monitoring)

`AppOps` 는 권한보다 더 세분화된 실행 단위의 기록과 제어를 담당합니다.

- **상태바 인디케이터 (Privacy Indicators)**: 마이크나 카메라 사용 시 오렌지/그린 점으로 사용자에게 실시간 알림.
- **Privacy Dashboard (Android 12+)**: 사용자가 지난 24 시간 동안의 권한 사용 타임라인(언제, 어떤 앱이 위치/카메라 등을 썼는지)을 확인하고 제어할 수 있는 통합 대시보드.
- **자동 리셋**: 3 개월간 사용하지 않은 앱의 권한을 시스템이 자동으로 회수.

```bash
# 특정 앱의 AppOps 상태 조회
adb shell appops get com.example.app
```
