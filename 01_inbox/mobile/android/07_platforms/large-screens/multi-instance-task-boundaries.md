---
title: multi-instance-task-boundaries
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## 데스크톱 멀티 인스턴스는 작업 단위와 데이터 소유권을 먼저 정해야 한다

상위 문서: [데스크톱 윈도잉과 멀티태스킹 계약](windowing-multitasking.md)

Multi-instance 지원은 같은 앱 창을 여러 개 띄우는 스위치를 켜는 문제가 아니다. 문서, 대화, 탭, 계정, 편집 세션 같은 작업 단위가 무엇인지와 동시에 열린 인스턴스들이 어떤 데이터를 공유하거나 격리하는지 먼저 정해야 한다.

### Manifest 선언 및 Intent Launch 메커니즘

```xml
<!-- AndroidManifest.xml -->
<application>
    <property
        android:name="android.window.PROPERTY_SUPPORTS_MULTI_INSTANCE_SYSTEM_UI"
        android:value="true" />
</application>
```

```kotlin
fun openDocumentInNewWindow(context: Context, documentId: String) {
    val intent = Intent(context, DocumentActivity::class.java).apply {
        action = Intent.ACTION_VIEW
        data = Uri.parse("content://com.example.app/documents/$documentId")
        flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_MULTIPLE_TASK
    }
    context.startActivity(intent)
}
```

### 실무 규칙

- 새 window 로 열 수 있는 사용자 과업을 명확히 정한다.
- 같은 항목을 두 인스턴스에서 편집할 때 충돌, 저장 순서, stale state 처리를 정의한다.
- singleton [viewmodel](../../02_app_framework/architecture/state-management/viewmodel.md), 전역 selection, shared mutable cache 가 여러 window 에서 섞이지 않는지 확인한다.
- drag-out 으로 새 인스턴스를 만드는 UX 는 원본 창과 새 창의 소유권 이전 규칙을 함께 설계한다.
- Android 15(API 35) 이상의 system UI multi-instance affordance 를 쓰려면 `PROPERTY_SUPPORTS_MULTI_INSTANCE_SYSTEM_UI` 와 task launch 동작을 함께 검증한다. 이 property 는 시스템 UI 에 New Window 같은 진입점을 요청할 뿐 데이터 격리나 올바른 task 생성을 구현하지 않는다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 실행 중인 동일 패키지 멀티 인스턴스 태스크 목록 확인
adb shell dumpsys activity tasks | grep -B 2 -A 5 "<package_name>"

# 태스크별 생성 Intent 플래그 (FLAG_ACTIVITY_MULTIPLE_TASK) 디버깅
adb shell dumpsys activity intents | grep -E "FLAG_ACTIVITY_MULTIPLE_TASK"
```

### 관련 문서

- [드래그 앤 드롭은 창 사이 데이터 이동 계약이다](drag-and-drop-cross-window.md)

공식 문서: [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing)

검증일: 2026-08-03. desktop 또는 multi-window 에서 새 task 는 새 window 로 열릴 수 있으므로 property, intent flags, back stack 을 함께 테스트한다.

