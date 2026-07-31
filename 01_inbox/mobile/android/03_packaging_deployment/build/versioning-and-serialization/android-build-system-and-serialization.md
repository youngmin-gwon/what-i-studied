# 안드로이드 빌드 시스템 & 직렬화(Serialization) 가이드

이 문서는 안드로이드 프로젝트의 의존성 관리 시스템인 **Version Catalog(`libs.versions.toml`)**, 타입 안전한 내비게이션을 가능하게 하는 *
*`kotlinx.serialization`**, 그리고 **KAPT → KSP → 컴파일러 플러그인**으로 이어지는 안드로이드 빌드 파이프라인의 진화사를 다룹니다.

---

---

## 원자 노트

- [Version Catalog (`libs.versions.toml`)](01_inbox/mobile/android/03_packaging_deployment/build/versioning-and-serialization/android-build-system-and-serialization/01-version-catalog-libs-versions-toml.md)
- [Serialization (`kotlinx.serialization`)](01_inbox/mobile/android/03_packaging_deployment/build/versioning-and-serialization/android-build-system-and-serialization/02-serialization-kotlinx-serialization.md)
- [빌드 파이프라인의 진화: KAPT → KSP → 컴파일러 플러그인](01_inbox/mobile/android/03_packaging_deployment/build/versioning-and-serialization/android-build-system-and-serialization/03-%EB%B9%8C%EB%93%9C-%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8%EC%9D%98-%EC%A7%84%ED%99%94-kapt-ksp-%EC%BB%B4%ED%8C%8C%EC%9D%BC%EB%9F%AC-%ED%94%8C%EB%9F%AC%EA%B7%B8%EC%9D%B8.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
