---
title: apk-vs-aab
tags: [aab, android, apk, app-bundle, deployment, packaging]
aliases: [APK vs AAB, APK 대 AAB, APK와 AAB 비교]
date modified: 2026-08-24 17:23:29 +09:00
date created: 2026-08-06 18:43:00 +09:00
---

## APK vs AAB (안드로이드 배포 규격 비교)

### 1. 개요 (Overview)

**APK (Android Application Package)** 와 **AAB (Android App Bundle)** 는 Android 앱을 빌드하고 배포하기 위한 두 가지 주요 패키징 규격이다.

레거시 무차별 포함 아티팩트인 APK 와 달리, AAB 는 Google Play 의 Dynamic Delivery 기술과 결합하여 기기 맞춤형 **Split APKs** 를 생성해 내는 현대 안드로이드 게시 표준이다.

### 2. 배포 및 전달 아키텍처의 차이

- **APK (모든 자원 통합 패키지 방식)**:
  - 기기의 화면 밀도, 언어, CPU ABI(arm64, x86 등)에 상관없이 모든 리소스와 네이티브 바이너리를 단일 파일에 모두 포함하여 배포하므로 다운로드 및 설치 용량이 비효율적으로 증가한다.
- **AAB (기기 맞춤형 Dynamic Delivery 조립 방식)**:
  - 개발자는 앱의 전체 구성 요소(AAB)를 Google Play 에 업로드하고, Google Play 가 사용자의 기기 사양(`arm64-v8a`, `xxhdpi`, `ko`)을 분석하여 꼭 필요한 조각들로 구성된 맞춤형 **Split APKs** 를 온디맨드로 생성하여 전달한다 (용량 15~30% 절감).

```mermaid
graph TD
    subgraph APKFlow ["레거시 APK 배포"]
        APKDev["빌드된 단일 APK (모든 ABI/Res 포함)"] -->|"직접 전송"| DevInst["기기에 거대한 통합 APK 그대로 설치"]
    end

    subgraph AABFlow ["현대 표준 AAB 배포"]
        AABDev["빌드된 AAB 업로드"] --> Play["Google Play Dynamic Delivery"]
        Play -->|"기기 사양 분석"| Split["기기 맞춤형 Split APK 조립 생성"]
        Split --> AppInst["기기에 꼭 필요한 최소 용량 조각만 설치"]
    end
```

---

### 3. APK vs AAB 핵심 비교표

| 비교 항목 | APK (Android Application Package) | AAB (Android App Bundle) |
| :--- | :--- | :--- |
| **주요 목적** | **기기 직접 설치 (`adb install`, 로컬 테스트)** | **Google Play 게시용 표준 아티팩트** |
| **파일 확장자** | `.apk` | `.aab` |
| **기기 맞춤 분할** | 불가 (모든 ABI/Resource 통째로 포함) | **가능 (Play 가 기기 맞춤 Split APK 생성)** |
| **앱용량 절감** | 용량 큼 (불필요 자원 상주) | **평균 15~30% 용량 절감** |
| **기기 직접 설치** | 가능 (스마트폰에서 즉시 실행) | 불가능 (APK 변환 도구 `bundletool` 필요) |
| **동적 기능 모듈** | 지원 안 함 | **On-Demand Dynamic Feature Module 지원** |

---

### 4. 연결 문서 (Related Links)

- [Play app signing은 업로드 키와 앱 서명 키를 분리한다](release/play-app-signing.md) - Play App Signing 필수 서명 계약
- [Play app signing은 업로드 키와 앱 서명 키를 분리한다](release/play-app-signing.md) - AAB 배포 계약 노드
- [APK (Android Application Package)](apk.md) - 직접 설치용 패키지 레퍼런스
