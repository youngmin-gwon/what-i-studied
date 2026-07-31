# 💡 Context: 생명주기 관리의 실제

현대적인 안드로이드 앱 개발에서는 단일 액티비티 구조(Single-Activity Architecture)가 표준입니다. 콜백 메서드의 순서를 아는 것보다, 구성 변경(Configuration Change)과 프로세스 데스의 차이를 명확히 구분하고 데이터 손실을 방지하는 것이 훨씬 중요합니다.

---

>[!CAUTION] **Devil's Advocate : 다중 Activity 시대의 종말**
>안드로이드 초창기에는 화면마다 `Activity` 를 하나씩 만들어 매니페스트에 등록하는 것이 국룰이었습니다. 하지만, 현재는 **Single-Activity Architecture (단일 액티비티 구조)**가 완전한 표준입니다.
>화면 전환은 Activity 간 `Intent` 통신이 아니라, 하나의 `MainActivity` 위에서 `Compose Navigation` (또는 Fragment) 교체를 통해 이루어집니다. 복잡한 다중 Activity 구조는 명백한 레거시 패턴입니다.
