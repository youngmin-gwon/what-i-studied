# Jetpack Navigation 3 가이드

이 문서는 Jetpack Compose 환경에서 Navigation 3를 사용하는 방법을 정리합니다. 핵심은 **화면 이동을 라이브러리 내부 상태가 아니라 앱이 소유한 `NavKey` back stack 상태로 표현한다**는 점입니다.

---

---

## 원자 노트

- [[01-핵심-모델|핵심 모델]]
- [[02-의존성|의존성]]
- [[03-route-key-설계|Route Key 설계]]
- [[04-back-stack-관리|Back Stack 관리]]
- [[05-entry-provider|Entry Provider]]
- [[06-navdisplay-기본형|NavDisplay 기본형]]
- [[07-viewmodel과-state|ViewModel과 State]]
- [[08-metadata|Metadata]]
- [[09-scene과-기본-제공-strategy|Scene과 기본 제공 Strategy]]
- [[10-scene-decorator|Scene Decorator]]
- [[11-animation|Animation]]
- [[12-deep-link|Deep Link]]
- [[13-이-프로젝트-권장-구조|이 프로젝트 권장 구조]]
- [[14-android-task와-app-back-stack|Android Task와 App Back Stack]]
- [[15-체크리스트|체크리스트]]
- [[16-관련-문서|관련 문서]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
