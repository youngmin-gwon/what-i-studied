# 안드로이드 빌드 시스템 & 직렬화(Serialization) 가이드

이 문서는 안드로이드 프로젝트의 의존성 관리 시스템인 **Version Catalog(`libs.versions.toml`)**, 타입 안전한 내비게이션을 가능하게 하는 *
*`kotlinx.serialization`**, 그리고 **KAPT → KSP → 컴파일러 플러그인**으로 이어지는 안드로이드 빌드 파이프라인의 진화사를 다룹니다.

---

---

## 원자 노트

- [[01-version-catalog-libs-versions-toml|Version Catalog (`libs.versions.toml`)]]
- [[02-serialization-kotlinx-serialization|Serialization (`kotlinx.serialization`)]]
- [[03-빌드-파이프라인의-진화-kapt-ksp-컴파일러-플러그인|빌드 파이프라인의 진화: KAPT → KSP → 컴파일러 플러그인]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
