# Context

상위 노트: [android-glossary](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md)

**정의**: 앱 환경에 대한 전역 정보 접근 인터페이스 (God Object)

**상세**:

Android 시스템의 핵심 핸들로, 리소스 로드, 컴포넌트 실행 (Activity/Service), 시스템 서비스 접근 등 거의 모든 작업에 필요하다.

`ApplicationContext` (싱글톤) 와 `ActivityContext` (UI 관련) 의 수명 주기가 다르므로 메모리 누수에 주의해야 한다.

**사용**:

```kotlin
// 리소스 접근
val color = context.getColor(R.color.black)

// 시스템 서비스
val am = context.getSystemService(Context.ACTIVITY_SERVICE)
```

**Memory Leak 주의**:

```kotlin
// ❌ Activity Context를 오래 사는 객체에 저장하면 누수!
Singleton.context = activity // Activity가 파괴되어도 못 놓아줌

// ✅ Application Context 사용
Singleton.context = activity.applicationContext
```

**관련**: [android-activity-lifecycle](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-activity-lifecycle.md)

---

### D
