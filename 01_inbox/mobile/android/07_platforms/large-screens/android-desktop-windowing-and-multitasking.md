---
title: android-desktop-windowing-and-multitasking
tags: []
aliases: []
date modified: 2026-04-05 17:43:05 +09:00
date created: 2026-04-04 00:34:25 +09:00
---

## [[mobile-security]] > [[android-desktop-windowing-and-multitasking]]

### Desktop Windowing: Multitasking Evolution

안드로이드 16(Baklava)에서 정식 도입된 **Desktop Windowing**과 한 차원 높은 멀티태스킹 환경을 위한 시스템 설계 기법을 분석합니다.

단순히 분할 화면(Split Screen)을 넘어, 자유로운 창 크기 조절과 위치 이동이 가능한 환경에서 앱이 어떻게 반응하고 리소스를 관리해야 하는지 이해하는 것이 목표입니다.

---

#### 💡 Context: 진정한 데스크톱 경험의 구현

태블릿과 폴더블 기기의 생산성을 극대화하기 위해 안드로이드는 윈도우/맥과 유사한 창 관리 시스템으로 진화하고 있습니다. 이제 모든 앱은 특정 화면 방향에 고정되지 않고, 가변적인 윈도우 환경에서도 완벽하게 동작하는 유연한 아키텍처를 갖춰야 합니다.

>[!NOTE] **상호 참조**
>iPadOS 의 스테이지 매니저 및 멀티태스킹 방식은 [[apple-ipados-productivity-deep]] 을 참고하세요.

---

#### 1. 데스크탑 윈도잉(Desktop Windowing) 대응

안드로이드 16 기기에서 사용자는 모든 앱을 창 모드로 전환할 수 있다. 이제 모든 앱은 **가변적인 화면 크기(Resizability)**를 완벽하게 지원해야 한다.

##### 매니페스트 설정 및 처리

```xml
<activity
    android:name=".MainActivity"
    android:resizeableActivity="true"
    android:configChanges="screenSize|smallestScreenSize|screenLayout|orientation">
    <!-- 창 크기 변화 시 Activity가 재시작되지 않도록 설정 -->
</activity>
```

#### 2. 적응형 레이아웃 (Adaptive Layouts)

단일 레이아웃이 아닌, 창 크기에 따라 배치가 변하는 적응형 UI 가 필수적이다.

- **Window Size Classes**: `Compact`, `Medium`, `Expanded` 클래스에 맞게 UI 를 분기한다.
- **Compose Adaptive**: `ListDetailPaneScaffold` 나 `SupportingPaneScaffold` 같은 라이브러리를 사용하여 창 크기에 맞는 화면 구성을 자동화한다.

#### 3. 멀티 인스턴스 (Multi-instance)

생산성 향상을 위해 한 앱의 창을 여러 개 띄우는 기능이 중요하다. (예: 브라우저 탭, 메모장 여러 개)

```kotlin
val intent = Intent(this, MainActivity::class.java).apply {
    addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_MULTIPLE_TASK)
}
startActivity(intent)
```

---

#### 🏛️ 생산성 향상을 위한 보조 기능

- **Taskbar Overflow**: 활성화된 창이 많을 때 태스크바에서 쉽게 관리할 수 있는 메뉴 제공.
- **Drag & Drop**: 앱 간의 데이터 이동은 이제 멀티태스킹의 핵심 요소이다.
- **Keyboard Shortcuts**: 물리 키보드 연결 시 `Alt + Tab` 등의 단축키 지원.

>[!TIP] **Devil's Advocate : 고정된 레이아웃은 이제 구시대의 유물이다**
>안드로이드 16 은 개발자가 선언한 `screenOrientation="portrait"` 를 무시하고 강제로 가로 창 모드로 띄울 수 있다. 이제 특정 방향에 고정된 앱이란 존재할 수 없으며, 어떤 화면 비율에서도 동작하는 **유연한 UI 아키텍처**만이 살아남을 것이다.

#### See Also

- [[android-ui-system]] - 기본 UI 시스템과 적응형 레이아웃
- [[android-large-screens]] - 태블릿 및 폴더블 최적화
- [[android-appfunctions-and-ai-agents]] - 에이전트 기반의 창 제어
