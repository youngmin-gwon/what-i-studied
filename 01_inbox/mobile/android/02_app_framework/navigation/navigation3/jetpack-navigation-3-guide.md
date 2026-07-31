# Jetpack Navigation 3 가이드

이 문서는 Jetpack Compose 환경에서 Navigation 3를 사용하는 방법을 정리합니다. 핵심은 **화면 이동을 라이브러리 내부 상태가 아니라 앱이 소유한 `NavKey` back stack 상태로 표현한다**는 점입니다.

---

---

## 원자 노트

- [핵심 모델](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/01-%ED%95%B5%EC%8B%AC-%EB%AA%A8%EB%8D%B8.md)
- [의존성](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/02-%EC%9D%98%EC%A1%B4%EC%84%B1.md)
- [Route Key 설계](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/03-route-key-%EC%84%A4%EA%B3%84.md)
- [Back Stack 관리](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/04-back-stack-%EA%B4%80%EB%A6%AC.md)
- [Entry Provider](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/05-entry-provider.md)
- [NavDisplay 기본형](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/06-navdisplay-%EA%B8%B0%EB%B3%B8%ED%98%95.md)
- [ViewModel과 State](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/07-viewmodel%EA%B3%BC-state.md)
- [Metadata](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/08-metadata.md)
- [Scene과 기본 제공 Strategy](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/09-scene%EA%B3%BC-%EA%B8%B0%EB%B3%B8-%EC%A0%9C%EA%B3%B5-strategy.md)
- [Scene Decorator](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/10-scene-decorator.md)
- [Animation](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/11-animation.md)
- [Deep Link](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/12-deep-link.md)
- [이 프로젝트 권장 구조](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/13-%EC%9D%B4-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B6%8C%EC%9E%A5-%EA%B5%AC%EC%A1%B0.md)
- [Android Task와 App Back Stack](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/14-android-task%EC%99%80-app-back-stack.md)
- [체크리스트](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/15-%EC%B2%B4%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%8A%B8.md)
- [관련 문서](01_inbox/mobile/android/02_app_framework/navigation/navigation3/jetpack-navigation-3-guide/16-%EA%B4%80%EB%A0%A8-%EB%AC%B8%EC%84%9C.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
