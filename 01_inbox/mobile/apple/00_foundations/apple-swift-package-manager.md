---
title: apple-swift-package-manager
tags: [apple, dependencies, modularization, spm, swift, xcode]
aliases: []
date modified: 2026-04-06 17:51:30 +09:00
date created: 2026-04-03 23:58:00 +09:00
---

## Swift Package Manager (SPM) Deep Dive

CocoaPods 의 `Podfile`, Carthage 의 `Cartfile` 시대는 끝났습니다.

**Swift Package Manager**는 Apple 이 공식으로 제공하는 의존성 관리 + 모듈화 도구이며, Xcode 에 완전히 통합되어 있습니다.

### 💡 왜 이것을 알아야 하나요? (Context)

- **표준화**: Apple 의 모든 오픈소스 프레임워크(`swift-collections`, `swift-algorithms`, `swift-testing` 등)가 SPM 으로 배포됩니다. CocoaPods 는 유지보수 모드에 들어갔고, 새로운 라이브러리들은 SPM-only 가 늘어나고 있습니다.
- **모듈화(Modularization)**: 대규모 앱에서 빌드 시간과 팀 간 의존성을 관리하려면 앱을 여러 로컬 패키지로 쪼개야 합니다. SPM 이 이를 가장 자연스럽게 지원합니다.
- **CI/CD 친화적**: `swift build`, `swift test` 명령어로 Xcode 없이도 빌드/테스트가 가능합니다. GitHub Actions 등에서 활용하기 좋습니다.

>[!CAUTION] **Devil's Advocate : CocoaPods/Carthage 에서의 탈출**
>레거시 프로젝트에서 CocoaPods 를 SPM 으로 전환할 때 주의사항:
> 1. 일부 라이브러리(Firebase 등 대형 SDK)는 과거 SPM 지원이 불안정했으나, 2024 년 기준 대부분 안정화되었습니다.
> 2. **Binary Dependency**: 소스가 비공개인 SDK 는 `XCFramework` 를 SPM 패키지로 감싸서 배포합니다.
> 3. **혼합 사용**: 전환 기간에는 CocoaPods + SPM 을 동시에 사용할 수 있지만, 같은 라이브러리를 양쪽에서 중복 참조하면 링크 에러가 발생합니다.

---

### 📦 Package.swift 구조

모든 SPM 패키지의 핵심은 `Package.swift` 파일입니다.

```swift
// swift-tools-version: 5.10
import PackageDescription

let package = Package(
    name: "MyCore",
    platforms: [.iOS(.v17), .macOS(.v14)],
    products: [
        // 외부에 노출할 모듈
        .library(name: "Networking", targets: ["Networking"]),
        .library(name: "Models", targets: ["Models"]),
    ],
    dependencies: [
        // 외부 패키지 의존성
        .package(url: "https://github.com/Alamofire/Alamofire.git", from: "5.9.0"),
    ],
    targets: [
        .target(
            name: "Networking",
            dependencies: ["Models", "Alamofire"]
        ),
        .target(name: "Models"),
        // 테스트 타겟
        .testTarget(
            name: "NetworkingTests",
            dependencies: ["Networking"]
        ),
    ]
)
```

#### 핵심 개념
- **Product**: 패키지가 외부에 노출하는 모듈. `.library` (다른 타겟이 import 가능) 또는 `.executable`.
- **Target**: 소스 코드의 논리적 단위. 각 타겟은 `Sources/<TargetName>/` 디렉토리에 코드를 둡니다.
- **Dependency**: 다른 패키지(원격 URL 또는 로컬 경로)에 대한 의존성.

---

### 🏗️ 앱 모듈화 전략 (Local Packages)

대규모 앱은 로컬 SPM 패키지로 분리하면 빌드 시간과 코드 관리가 극적으로 개선됩니다.

```
MyApp/
├── App/                        # Xcode 프로젝트 (얇은 셸)
│   ├── MyApp.xcodeproj
│   └── Sources/
│       └── AppEntry.swift      # @main, DI 조립
│
├── Packages/
│   ├── Core/                   # 공유 유틸리티, 확장
│   │   └── Package.swift
│   ├── Models/                 # Codable 엔티티, SwiftData 모델
│   │   └── Package.swift
│   ├── Networking/             # API 클라이언트
│   │   └── Package.swift
│   ├── DesignSystem/           # 공통 UI 컴포넌트, 색상, 폰트
│   │   └── Package.swift
│   └── Features/
│       ├── LoginFeature/       # 로그인 화면 + ViewModel
│       └── HomeFeature/        # 홈 화면 + ViewModel
```

#### 핵심 원칙

1. **단방향 의존성**: Feature → Domain → Core. Feature 간 직접 의존 금지.
2. **Interface 분리**: 프로토콜을 별도 타겟으로 분리하면, Mock 을 쉽게 만들 수 있습니다.
3. **증분 빌드(Incremental Build)**: 변경된 모듈만 재컴파일됩니다. 모노리식 대비 빌드 시간 50-80% 절감 가능.

---

### 🔧 주요 기능

#### 1. 의존성 버전 관리

```swift
// 시맨틱 버전 (권장)
.package(url: "...", from: "5.0.0")         // 5.0.0 이상, 6.0.0 미만
.package(url: "...", exact: "5.2.1")         // 정확히 5.2.1
.package(url: "...", "5.0.0"..<"5.3.0")     // 범위 지정

// 브랜치/커밋 (개발 중에만 사용)
.package(url: "...", branch: "main")
.package(url: "...", revision: "abc123")

// 로컬 경로 (모듈화 시 필수)
.package(path: "../Packages/Core")
```

#### 2. Resource 번들링

이미지, JSON, 스토리보드 등의 리소스를 패키지에 포함할 수 있습니다.

```swift
.target(
    name: "DesignSystem",
    resources: [
        .process("Resources/Colors.xcassets"),  // 자동 처리
        .copy("Resources/config.json"),          // 그대로 복사
    ]
)
```

접근: `Bundle.module.url(forResource: "config", withExtension: "json")`

#### 3. Plugin 시스템

코드 생성(SwiftGen, Sourcery 등)을 빌드 과정에 통합할 수 있습니다.

```swift
.plugin(name: "MyCodeGenPlugin", capability: .buildTool())
```

#### 4. Macro Target

Swift 5.9+ 매크로를 SPM 패키지로 배포할 수 있습니다.

```swift
.macro(name: "MyMacros", dependencies: [
    .product(name: "SwiftSyntaxMacros", package: "swift-syntax"),
])
```

---

### 🛠️ CLI 사용법

Xcode 없이도 터미널에서 패키지를 관리할 수 있습니다.

```bash
# 새 패키지 생성
swift package init --type library

# 의존성 해결
swift package resolve

# 빌드
swift build

# 테스트
swift test

# Xcode 프로젝트 생성 (필요시)
swift package generate-xcodeproj  # ⚠️ deprecated, 직접 Package.swift 를 Xcode 에서 열기 권장
```

---

### ⚠️ 주의사항 & Best Practices

1. **`.build` 디렉토리**: SPM 이 캐시와 빌드 산출물을 저장합니다. `.gitignore` 에 반드시 추가하세요.
2. **Resolution 충돌**: 두 패키지가 같은 라이브러리의 다른 버전을 요구하면 빌드가 실패합니다. `Package.resolved` 파일을 커밋하여 팀 내 버전을 동기화하세요.
3. **Access Control**: 패키지 간에는 `public` 으로 선언된 타입만 접근 가능합니다. `internal`(기본값)은 같은 모듈 내에서만 보입니다.

### 더 보기

- [apple-cross-platform-architecture](../07_platforms/apple-cross-platform-architecture.md) - SPM 을 활용한 크로스 플랫폼 코드 공유
- [apple-build-and-distribution](../05_security_privacy/apple-build-and-distribution.md) - 빌드 파이프라인에서 SPM 이 차지하는 위치
- [apple-testing-and-quality](../06_testing_performance/apple-testing-and-quality.md) - 모듈별 독립 테스트 전략
