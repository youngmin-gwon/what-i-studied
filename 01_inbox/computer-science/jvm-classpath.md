---
title: jvm-classpath
tags: ["build-system", "classloader", "classpath", "computer-science", "java", "jvm"]
aliases: ["AppClassLoader", "Classpath", "Jar Hell", "java.class.path", "JVM Classpath", "클래스패스", "파일시스템 경로 목록"]
date modified: 2026-08-21 18:54:08 +09:00
date created: 2026-08-19 14:40:00 +09:00
---

## JVM 클래스패스 (Classpath)와 탐색 메커니즘

### 개요

**클래스패스(Classpath)** 는 [JVM(Java Virtual Machine)](jvm-architecture.md) 및 Java/Kotlin 컴파일러가 특정 클래스를 필요로 할 때, 해당 클래스의 [바이트코드(.class)와 아카이브(.jar)](jvm-bytecode-and-jar-archive.md) 를 찾기 위해 탐색하는 **물리적 파일 시스템 경로들의 순서 있는 목록(Ordered List of File System Paths)** 이다.

C/C++ 과 같은 정적 링크 언어가 빌드 시점에 모든 라이브러리를 단일 바이너리로 묶는 것과 달리, JVM 은 **런타임에 [클래스로더(ClassLoader)](jvm-classloader.md) 가 클래스패스에 나열된 경로를 순차적으로 스캔하여 클래스를 동적으로 메모리에 적재(Dynamic Class Loading)** 한다.

```mermaid
flowchart TD
    Req["클래스 로드 요청<br/>(예: com.example.util.MathUtils)"] --> CL["ClassLoader (AppClassLoader)"]
    CL --> CP["Classpath 탐색 목록<br/>/build/classes : /libs/ktor.jar : /libs/common.jar"]
    
    subgraph PhysicalMap ["물리적 경로 매핑 해석"]
        CP -->|1. 디렉터리 경로| Dir["/build/classes/com/example/util/MathUtils.class (OS 파일 시스템 탐색)"]
        CP -->|2. JAR 아카이브 경로| Jar["/libs/ktor.jar 내부의 com/example/util/MathUtils.class (ZIP 중앙 디렉터리 색인)"]
    end

    Dir & Jar -->|첫 번째 매칭 발견| Load["바이트코드 읽기 ➔ Metaspace 메모리 적재"]
    Dir & Jar -->|전체 경로에 없음| Error["ClassNotFoundException / NoClassDefFoundError"]
```

---

### 1. 클래스패스의 본질: 파일인가, 개념인가?

>Classpath 는 물리적인 파일이 아니라, JVM 과 컴파일러에게 클래스 탐색 위치를 알려주는 '명령행 파라미터(-cp) 또는 환경변수 형식의 개념(Concept)'이다.

Eclipse 의 `.classpath`나 IntelliJ 의 `.idea/libraries` 처럼 파일명에 classpath 가 들어가는 경우가 있어 파일로 오해하기 쉬우나, 이는 IDE 가 프로젝트를 관리하기 위해 만든 자체 메타데이터 설정 파일일 뿐 JVM 스펙상의 Classpath 가 아니다.

#### 1) 운영체제의 `PATH` 환경변수와의 직접적인 비교

- **OS 의 `PATH`**: 터미널에서 `ls`나 `git` 을 입력했을 때, 운영체제가 실행 가능한 바이너리 파일이 디스크의 어느 폴더에 있는지 탐색하는 디렉터리 목록이다.
- **JVM 의 `CLASSPATH`**: 소스 코드에서 `import com.example.MyClass;` 를 만났을 때, JVM 이 해당 클래스의 바이트코드(`.class`)가 디스크의 어느 위치에 있는지 탐색하는 **Java 전용 경로 목록**이다.

```mermaid
flowchart LR
    subgraph OSPath ["운영체제 PATH 메커니즘"]
        Cmd["CLI 명령어 입력 (git)"] --> OS["OS Shell"]
        OS --> Scan1["PATH 탐색 (/usr/bin : /usr/local/bin)"]
        Scan1 --> Bin["실행 바이너리 실행 (/usr/bin/git)"]
    end

    subgraph JVMCP ["JVM CLASSPATH 메커니즘"]
        Code["코드 실행 (import com.example.Util)"] --> JVM["JVM ClassLoader"]
        JVM --> Scan2["CLASSPATH 탐색 (build/classes : libs/util.jar)"]
        Scan2 --> Bytecode["바이트코드 로드 (Metaspace)"]
    end
```

#### 2) 클래스패스에 추가될 수 있는 3 가지 물리적 실체

클래스패스 자체는 개념이지만, 가리키는 대상은 디스크에 존재하는 **물리적 위치**이다:

1. **디렉터리(Directories)**: 패키지 폴더 구조대로 풀려 있는 개별 `.class` 파일들의 루트 폴더 (예: `build/classes/java/main/`).
2. **JAR 파일(JAR Files)**: 수많은 `.class` 파일들을 ZIP 포맷으로 압축해 둔 아카이브 파일 (예: `libs/gson.jar`).
3. **ZIP 파일(ZIP Files)**: JAR 와 동일한 구조를 가진 압축 아카이브.

#### 3) 클래스패스 지정 방식과 OS 별 구분자

- **CLI 파라미터 (`-cp` 또는 `-classpath`)**: 특정 실행에만 적용되는 표준 권장 방식.
- **환경변수 (`CLASSPATH`)**: 머신 전체에 적용되는 전역 시스템 변수 (버전 충돌을 야기하므로 현대 개발에서는 지양).
- **OS 별 경로 구분자(Separator)**:
  - **Linux / macOS (POSIX)**: 콜론(`:`) ➔ `java -cp "build/classes:libs/app.jar" com.example.Main`
  - **Windows**: 세미콜론(`;`) ➔ `java -cp "build\classes;libs\app.jar" com.example.Main`

---

### 2. 클래스패스의 실제 물리적 구현체는 어디에 존재하는가?

"클래스패스 문자열을 파싱하고, 디스크를 스캔하여 클래스를 메모리에 올리는 실제 구현 코드"는 **JVM 내부의 C/C++ 네이티브 엔진과 Java 표준 라이브러리 클래스로더 계층**에 존재한다.

```mermaid
flowchart TD
    User["CLI 실행 (java -cp 'libs/a.jar:build/classes' Main)"]
    
    subgraph JVMNative ["1. JVM C/C++ 네이티브 엔진 (HotSpot Core)"]
        NativeParser["명령행 파라미터(-cp) 파싱"]
        NativeScanner["OS 시스템 콜 (POSIX stat, open / Win32 API)"]
        NativeZip["ZIP / JAR Central Directory 헤더 메모리 매핑"]
    end

    subgraph JavaRuntime ["2. Java 표준 라이브러리 계층 (ClassLoader)"]
        SysProp["java.class.path 시스템 프로퍼티 등록"]
        AppCL["AppClassLoader (jdk.internal.loader.ClassLoaders$AppClassLoader)"]
        DefineClass["JVM native defineClass() ➔ Metaspace 적재"]
    end

    subgraph BuildTools ["3. 빌드 도구 및 IDE 자동화 계층"]
        Gradle["Gradle / Maven (의존성 그래프 해석 ➔ 수 KB의 -cp 문자열 동적 생성)"]
    end

    User --> NativeParser
    NativeParser --> NativeScanner & NativeZip
    NativeScanner --> SysProp
    SysProp --> AppCL
    AppCL --> DefineClass
    Gradle -.->|"JVM 실행 시 -cp 자동 주입"| User
```

#### 1) JVM C/C++ 네이티브 엔진 (HotSpot Core Layer)

- `java` 실행 명령이 들어오면 OpenJDK HotSpot JVM 의 C/C++ 네이티브 런처가 `-cp` 뒤의 문자열을 파싱한다.
- JVM 네이티브 파일 스캐너는 OS 파일 시스템 API(POSIX `stat`, `open` 등)를 호출하여 지정된 디렉터리를 스캔하고, JAR 파일의 경우 압축을 풀지 않고 파일 끝부분의 **Central Directory Header**를 메모리에 매핑하여 내부 엔트리를 색인한다.

#### 2) Java 표준 라이브러리 클래스로더 계층 (Java Runtime Layer)

- JVM 이 네이티브 수준의 파일 핸들을 준비한 후, Java 표준 라이브러리의 **`Application ClassLoader (AppClassLoader)`** (`jdk.internal.loader.ClassLoaders$AppClassLoader`)에게 클래스 로딩을 위임한다.
- `AppClassLoader`는 JVM 이 전달한 `java.class.path` 시스템 프로퍼티의 경로 목록을 순차적으로 탐색하여 바이트코드(`byte[]`)를 읽어 들이고, 최종적으로 JVM 네이티브 메서드인 `defineClass()`를 호출하여 Metaspace 영역에 `Class<?>` 인스턴스를 생성한다.

#### 3) 빌드 도구 및 IDE 자동화 계층 (The Automation Layer)

- 현대 개발에서는 수십~수백 개의 라이브러리 경로를 개발자가 직접 손으로 `-cp` 에 작성하지 않는다.
- **Gradle / Maven**: 원격 저장소에서 의존성 JAR 를 다운로드하고, 충돌을 해결한 뒤, 컴파일러나 테스트 러너를 실행할 때 수 킬로바이트에 달하는 방대한 `-cp` 문자열을 동적으로 구성하여 JVM 프로세스에 전달한다.

---

### 3. 파일 시스템 경로 목록의 구체적 탐색 메커니즘

클래스로더는 찾고자 하는 클래스의 완전한 패키지명(FQCN, 예: `com.example.util.MathUtils`)을 파일 경로 형태(`com/example/util/MathUtils.class`)로 변환한 후, 클래스패스에 나열된 항목을 **왼쪽부터 오른쪽으로 순차 탐색**한다.

#### 1) 경로가 '디렉터리'인 경우 (`/app/build/classes`)

- 해당 디렉터리를 **패키지 루트 디렉터리**로 간주한다.
- 디렉터리 경로 뒤에 클래스 상대 경로를 이어 붙여 물리 파일(`/app/build/classes/com/example/util/MathUtils.class`)이 존재하는지 `stat` 파일 시스템 호출로 확인한다.

#### 2) 경로가 'JAR 아카이브 파일'인 경우 (`/libs/ktor.jar`)

- 해당 JAR(ZIP 파일)을 **패키지 루트 컨테이너**로 간주한다.
- JAR 파일을 디스크에 풀지 않고, JAR 내부의 **중앙 디렉터리 헤더(Central Directory Header)**에서 엔트리 이름(`com/example/util/MathUtils.class`)이 존재하는지 O(1) 메모리 인덱스로 검색한다.

---

### 4. 빌드 도구 관점에서의 3 단계 클래스패스 분리

현대 빌드 시스템(Gradle, Bazel)은 클래스 오염과 불필요한 빌드 전파를 방지하기 위해 클래스패스를 3 단계로 엄격히 분리하여 관리한다.

```mermaid
flowchart LR
    subgraph "1. Buildscript Classpath (빌드 런타임)"
        AGP["AGP / Kotlin Plugin / Detekt"] --> Daemon["Gradle Daemon 실행"]
    end

    subgraph "2. Compile Classpath (컴파일 시점)"
        Sources["src/main/kotlin"] --> K2["Kotlin Compiler"]
        Deps1["implementation / api / compileOnly"] --> K2
        K2 --> Classes["build/classes (.class)"]
    end

    subgraph "3. Runtime Classpath (실행 시점)"
        Classes --> App["App Process / Test Runner"]
        Deps2["implementation / api / runtimeOnly"] --> App
    end
```

| 구분 | 목적 | 포함 대상 | 배제 대상 |
|---|---|---|---|
| **Buildscript / Plugin Classpath** | 빌드 도구 자체 및 플러그인 구동 | AGP, Detekt, Compose Compiler Plugin, Kotlin Gradle Plugin | 앱 소스 코드, 앱 런타임 라이브러리 |
| **Compile Classpath** | 소스 코드(`src/`)의 문법 검증 및 바이트코드 생성 | `api`, `implementation`, `compileOnly` | `runtimeOnly` (컴파일 시점에 불필요한 구현체) |
| **Runtime Classpath** | 컴파일된 코드가 실제 실행/테스트될 때 클래스 로딩 | `api`, `implementation`, `runtimeOnly` | `compileOnly` (어노테이션, 빌드 전용 타입) |

---

### 5. 클래스패스 탐색 규칙과 Jar Hell (클래스 충돌)

클래스로더는 클래스패스에 지정된 순서대로 탐색하며, **가장 먼저 발견된 클래스를 로드하고 탐색을 즉시 종료(First-match wins)**한다.

```text
클래스패스: [ lib-v1.0.jar : lib-v2.0.jar ]
             └── com.example.Util.class 가 양쪽에 존재할 때
                 ➔ 항상 lib-v1.0.jar 의 Util 이 로드됨 (Class Shadowing)
```

#### Jar Hell (의존성 지옥)과 클래스 섀도잉

- 서로 다른 라이브러리가 동일한 패키지/클래스명을 가진 구버전과 신버전 클래스를 각각 포함할 경우, 클래스패스 순서에 따라 런타임에 예기치 않은 메서드 누락(`NoSuchMethodError`)이나 비정상 동작이 발생한다.
- Gradle 은 이를 해결하기 위해 **의존성 그래프 단일 버전 해결 규칙(Dependency Conflict Resolution)** 을 사용하여 최신 버전을 선택하거나 버전을 강제 통일한다.

---

### 6. ClassNotFoundException vs NoClassDefFoundError

- **`ClassNotFoundException` (런타임 동적 탐색 실패)**:
  - `Class.forName("com.example.MyClass")` 또는 리플렉션을 통해 동적으로 클래스명을 조회했으나, 클래스패스 상의 어떤 경로에도 해당 `.class` 파일이 존재하지 않을 때 발생한다.
- **`NoClassDefFoundError` (컴파일 성공 후 런타임 로드 실패)**:
  - 컴파일 시점에는 클래스패스에 클래스가 존재하여 컴파일에 성공했으나, **런타임 클래스패스에서 해당 클래스나 의존 클래스가 누락되었거나 정적 초기화(`static {}`) 블록에서 예외가 발생**하여 클래스 정의를 읽지 못할 때 발생한다.

---

### 7. Classpath vs Modulepath (Java 9+ JPMS)

- **Classpath**: 평면적인(Flat) 경로 구조로, 모든 JAR 의 패키지가 하나의 전역 네임스페이스로 병합된다. 캡슐화가 없고 런타임 클래스 누락을 기동 전에 검증할 수 없다.
- **Modulepath**: Java 9 JPMS(Java Platform Module System)에서 도입된 명시적 모듈 경로(`module-info.java`)로, 모듈 간 공개 패키지와 의존성을 명시적으로 선언하여 컴파일/기동 시점에 캡슐화와 의존성 완전성을 엄격히 검증한다.

---

### 상위 및 연관 문서

- [JVM 아키텍처와 런타임 실행 엔진](jvm-architecture.md)
- [JVM 클래스로더 메커니즘 (ClassLoader)](jvm-classloader.md)
- [바이트코드 파일(.class)과 아카이브 파일(.jar)의 본질](jvm-bytecode-and-jar-archive.md)
- [API vs ABI](api-vs-abi.md)
- [Gradle 의존성 구성 및 클래스패스 격리](../mobile/android/03_packaging_deployment/build/gradle/gradle-build/gradle-dependency-configurations.md)
- [Gradle 플러그인(Plugin)과 의존성(Dependency)의 차이](../mobile/android/03_packaging_deployment/build/gradle/gradle-build/gradle-plugins-vs-dependencies.md)
