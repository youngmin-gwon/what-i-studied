---
title: "학습 경로의 끝은 문서 소비가 아니라 프로젝트 결정이어야 한다"
tags: ["android", "android/foundations"]
---

# 학습 경로의 끝은 문서 소비가 아니라 프로젝트 결정이어야 한다

Android 학습 경로는 많은 글을 읽는 순서가 아니라 프로젝트에서 결정을 내릴 수 있게 만드는 순서여야 한다. 어떤 state owner를 쓸지, 어떤 storage를 쓸지, background work를 어떻게 보장할지, release artifact와 test gate를 어떻게 만들지 답할 수 있어야 한다.

그래서 foundations는 최종 목적지가 아니라 routing layer다. 세부 판단은 app architecture, Compose, data/storage, background work, security, testing/performance, packaging 정본에서 한다.

관련 노트: [app architecture](01_inbox/mobile/android/02_app_framework/architecture/android-app-architecture.md), [persistence](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md), [background work](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md), [performance](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/performance-contracts.md), [packaging/deployment](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md).

## 판단 기준

Foundation 노트는 세부 구현을 반복하지 않고 Android 지식이 어느 계층의 문제인지 찾아가는 입구로 사용한다.

## 경계

학습 순서나 역사 설명은 API 목록을 외우는 방향이 아니라 runtime, framework, service, security, tooling boundary를 구분하는 방향으로 유지한다.
