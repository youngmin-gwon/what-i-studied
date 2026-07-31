# Compose CompositionLocal과 이 프로젝트의 Local 값

이 문서는 Jetpack Compose의 `CompositionLocal` 개념과, 현재 design system에 있는 `LocalMyBenefit*` 값들이 어떤 역할을 하는지
정리합니다.

관련 공식 문서:

- [CompositionLocal in Jetpack Compose](https://developer.android.com/develop/ui/compose/compositionlocal)
- [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
- [Architecture layering in Compose](https://developer.android.com/develop/ui/compose/architecture)

---

---

## 원자 노트

- [[01-compositionlocal이란|CompositionLocal이란?]]
- [[02-local이라는-이름|Local이라는 이름]]
- [[03-언제-compositionlocal을-쓰나|언제 CompositionLocal을 쓰나?]]
- [[04-compositionlocalof와-staticcompositionlocalof|compositionLocalOf와 staticCompositionLocalOf]]
- [[05-이-프로젝트의-adaptive-값-흐름|이 프로젝트의 adaptive 값 흐름]]
- [[06-각-파일의-역할|각 파일의 역할]]
- [[07-화면에서-사용하는-방식|화면에서 사용하는 방식]]
- [[08-언제-직접-local을-읽어도-되나|언제 직접 Local을 읽어도 되나?]]
- [[09-왜-이렇게-나눴나|왜 이렇게 나눴나?]]
- [[10-compositionlocalprovider-및-유사한-스코프-제공-composable-패턴|CompositionLocalProvider 및 유사한 스코프 제공 Composable 패턴]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
