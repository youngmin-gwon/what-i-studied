---
title: dex2oat
tags: [android, system-internals, art, dex2oat, compiler, binary]
aliases: [dex2oat, dex2oat 컴파일러, dex2oat 데몬]
date modified: 2026-08-06 18:05:00 +09:00
date created: 2026-08-06 18:05:00 +09:00
---

# dex2oat (Android AOT 컴파일러 데몬)

## 1. 개요 (Overview)

**`dex2oat`** 는 Android [ART 런타임](art.md) 환경에서 [DEX 바이트코드](android-compilation-pipeline.md)를 읽어 타겟 CPU 아키텍처의 네이티브 기계어 바이너리 파일(`.oat`)로 번역해 주는 **안드로이드 전용 AOT 컴파일러 실행 파일 및 데몬 서비스**이다.

기기 부팅 시, 앱 설치 시, 또는 충전 중 유휴 백그라운드 환경에서 [Android Compilation Pipeline](android-compilation-pipeline.md) 의 명령을 받아 작동한다.

---

## 2. dex2oat 의 입출력 파일 구조

```mermaid
graph LR
    subgraph InputFiles ["입력 파일 (Inputs)"]
        DEX[".dex 바이트코드"]
        PROF[".prof 핫코드 프로파일"]
    end

    InputFiles --> dex2oatProc["dex2oat 컴파일 엔진"]

    subgraph OutputFiles ["출력 파일 (Outputs)"]
        OAT[".oat 네이티브 기계어 (ELF)"]
        VDEX[".vdex 검증 바이트코드"]
    end

    dex2oatProc --> OutputFiles
```

- **입력 파일**:
  - **`.dex`**: 앱 패키지(APK) 내 포함된 원본 안드로이드 압축 바이트코드.
  - **`.prof`**: 앱 사용 중 JIT 프로파일러가 수집한 핫코드(Hot Code) 메서드 목록.
- **출력 파일**:
  - **`.oat`**: CPU 아키텍처(ARM64 등)에 최적화된 ELF 포맷의 네이티브 기계어 파일.
  - **`.vdex`**: 런타임 검증(Verification)을 마쳐 빠른 재컴파일을 돕는 가공 바이트코드.

---

## 3. dex2oat 컴파일 필터 옵션 (Compile Filters)

`dex2oat` 는 시스템 상황이나 프로파일 유무에 따라 다양한 컴파일 필터(Compile Filter) 옵션으로 동작한다.

- **`verify`**: 컴파일 없이 바이트코드의 바인딩 및 타입 안전성만 검증한다.
- **`quicken`**: 최소한의 바이트코드 최적화만 적용한다.
- **`speed-profile` (기본값)**: `.prof` 프로파일 파일에 기록된 핫코드만 선별하여 AOT 컴파일한다. (저장공간 및 성능 최적화)
- **`speed`**: 프로파일 여부와 관계없이 애플리케이션의 모든 바이트코드를 100% 네이티브 기계어로 사전 컴파일한다.

---

## 4. 연결 문서 (Related Links)

- [Android Compilation Pipeline](android-compilation-pipeline.md) - dex2oat 가 트리거되는 3단계 안드로이드 컴파일 파이프라인
- [ART (Android Runtime)](art.md) - dex2oat 컴파일러를 내장하고 관리하는 백본 런타임
- [DEX (Dalvik Executable)](android-compilation-pipeline.md) - dex2oat 의 입력 대상이 되는 압축 바이트코드
- [AOT Compilation](../../../computer-science/aot-compilation.md) - dex2oat 가 기반하고 있는 CS 정적 컴파일 이론
