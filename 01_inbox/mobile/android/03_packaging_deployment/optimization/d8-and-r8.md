---
title: d8-and-r8
tags: ["android", "bytecode", "d8", "desugaring", "dexing", "optimization", "proguard", "r8"]
aliases: ["D8 and R8", "D8 컴파일러", "D8과 R8", "Desugaring", "DEX 변환", "Dexing", "R8 최적화", "덱싱"]
date modified: 2026-08-24 17:47:21 +09:00
date created: 2026-08-24 14:25:00 +09:00
---

## D8 과 R8 컴파일러 및 덱싱(Dexing) 메커니즘

### 개요

Android 빌드 파이프라인에서 **덱싱(Dexing)** 이란 Java/Kotlin 컴파일러가 생성한 표준 JVM 바이트코드(`.class`)를 Android 런타임(ART/Dalvik)이 실행할 수 있는 레지스터 기반의 **`.dex` (Dalvik Executable) 바이너리 포맷**으로 변환하는 컴파일 과정이다.

Google 은 덱싱과 코드 최적화 성능을 극대화하기 위해 **D8(고속 DEX 컴파일러 및 디슈가링 엔진)** 과 **R8(코드 수축·최적화·난독화·덱싱을 단일 패스로 처리하는 통합 차세대 컴파일러)** 을 표준 도구로 제공한다.

```mermaid
flowchart TD
    JavaKt["Java / Kotlin 소스 (.java, .kt)"] --> Compilers["javac / kotlinc"]
    Compilers --> Bytecode["JVM 바이트코드 (.class)"]
    
    subgraph DebugFlow ["Debug 빌드 경로 (D8)"]
        Bytecode --> D8["D8 컴파일러<br/>(고속 덱싱 + Core Library Desugaring)"]
        D8 --> DebugDEX["디버그용 classes.dex"]
    end
    
    subgraph ReleaseFlow ["Release 빌드 경로 (R8: isMinifyEnabled = true)"]
        Bytecode & ProRules["ProGuard Rules<br/>(proguard-rules.pro)"] --> R8["R8 통합 최적화 엔진"]
        R8 --> TreeShaking["1. Tree Shaking (코드 수축)"]
        R8 --> Opt["2. Inlining & Class Merging (코드 최적화)"]
        R8 --> Obf["3. Obfuscation (식별자 난독화)"]
        R8 --> DexDirect["4. 직접 DEX 변환 (Dexing)"]
        TreeShaking & Opt & Obf & DexDirect --> ReleaseDEX["초소형·난독화된 classes.dex"]
        R8 --> Reports["4대 분석 리포트 (mapping.txt, usage.txt 등)"]
    end
```

---

### 1. 덱싱(Dexing)이란 무엇이며, 왜 필요한가?

>Android 기기는 JVM 바이트코드(`.class`)를 직접 실행하지 못하며, 모바일 하드웨어에 최적화된 `.dex` 포맷만을 실행할 수 있다.

| 비교 항목                   | JVM 표준 바이트코드 (`.class`)              | Android 런타임 바이너리 (`.dex`)                  |
| ----------------------- | ------------------------------------ | ------------------------------------------ |
| **실행 가상 머신**            | 표준 JVM (HotSpot 등)                   | **Android ART (Android Runtime)** / Dalvik |
| **가상 머신 구조**            | **스택 기반 (Stack-based)** (피연산자 스택 사용) | **레지스터 기반 (Register-based)** (가상 레지스터 사용)  |
| **상수 풀(Constant Pool)** | 각 `.class` 파일마다 독립된 상수 풀 소유 (극심한 중복) | **전체 앱의 모든 클래스가 단일 상수 풀을 공유 (중복 제거)**      |
| **파일 구조**               | 1 개 클래스 = 1 개 `.class` 파일 (수천 개 분산)  | **수천 개의 클래스가 단 하나의 `classes.dex` 로 압축 통합** |
| **메모리 및 I/O 효율**        | 데스크톱/서버용 (메모리 사용량 큼)                 | **모바일 최적화 (RAM 절약, 캐시 지역성 향상, 빠른 검증)**     |

---

### 2. 안드로이드 덱싱 컴파일러의 진화사 (`dx` ➔ `D8` ➔ `R8`)

```text
[과거 레거시: 4단계 분리 파이프라인]
.class ➔ [ProGuard: 코드 수축/난독화] ➔ .class ➔ [dx: 레거시 덱싱] ➔ .dex
  - 문제점: 각 단계마다 바이트코드를 읽고 쓰는 I/O 오버헤드, 느린 빌드 속도, 높은 메모리 소모.

[중간 과도기: D8 도입]
.class ➔ [ProGuard: 코드 수축/난독화] ➔ .class ➔ [D8: 차세대 고속 덱싱] ➔ .dex
  - 개선점: dx 대비 덱싱 속도 2배 이상 향상, 바이트코드 크기 축소.

[현대 표준: R8 단일 패스(Single-pass) 통합 파이프라인]
.class + ProGuard Rules ➔ [ R8: 수축 + 최적화 + 난독화 + 덱싱 통합 ] ➔ .dex
  - 혁신: 중간 .class 재생성 없이 메모리 상에서 직접 .dex를 출력하여 빌드 속도 극대화 및 최고 수준의 최적화 달성.
```

---

### 3. D8 과 R8 이름의 어원과 명명 규칙 (Why D8 and R8?)

Google 컴파일러 팀이 부여한 **"핵심 기능 머리글자(Prefix)" + "차세대 컴파일러 시리즈 식별자 `8`(Suffix)"** 의 결합 구조이다:

| 컴파일러 이름  | 머리글자 의미 (Prefix)                       | 숫자 `8` 의 의미 (Suffix)                                                         | 핵심 정체성                                |
| -------- | -------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------- |
| **`D8`** | **D**ex / **D**exer                    | 과거 1 세대 **`dx`** 를 대체하며, **Java 8** 언어 기능(람다, 스트림)의 Desugaring 을 지원하는 차세대 덱서 | **D**exing Engine (DEX 변환기)           |
| **`R8`** | **R**eduction / **R**eplacing ProGuard | D8 컴파일러 패밀리 제품군으로서의 세대 번호 일치 (`D8`에 `Reduction` 을 결합)                        | **R**eduction + Dexing (수축·난독화 통합 엔진) |

- **`D8`**: '`D`ex'를 만드는 도구로서, 과거 Dalvik 시절의 `dx` 명령어를 계승하면서 구글 V8 자바스크립트 엔진 개발팀(Google Aarhus)의 네이밍 전통을 따라 명명되었다.
- **`R8`**: 기존 ProGuard 가 수행하던 **코드 축소(Reduction / Shrinking)** 와 최적화를 D8 덱싱 파이프라인과 하나로 결합했음을 나타내기 위해 `R` + `8` 로 명명되었다.

---

### 4. D8 과 R8 의 공존 관계: 무엇이 사라지고 무엇이 남았는가?

>D8 이 사라지고 R8 만 남은 것이 아니다! D8 과 R8 은 단일 코드베이스 안에서 빌드 목적(Debug vs Release)에 따라 동작 모드를 달리하는 공존 관계이다.

| 구분                       | **D8 (Debug 빌드 기본)**                                   | **R8 (Release 빌드 기본)**         |
| ------------------------ | ------------------------------------------------------ | ------------------------------ |
| **활성화 조건**               | `isMinifyEnabled = false`                              | `isMinifyEnabled = true`       |
| **주요 목표**                | **개발자 생산성 극대화 (초고속 증분 빌드)**                            | **배포 크기 최소화 & 코드 보안 (난독화/수축)** |
| **코드 수축 (Tree Shaking)** | ❌ 미수행 (모든 클래스 보존)                                      | ⭕ **수행 (미사용 코드 완전 삭제)**        |
| **난독화 (Obfuscation)**    | ❌ 미수행 (디버깅 시 원본 이름 보존)                                 | ⭕ **수행 (`a`, `b` 등 식별자 축소)**   |
| **증분 덱싱 지원**             | ⭕ **지원 (수정된 클래스만 즉시 덱싱)**                              | ❌ 전체 앱 그래프 분석 필요로 증분 불가        |
| **실행되는 Gradle 태스크**      | `:app:dexBuilderDebug`<br/>`:app:mergeProjectDexDebug` | `:app:minifyReleaseWithR8`     |

#### 실제로 완전히 사라진 도구들 (Deprecated & Removed)

- ❌ **`dx` (레거시 덱서)**: AGP 3.1+ 에서 기본값이 D8 로 교체되었고, AGP 7.0 에서 빌드 도구체인에서 **완전히 제거**되었다.
- ❌ **`ProGuard` (레거시 난독화기)**: AGP 3.4+ 부터 기본 난독화 엔진이 R8 로 완전 교체되었다.

---

### 5. D8 컴파일러와 디슈가링(Desugaring) 메커니즘

#### 1) 디슈가링(Desugaring)이란?

>Syntactic Sugar(문법적 설탕)에서 Sugar(설탕)를 De-(제거하다/풀어헤치다)한다는 의미의 컴파일러 기법.

- **문법적 설탕(Syntactic Sugar)**: 개발자가 코드를 간결하고 읽기 쉽게 작성할 수 있도록 제공되는 최신 언어 문법 (람다식, 메서드 참조, 인터페이스 `default` 메서드, `try-with-resources`, 최신 `java.time` API 등).
- **구버전 Android 런타임의 한계**: 구버전 Android 기기(`minSdk < 26` 등)의 가상 머신(Dalvik/초기 ART)은 최신 JVM 바이트코드 명령어(`invokedynamic`)나 최신 Java 표준 라이브러리를 OS 프레임워크(`bootclasspath`)에 가지고 있지 않다.
- **D8/R8 의 역할**: 컴파일 시점에 이 **달콤한 문법(Sugar)을 걷어내고(De-sugar)**, 구버전 안드로이드 OS 도 안전하게 실행할 수 있는 투박하고 원시적인 하위 호환 구조(익명 클래스, 정적 헬퍼 메서드, `j$.*` 리라이팅)로 바이트코드를 재작성(Backporting)한다.

---

#### 2) 디슈가링의 2 대 계층 구조

```mermaid
flowchart TD
    Java8Code["최신 Java 8+ 문법 코드"] --> D8Desugar["D8 / R8 디슈가링 엔진"]
    
    subgraph Layer1 ["1. 언어 문법 디슈가링 (Language Desugaring)"]
        D8Desugar --> Lambda["람다식 / 메서드 참조"] -->|"invokedynamic 제거"| AnonClass["합성 익명 클래스 변환"]
        D8Desugar --> DefMethod["인터페이스 default 메서드"] -->|"인터페이스 바이트코드 분리"| HelperClass["동반 정적 헬퍼 클래스 합성<br/>(Interface$-CC.class)"]
        D8Desugar --> TryRes["try-with-resources"] -->|"addSuppressed 에뮬레이션"| SafeTry["하위 호환 예외 처리"]
    end
    
    subgraph Layer2 ["2. 코어 라이브러리 디슈가링 (Core Library Desugaring)"]
        D8Desugar --> JavaTime["java.time / java.util.stream API"]
        JavaTime -->|"패키지 호출 리라이팅"| JDollar["j$.time.* / j$.util.stream.* 로 변경"]
        JDollar --> DesugarJar["desugar_jdk_libs 백포트 구현체를 DEX에 번들링"]
    end
    
    AnonClass & HelperClass & SafeTry & DesugarJar --> FinalCompatDEX["구버전 OS(API 21+) 완벽 호환 DEX"]
```

1. **언어 문법 디슈가링 (Language Feature Desugaring - D8 기본 내장)**:
   - **람다식(Lambda)**: 구버전 VM 이 지원하지 않는 `invokedynamic` 호출을 D8 이 컴파일 타임에 `합성 익명 내부 클래스(Synthetic Anonymous Class)` 형태로 변환.
   - **인터페이스 `default`/`static` 메서드**: 인터페이스에 구현 코드가 들어간 Java 8 문법을, D8 이 `동반 정적 헬퍼 클래스(예: MyInterface$-CC.class)` 를 생성하여 정적 메서드 호출로 변환.
2. **코어 라이브러리 디슈가링 (Core Library Desugaring / API Desugaring)**:
   - Java 8+ 표준 라이브러리(`java.time.LocalDate`, `java.util.stream.Stream` 등)는 구버전 OS 에 아예 존재하지 않아 `NoClassDefFoundError` 크래시를 유발한다.
   - `coreLibraryDesugaring` 옵션 활성화 시, D8 이 소스 코드의 `java.time.*` 호출을 `j$.time.*` 네임스페이스로 자동 리라이팅(Rewriting)하고, Google 의 백포트 런타임 라이브러리(`desugar_jdk_libs`)를 앱의 `classes.dex` 에 함께 패키징한다.

#### `build.gradle.kts` 코어 라이브러리 디슈가링 설정 예시
```kotlin
// app/build.gradle.kts
android {
    compileOptions {
        // 코어 라이브러리 디슈가링 활성화
        isCoreLibraryDesugaringEnabled = true
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
}

dependencies {
    // 백포트 구현체 의존성 주입
    coreLibraryDesugaring("com.android.tools:desugar_jdk_libs:2.1.4")
}
```

---

### 6. R8 컴파일러: 4 대 통합 최적화 메커니즘

**R8**은 **Release 빌드(`isMinifyEnabled = true`)** 시 활성화되며, ProGuard 의 모든 기능을 대체하고 덱싱까지 한 번에 수행한다:

1. **Tree Shaking (코드 수축 / Code Shrinking)**:
   - 진입점(Entry Points: `AndroidManifest.xml` 에 등록된 Activity, Service 등)부터 정적 호출 그래프를 추적하여, 도달 불가능한(Unreachable) 미사용 클래스, 메서드, 필드를 완전히 제거한다.
2. **Code Optimization (바이트코드 최적화)**:
   - **Method Inlining**: 호출 비용을 줄이기 위해 짧은 메서드 본문을 호출 지점에 직접 인라이닝.
   - **Class Merging**: 인터페이스 구현체가 1 개뿐이거나 상속 계층이 불필요한 경우 두 클래스를 하나로 병합.
   - **Dead Code Elimination**: 절대 실행되지 않는 `if (false)` 블록 및 미사용 변수 할당 제거.
3. **Obfuscation (식별자 난독화)**:
   - 패키지, 클래스, 메서드, 필드 이름을 `a`, `b`, `c` 등 의미 없는 짧은 문자로 치환하여 APK 크기를 줄이고 역공학(Reverse Engineering)을 방지한다.
4. **Direct DEX Generation (직접 덱싱)**:
   - 최적화된 내부 AST(Abstract Syntax Tree)에서 중간 `.class`를 거치지 않고 직접 `classes.dex` 바이너리를 생성한다.

---

### 7. R8 빌드 산출물 4 대 리포트

R8 이 실행되면 `app/build/outputs/mapping/release/` 디렉터리에 다음 4 가지 핵심 분석 보고서가 생성된다:

| 파일명 | 내용 및 주요 용도 |
|---|---|
| **`mapping.txt`** | 원본 클래스/메서드명과 난독화된 이름 간의 매핑 테이블. (Play Console 에 업로드하여 크래시 난독화 스택 트레이스 복원 시 필수) |
| **`seeds.txt`** | ProGuard Keep 규칙(`-keep`)에 의해 제거되거나 난독화되지 않고 온전히 보존된 진입점 심볼 목록 |
| **`usage.txt`** | R8 의 Tree Shaking 에 의해 미사용으로 판정되어 **실제 APK 에서 완전히 삭제된 클래스 및 메서드 목록** |
| **`configuration.txt`** | AGP 기본 최적화 파일, 라이브러리 내장 AAR 룰, 앱 커스텀 `proguard-rules.pro` 가 모두 병합된 최종 실효 규칙 |

---

### 8. 관측 가능 증거 (Observable Evidence)

DEX 내부의 클래스 구조와 R8 의 최적화 결과는 터미널 명령어로 직접 검증할 수 있다:

```bash
# 1. R8에 의해 삭제된 미사용 메서드 목록 확인
head -n 30 build/outputs/mapping/release/usage.txt

# 2. 최종 DEX 파일 내부의 클래스 및 메서드 개수 관측 (apkanalyzer)
apkanalyzer dex packages build/outputs/apk/release/app-release.apk

# 3. Android SDK dexdump 도구로 DEX 바이트코드 디스어셈블
dexdump -d build/intermediates/dex/release/minifyReleaseWithR8/classes.dex | head -n 40
```

---

### 상위 및 연관 문서

- [Android 빌드 파이프라인과 핵심 빌드 용어 해설](../build/gradle/android-build-pipeline.md)
- [AGP 릴리스 빌드 점검 체크리스트](../build/gradle/agp-release-checklist.md)
- [바이트코드 파일(.class)과 아카이브 파일(.jar)의 본질](../../../../computer-science/jvm-bytecode-and-jar-archive.md)
- [APK vs AAB (안드로이드 배포 규격 비교)](../distribution/apk-vs-aab.md)
- [ProGuard의 본질과 R8과의 관계](proguard.md)
- [R8 Keep 규칙과 최적화 경계](r8-keep-rules.md)
- [R8 리소스 수축과 keep.xml 관리](r8-resource-shrinking.md)
