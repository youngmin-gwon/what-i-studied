---
title: android-zygote-and-runtime
tags: [android, android/runtime, android/zygote]
aliases: []
date modified: 2025-12-16 16:03:39 +09:00
date created: 2025-12-16 15:23:47 +09:00
---

## Zygote & Android Runtime android android/runtime android/zygote

앱을 빠르게 만들고 실행하는 두 주인공이 [[android-glossary#zygote|Zygote]] 와 [[android-glossary#art|ART]] 다.

### Zygote: 앱 공장
- 부팅 때 미리 클래스/리소스를 [[android-glossary#zygote#preload|Preload]] 하고 대기한다.
- 새 앱이 필요하면 Zygote 가 자기 자신을 [[android-glossary#zygote#fork|fork]] 해 복사본을 만든다.
- 복사본은 ActivityThread.main 을 실행하며 앱의 메인 스레드를 연다.

### 프로세스 시작 흐름
1. ActivityManager 가 "이 앱 프로세스가 없다"고 판단한다.
2. Zygote 소켓으로 UID/세팅을 보내 포크를 요청한다.
3. 새 프로세스가 생기면 [[android-glossary#art|ART]]/Binder/Looper 를 준비하고 Application 을 띄운다.

### ART: 실행 엔진
- DEX 를 실행한다. 자주 쓰는 코드는 미리 (AOT) 또는 실행 중 (JIT) 빠르게 바꾼다.
- GC 로 메모리를 치우되 멈춤을 최소화하려 한다.
- 프로필 (자주 쓰인 코드 목록) 로 무엇을 먼저 빠르게 만들지 정한다.

### 성능을 위한 장치
- Baseline Profile/Cloud Profile 로 처음 실행도 빠르게 한다.
- Boot image/App image 를 공유해 메모리 낭비를 줄인다.

### 안전 장치
- [[android-glossary#selinux|SELinux]] 와 seccomp 필터가 위험한 시스템 호출을 제한한다.
- [[android-glossary#uid|Isolated UID]] 프로세스는 권한이 거의 없는 특별한 모드다.

### 더 보기

[[android-performance-and-debug]]: 시작 속도·GC 확인 방법.

[[android-boot-flow]]: Zygote 가 언제 뜨는지.

[[android-evolution-history]]: Dalvik→ART 흐름.
