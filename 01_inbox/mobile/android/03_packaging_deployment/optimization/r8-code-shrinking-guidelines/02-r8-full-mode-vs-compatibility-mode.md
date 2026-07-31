# R8 Full Mode vs Compatibility Mode

R8은 ProGuard와의 하위 호환성을 유지하는 **Compatibility Mode**와 더 적극적이고 강하게 최적화를 적용하는 **Full Mode**를 지원합니다.

* **Full Mode (`android.enableR8.fullMode=true`)**:
  * 최신 AGP 환경에서는 기본적으로 **Full Mode가 활성화**되어 있습니다.
  * 계층 구조 최적화 및 인라이닝이 훨씬 강력하게 동작하지만, **Reflection(반사 API)**이나 디시리얼라이제이션(JSON 변환)을 사용하는 코드에서 명시적인 규칙(`-keep`)이 없으면 런타임에 에러가 발생할 수 있습니다.

---
