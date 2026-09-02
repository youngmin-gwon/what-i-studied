---
title: apple-packaging-deployment-map
tags: [apple, apple/packaging, distribution, map, moc, xcode]
aliases: ["서명·프로비저닝·심사는 서로 다른 시점의 독립 게이트다", "Apple Packaging & Deployment Map", "Apple 패키징 배포 지도"]
date modified: 2026-09-03 00:00:00 +09:00
date created: 2026-09-03 00:00:00 +09:00
---

## 서명·프로비저닝·심사는 서로 다른 시점의 독립 게이트다

소스에서 사용자 기기까지 가는 길에는 통과 시점이 다른 관문이 여러 개 있다. **의존성 해석(SPM)** 은 빌드 이전, **코드 서명과 entitlement 봉인**은 빌드 시점, **프로비저닝 프로파일 매칭**은 설치 시점, **App Store 심사**는 배포 시점이다. "Profile doesn't match the entitlements" 같은 오류가 어느 관문에서 났는지 먼저 나눠야 고칠 대상이 정해진다. 이 폴더는 그 관문들을 다룬다.

### 정본 노트

- [apple-swift-package-manager](apple-swift-package-manager.md) - 의존성 해석과 로컬 패키지 기반 모듈화.
- [apple-build-and-distribution](apple-build-and-distribution.md) - 코드 서명 신뢰 사슬, 빌드 파이프라인, 아카이브와 검증.
- [apple-distribution-and-policies](apple-distribution-and-policies.md) - App Store 심사 가이드라인, 주요 반려 사유, 글로벌 규제.
- [apple-app-clips](apple-app-clips.md) - 설치 없이 실행되는 경량 배포 단위와 크기 제한.

### 경계

이 폴더에는 **아티팩트를 만들고 내보내는 과정**만 둔다. entitlement 가 런타임에 무엇을 여는지, 샌드박스가 무엇을 막는지는 [05_security_privacy](../05_security_privacy/mobile-apple-foundation-security.md) 에 둔다.

### 연관 문서

- [apple-security-entitlements](../05_security_privacy/apple-security-entitlements.md) - 서명에 봉인되는 권한 명세
- [apple-privacy-and-tcc-details](../05_security_privacy/apple-privacy-and-tcc-details.md) - Privacy Manifest 심사 요구사항
- [apple-testing-and-quality](../06_testing_performance/apple-testing-and-quality.md) - CI/CD 와 TestFlight 배포 자동화
- [android-packaging-deployment](../../android/03_packaging_deployment/android-packaging-deployment.md) - 안드로이드 대응 영역
