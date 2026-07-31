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

- [CompositionLocal이란?](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals/01-compositionlocal%EC%9D%B4%EB%9E%80.md)
- [Local이라는 이름](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals/02-local%EC%9D%B4%EB%9D%BC%EB%8A%94-%EC%9D%B4%EB%A6%84.md)
- [언제 CompositionLocal을 쓰나?](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals/03-%EC%96%B8%EC%A0%9C-compositionlocal%EC%9D%84-%EC%93%B0%EB%82%98.md)
- [compositionLocalOf와 staticCompositionLocalOf](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals/04-compositionlocalof%EC%99%80-staticcompositionlocalof.md)
- [이 프로젝트의 adaptive 값 흐름](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals/05-%EC%9D%B4-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EC%9D%98-adaptive-%EA%B0%92-%ED%9D%90%EB%A6%84.md)
- [각 파일의 역할](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals/06-%EA%B0%81-%ED%8C%8C%EC%9D%BC%EC%9D%98-%EC%97%AD%ED%95%A0.md)
- [화면에서 사용하는 방식](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals/07-%ED%99%94%EB%A9%B4%EC%97%90%EC%84%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EB%B0%A9%EC%8B%9D.md)
- [언제 직접 Local을 읽어도 되나?](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals/08-%EC%96%B8%EC%A0%9C-%EC%A7%81%EC%A0%91-local%EC%9D%84-%EC%9D%BD%EC%96%B4%EB%8F%84-%EB%90%98%EB%82%98.md)
- [왜 이렇게 나눴나?](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals/09-%EC%99%9C-%EC%9D%B4%EB%A0%87%EA%B2%8C-%EB%82%98%EB%88%B4%EB%82%98.md)
- [CompositionLocalProvider 및 유사한 스코프 제공 Composable 패턴](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals/10-compositionlocalprovider-%EB%B0%8F-%EC%9C%A0%EC%82%AC%ED%95%9C-%EC%8A%A4%EC%BD%94%ED%94%84-%EC%A0%9C%EA%B3%B5-composable-%ED%8C%A8%ED%84%B4.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
