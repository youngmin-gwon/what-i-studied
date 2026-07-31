# Android Context 완전 가이드

이 문서는 Android 개발에서 거의 모든 곳에 등장하는 **`Context`**가 무엇인지, 왜 필요한지, 어떤 종류가 있고, 현대
Compose/ViewModel/Repository 구조에서는 어떻게 다뤄야 하는지를 정리합니다.

관련 공식 문서:

- [Context API reference](https://developer.android.com/reference/android/content/Context)
- [App resources overview](https://developer.android.com/guide/topics/resources/providing-resources)
- [Data and file storage overview](https://developer.android.com/training/data-storage)

---

---

## 원자 노트

- [Context란?](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context/01-context%EB%9E%80.md)
- [Context가 할 수 있는 일](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context/02-context%EA%B0%80-%ED%95%A0-%EC%88%98-%EC%9E%88%EB%8A%94-%EC%9D%BC.md)
- [Context의 대표 종류](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context/03-context%EC%9D%98-%EB%8C%80%ED%91%9C-%EC%A2%85%EB%A5%98.md)
- [Application Context](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context/04-application-context.md)
- [Activity Context](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context/05-activity-context.md)
- [Service, Receiver, Provider의 Context](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context/06-service-receiver-provider%EC%9D%98-context.md)
- [Compose에서 Context: LocalContext](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context/07-compose%EC%97%90%EC%84%9C-context-localcontext.md)
- [Flutter BuildContext와 Android Context는 다르다](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context/08-flutter-buildcontext%EC%99%80-android-context%EB%8A%94-%EB%8B%A4%EB%A5%B4%EB%8B%A4.md)
- [Context와 ViewModel/Repository](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context/09-context%EC%99%80-viewmodel-repository.md)
- [자주 하는 실수](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context/10-%EC%9E%90%EC%A3%BC-%ED%95%98%EB%8A%94-%EC%8B%A4%EC%88%98.md)
- [선택 기준 요약](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context/11-%EC%84%A0%ED%83%9D-%EA%B8%B0%EC%A4%80-%EC%9A%94%EC%95%BD.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
