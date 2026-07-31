# DerivedStateOf의 올바른 활용

## 원자 노트

### 개요
- [03-derivedstateof의-올바른-활용-00-개요](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/03-derivedstateof%EC%9D%98-%EC%98%AC%EB%B0%94%EB%A5%B8-%ED%99%9C%EC%9A%A9/03-derivedstateof%EC%9D%98-%EC%98%AC%EB%B0%94%EB%A5%B8-%ED%99%9C%EC%9A%A9-00-%EA%B0%9C%EC%9A%94.md)

### 2-1. 잘못된 사용 vs 올바른 사용
- [01-잘못된-사용-vs-올바른-사용](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/03-derivedstateof%EC%9D%98-%EC%98%AC%EB%B0%94%EB%A5%B8-%ED%99%9C%EC%9A%A9/01-%EC%9E%98%EB%AA%BB%EB%90%9C-%EC%82%AC%EC%9A%A9-vs-%EC%98%AC%EB%B0%94%EB%A5%B8-%EC%82%AC%EC%9A%A9.md)

### 3-1. 불안정(Unstable) 타입과 기존 문제점
- [02-불안정-unstable-타입과-기존-문제점](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/03-derivedstateof%EC%9D%98-%EC%98%AC%EB%B0%94%EB%A5%B8-%ED%99%9C%EC%9A%A9/02-%EB%B6%88%EC%95%88%EC%A0%95-unstable-%ED%83%80%EC%9E%85%EA%B3%BC-%EA%B8%B0%EC%A1%B4-%EB%AC%B8%EC%A0%9C%EC%A0%90.md)

### 3-2. Kotlin 2.x (Strong Skipping Mode) 도입 이후 변화
- [03-kotlin-2-x-strong-skipping-mode-도입-이후-변화](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/03-derivedstateof%EC%9D%98-%EC%98%AC%EB%B0%94%EB%A5%B8-%ED%99%9C%EC%9A%A9/03-kotlin-2-x-strong-skipping-mode-%EB%8F%84%EC%9E%85-%EC%9D%B4%ED%9B%84-%EB%B3%80%ED%99%94.md)

### 3-3. kotlinx-collections-immutable 도입 가이드라인
- [04-kotlinx-collections-immutable-도입-가이드라인](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/03-derivedstateof%EC%9D%98-%EC%98%AC%EB%B0%94%EB%A5%B8-%ED%99%9C%EC%9A%A9/04-kotlinx-collections-immutable-%EB%8F%84%EC%9E%85-%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8.md)

### 3-4. 외부 라이브러리 및 클래스를 위한 Stability Configuration File 활용
- [05-외부-라이브러리-및-클래스를-위한-stability-configuration-file-활용](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/03-derivedstateof%EC%9D%98-%EC%98%AC%EB%B0%94%EB%A5%B8-%ED%99%9C%EC%9A%A9/05-%EC%99%B8%EB%B6%80-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-%EB%B0%8F-%ED%81%B4%EB%9E%98%EC%8A%A4%EB%A5%BC-%EC%9C%84%ED%95%9C-stability-configuration-file-%ED%99%9C%EC%9A%A9.md)
