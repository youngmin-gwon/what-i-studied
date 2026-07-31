# Kotlin Metadata 스트리핑 (Kotlin Metadata Optimization)
* 코틀린 컴파일러는 디버깅 및 Reflection을 위해 클래스 파일마다 `@Metadata` 어노테이션을 부착합니다.
* R8은 릴리즈 빌드 시 Reflection에 사용되지 않는 불필요한 코틀린 메타데이터 스트링 파라미터를 도려내어 DEX 용량을 추가로 절감합니다.

---
