---
title: android-desktop-windowing-and-multitasking
tags: [android, android/16, desktop-windowing, multitasking, tablets, foldables]
aliases: [Desktop Mode, Desktop Windowing, Android Multitasking]
date modified: 2026-04-04 00:33:00 +09:00
date created: 2026-04-04 00:33:00 +09:00
---

## Android 16: Desktop Windowing & Multitasking

Android 16(Baklava)은 태블릿 및 대화면 기기(폴더블 포함)를 위한 **Desktop Windowing** 기능을 정식으로 도입했다. 이는 기존의 분할 화면(Split Screen)이나 팝업 모드를 넘어, 윈도우나 맥과 같은 자유로운 창 관리 환경을 제공한다.

> [!NOTE] **iOS 비교: Stage Manager vs Desktop Windowing**
> - **iOS/iPadOS**: `Stage Manager`를 통해 창을 그룹화하고 크기를 조절한다. 애플은 하드웨어와 소프트웨어의 통제력을 바탕으로 정형화된 창 전환 경험을 제공한다. (iOS 26+)
> - **Android**: `Desktop Windowing`을 통해 보다 자유로운 창 배치와 크기 조절을 지원한다. 또한 안드로이드 16부터는 앱이 화면 방향(Orientation)을 강제하는 것을 시스템 수준에서 무시하고 강제로 창 모드로 구동할 수 있다.
> 자세한 내용은 [apple-ipados-multitasking](../../apple/04_system_services/apple-ipados-multitasking.md)를 참고하세요.

### 1. 데스크탑 윈도잉(Desktop Windowing) 대응

안드로이드 16 기기에서 사용자는 모든 앱을 창 모드로 전환할 수 있다. 이제 모든 앱은 **가변적인 화면 크기(Resizability)**를 완벽하게 지원해야 한다.

#### 매니페스트 설정 및 처리

```xml
<activity
    android:name=".MainActivity"
    android:resizeableActivity="true"
    android:configChanges="screenSize|smallestScreenSize|screenLayout|orientation">
    <!-- 창 크기 변화 시 Activity가 재시작되지 않도록 설정 -->
</activity>
```

### 2. 적응형 레이아웃 (Adaptive Layouts)

단일 레이아웃이 아닌, 창 크기에 따라 배치가 변하는 적응형 UI가 필수적이다.
- **Window Size Classes**: `Compact`, `Medium`, `Expanded` 클래스에 맞게 UI를 분기한다.
- **Compose Adaptive**: `ListDetailPaneScaffold`나 `SupportingPaneScaffold` 같은 라이브러리를 사용하여 창 크기에 맞는 화면 구성을 자동화한다.

### 3. 멀티 인스턴스 (Multi-instance)

생산성 향상을 위해 한 앱의 창을 여러 개 띄우는 기능이 중요하다. (예: 브라우저 탭, 메모장 여러 개)

```kotlin
val intent = Intent(this, MainActivity::class.java).apply {
    addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_MULTIPLE_TASK)
}
startActivity(intent)
```

---

### 🏛️ 생산성 향상을 위한 보조 기능

- **Taskbar Overflow**: 활성화된 창이 많을 때 태스크바에서 쉽게 관리할 수 있는 메뉴 제공.
- **Drag & Drop**: 앱 간의 데이터 이동은 이제 멀티태스킹의 핵심 요소이다.
- **Keyboard Shortcuts**: 물리 키보드 연결 시 `Alt + Tab` 등의 단축키 지원.

> [!TIP] **Devil's Advocate : 고정된 레이아웃은 이제 구시대의 유물이다**
> 안드로이드 16은 개발자가 선언한 `screenOrientation="portrait"`를 무시하고 강제로 가로 창 모드로 띄울 수 있다. 이제 특정 방향에 고정된 앱이란 존재할 수 없으며, 어떤 화면 비율에서도 동작하는 **유연한 UI 아키텍처**만이 살아남을 것이다.

### 더 보기
- [android-ui-system](android-ui-system.md) - 기본 UI 시스템과 적응형 레이아웃
- [android-large-screens](android-large-screens.md) - 태블릿 및 폴더블 최적화
- [android-appfunctions-and-ai-agents](android-appfunctions-and-ai-agents.md) - 에이전트 기반의 창 제어
