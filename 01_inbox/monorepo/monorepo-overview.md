---
title: monorepo-overview
tags: []
aliases: []
date modified: 2026-04-07 17:16:00 +09:00
date created: 2026-04-07 17:09:56 +09:00
---

## Monorepo Architecture Overview

>전체 모노레포 구조와 각 레이어의 역할

```
repo/  
├── apps/ # Entry points: 각 플랫폼에서 앱 실행 + feature 조합  
│ ├── mobile-ios/ # iOS app  
│ ├── mobile-android/ # Android app  
│ ├── watch/ # watchOS + Android Watch apps  
│ ├── tv/ # tvOS + Android TV apps  
│ ├── xr/ # VisionOS + Android XR apps  
│ ├── car/ # CarPlay + Android Auto apps  
│ ├── desktop/ # macOS + Android Desktop apps  
│ └── web/ # Web app  
│
├── platforms/ # Platform-specific runtime implementations  
│ ├── apple/ # iOS, macOS, watchOS, tvOS, VisionOS, CarPlay  
│ │ ├── navigation/  
│ │ ├── lifecycle/  
│ │ └── storage/  
│ ├── android/ # Android mobile, watch, TV, XR, Auto, Desktop  
│ │ ├── navigation/  
│ │ ├── lifecycle/  
│ │ └── storage/  
│ ├── web/ # SSR / CSR, routing, state management  
│ │ ├── rendering/  
│ │ ├── routing/  
│ │ └── state/  
│ └── server/ # Backend runtime (Node, JVM, etc.)  
│
├── features/ # User-visible features (platform-independent orchestration)  
│ ├── home/  
│ │ ├── core/ # Business logic orchestration, platform-independent  
│ │ ├── ios/  
│ │ ├── android/  
│ │ └── web/  
│ ├── profile/  
│ │ ├── core/  
│ │ ├── ios/  
│ │ ├── android/  
│ │ └── web/  
│ └── playback/  
│ ├── core/  
│ ├── ios/  
│ ├── android/  
│ └── web/  
│  
├── domain/ # Core business rules (state transitions, validation)  
│ ├── user/  
│ ├── content/  
│ └── auth/  
│  
├── contracts/ # Boundary definitions (API / events / DTOs)  
│ ├── api/  
│ ├── events/  
│ └── schemas/  
│  
├── services/ # Backend services (microservices)  
│ ├── user-service/  
│ │ ├── api/  
│ │ ├── domain/  
│ │ └── infra/  
│ ├── content-service/  
│ │ ├── api/  
│ │ ├── domain/  
│ │ └── infra/  
│ └── auth-service/  
│ ├── api/  
│ ├── domain/  
│ └── infra/  
│  
├── design-system/ # UI consistency, tokens & components  
│ ├── tokens/ # Colors, spacing, typography  
│ ├── mobile/ # UIKit / Jetpack Compose components  
│ └── web/ # React / CSS components  
│  
└── infra/ # CI/CD, deployment, observability  
```

### Layered Responsibilities

- **apps/**: 앱 실행 포인트. feature 조합만 담당, 플랫폼 로직 없음.
- **platforms/**: 각 플랫폼 별 runtime, navigation, lifecycle, storage 등의 구현을 캡슐화. feature 가 플랫폼을 몰라도 되도록 보호.
- **features/**: 유저 기능 단위. core 는 플랫폼 독립, 각 플랫폼별 폴더에서 실제 UI/interaction 구현.
- **domain/**: 비즈니스 규칙과 상태 전이. 절대 플랫폼 의존 X.
- **contracts/**: 서비스/API boundary 정의. 프론트 ↔ 백엔드, 서비스 ↔ 서비스 간 통신 약속.
- **services/**: backend microservices. domain/feature/infra 를 포함, 독립 배포 가능.
- **design-system/**: 공통 UI 구성요소와 tokens, 플랫폼별 컴포넌트 포함.
- **infra/**: CI/CD, 배포 스크립트, 모니터링, 로그, 테스팅 환경.
  
---

이 구조를 기준으로 하면, **iOS/Android/Web/Watch/TV/XR/Car/Desktop + Backend microservices**까지 모두 포함하면서도 레이어 간 책임이 명확하게 구분되어 확장과 유지보수 용이성이 확보됩니다.
