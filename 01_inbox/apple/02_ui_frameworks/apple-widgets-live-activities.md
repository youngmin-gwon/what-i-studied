---
title: apple-widgets-live-activities
tags: [apple, widgets, widgetkit, live-activities, dynamic-island]
aliases: []
date modified: 2025-12-17 20:00:00 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Widgets & Live Activities Deep Dive

앱에 들어오지 않아도 중요한 정보를 가장 빠르게 확인할 수 있는 창구입니다.
홈 화면의 **위젯(Widgets)**과 잠금 화면/다이내믹 아일랜드의 **실시간 현황(Live Activities)**은 앱의 재방문율을 높이는 핵심 기능입니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Snapshot Limitation**: 위젯은 "미니 앱"이 아닙니다. 매초 움직이거나 복잡한 애니메이션을 넣으려다 실패하는 경우가 많습니다. 위젯은 **"미리 그려진 그림(Snapshot)"**을 시간표(Timeline)에 맞춰 갈아끼우는 방식임을 이해해야 합니다.
- **Dynamic Island**: 아이폰 14 Pro 이후, 화면 상단의 펀치홀 영역이 정보 창으로 변했습니다. 이곳을 점유하지 못하면 사용자 경험에서 밀려납니다.
- **실시간성**: 배달 현황, 스포츠 점수처럼 "지금 당장" 변하는 정보는 위젯(갱신 주기 15분+)으로는 불가능합니다. 이때 Live Activity가 필요합니다.

---

### 🧩 WidgetKit Internals

위젯은 앱 프로세스와 별개로 동작하는 **App Extension**입니다.

#### 1. Snapshot-based Rendering
- 위젯 확장이 뷰를 렌더링하면, 시스템은 이를 **직렬화된 파일(Archived View)**로 저장해둡니다.
- 홈 화면에 표시될 때는 앱 실행 없이 이 파일을 보여주기만 합니다. 그래서 배터리 효율이 극도로 좋습니다.
- **제약**: 동영상 재생, 커스텀 제스처(스크롤, 드래그)가 불가능합니다 (단, iOS 17부터 버튼 인터랙션 일부 허용).

#### 2. Timeline Provider
"미래의 뷰"를 미리 그려서 시스템에 제출합니다.

```swift
func getTimeline(in context: Context, completion: @escaping (Timeline<SimpleEntry>) -> Void) {
    var entries: [SimpleEntry] = []
    
    // 현재부터 1시간 뒤까지 5개의 뷰를 미리 생성
    for hourOffset in 0..<5 {
        let entryDate = Calendar.current.date(byAdding: .hour, value: hourOffset, to: Date())!
        let entry = SimpleEntry(date: entryDate, text: "Hour \(hourOffset)")
        entries.append(entry)
    }
    
    // 타임라인 제출 (.atEnd: 다 보여주면 다시 요청해라)
    let timeline = Timeline(entries: entries, policy: .atEnd)
    completion(timeline)
}
```

---

### 🏝️ Live Activities (실시간 현황)

단기적인 실시간 이벤트(최대 8~12시간)를 추적합니다. (예: 택시 호출, 운동 기록, 타이머)

#### 1. 구조
- **Dynamic Island**: Compact(작게), Minimal(더 작게), Expanded(길게 누름) 3가지 모드를 디자인해야 합니다.
- **Lock Screen**: 잠금 화면 하단에 배너 형태로 표시됩니다.

#### 2. 업데이트 메커니즘
Live Activity는 `Timeline`을 쓰지 않습니다. **Push Notification**이나 앱 내부(`ActivityKit`)에서 즉시 업데이트합니다.
- **Push Token**: 각 액티비티마다 고유의 푸시 토큰이 발급됩니다. 서버는 이 토큰으로 JSON 페이로드를 보내 UI를 갱신합니다.

```swift
// 앱 내부에서 업데이트 (앱이 켜져 있거나 백그라운드 동작 중일 때)
func updateLiveActivity(activity: Activity<DeliveryAttributes>) {
    Task {
        let newState = DeliveryAttributes.ContentState(
            status: "배달 중",
            estimatedTime: Date().addingTimeInterval(900)
        )
        
        // 즉시 반영
        await activity.update(using: newState)
    }
}
```

#### 3. Push Frequency
Live Activity 푸시는 일반 푸시보다 우선순위가 높습니다(High Priority). 하지만 너무 자주 보내면 시스템이 과부하(Throttling)를 걸 수 있습니다. (권장: 정말 상태가 변했을 때만)

### 📚 더 보기
- [apple-app-lifecycle-and-ui](apple-app-lifecycle-and-ui.md) - Extension의 생명주기
- [apple-swiftui-deep-dive](apple-swiftui-deep-dive.md) - 위젯 UI는 100% SwiftUI
