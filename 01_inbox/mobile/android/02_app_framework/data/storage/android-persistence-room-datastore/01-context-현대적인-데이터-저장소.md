# 💡 Context: 현대적인 데이터 저장소

모바일 앱에서 오프라인 모드 지원은 더 이상 옵션이 아닙니다. `Room` 은 기존의 복잡한 SQLite 사용법을 현대적으로 추상화하며, `DataStore` 는 결함이 많았던 `SharedPreferences` 를 대체하여 타입 세이프하고 비동기적인 데이터 접근을 보장합니다.

---

>[!NOTE] **iOS 비교: SwiftData vs Room/DataStore**
> - **iOS**: `SwiftData` 가 SQLite 를 추상화하며, `@Model` 매크로와 `Query` 를 통해 선언형 데이터 관리를 제공한다. (iOS 17+)
> - **Android**: `Room` 이 SQLite 를 추상화하며, `Flow` 와의 강력한 통합을 통해 반응형 데이터 스트림을 구축한다. **DataStore**는 `SharedPreferences` 를 대체하여 타입 세이프하고 비동기적인 설정 저장을 보장한다.
>자세한 내용은 [[apple-swiftdata-deep-dive]] 를 참고하세요.
