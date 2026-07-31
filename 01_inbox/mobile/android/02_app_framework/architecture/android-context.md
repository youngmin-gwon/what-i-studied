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

- [[01-context란|Context란?]]
- [[02-context가-할-수-있는-일|Context가 할 수 있는 일]]
- [[03-context의-대표-종류|Context의 대표 종류]]
- [[04-application-context|Application Context]]
- [[05-activity-context|Activity Context]]
- [[06-service-receiver-provider의-context|Service, Receiver, Provider의 Context]]
- [[07-compose에서-context-localcontext|Compose에서 Context: LocalContext]]
- [[08-flutter-buildcontext와-android-context는-다르다|Flutter BuildContext와 Android Context는 다르다]]
- [[09-context와-viewmodel-repository|Context와 ViewModel/Repository]]
- [[10-자주-하는-실수|자주 하는 실수]]
- [[11-선택-기준-요약|선택 기준 요약]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
