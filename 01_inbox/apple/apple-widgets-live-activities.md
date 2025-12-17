---
title: apple-widgets-live-activities
tags: [apple, widgets, widgetkit, live-activities, dynamic-island]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Widgets & Live Activities apple widgets widgetkit live-activities

WidgetKit 과 Live Activities. 기본은 [[apple-app-lifecycle-and-ui]] 참고.

### Widget 기본

```swift
import WidgetKit
import SwiftUI

struct SimpleWidget: Widget {
    let kind: String = "SimpleWidget"
    
    var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind, provider: Provider()) { entry in
            SimpleWidgetView(entry: entry)
        }
        .configurationDisplayName("My Widget")
        .description("This is a simple widget")
        .supportedFamilies([.systemSmall, .systemMedium, .systemLarge])
    }
}

struct Provider: TimelineProvider {
    func placeholder(in context: Context) -> SimpleEntry {
        SimpleEntry(date: Date(), text: "Placeholder")
    }
    
    func getSnapshot(in context: Context, completion: @escaping (SimpleEntry) -> Void) {
        let entry = SimpleEntry(date: Date(), text: "Snapshot")
        completion(entry)
    }
    
    func getTimeline(in context: Context, completion: @escaping (Timeline<SimpleEntry>) -> Void) {
        var entries: [SimpleEntry] = []
        
        let currentDate = Date()
        for hourOffset in 0..<5 {
            let entryDate = Calendar.current.date(byAdding: .hour, value: hourOffset, to: currentDate)!
            let entry = SimpleEntry(date: entryDate, text: "Hour \(hourOffset)")
            entries.append(entry)
        }
        
        let timeline = Timeline(entries: entries, policy: .atEnd)
        completion(timeline)
    }
}

struct SimpleEntry: TimelineEntry {
    let date: Date
    let text: String
}

struct SimpleWidgetView: View {
    var entry: Provider.Entry
    
    var body: some View {
        VStack {
            Text(entry.date, style: .time)
            Text(entry.text)
        }
    }
}
```

### Live Activities

```swift
import ActivityKit

struct DeliveryAttributes: ActivityAttributes {
    public struct ContentState: Codable, Hashable {
        var status: String
        var estimatedTime: Date
    }
    
    var orderNumber: String
}

// 시작
func startLiveActivity() {
    let attributes = DeliveryAttributes(orderNumber: "12345")
    let initialState = DeliveryAttributes.ContentState(
        status: "준비 중",
        estimatedTime: Date().addingTimeInterval(1800)
    )
    
    do {
        let activity = try Activity<DeliveryAttributes>.request(
            attributes: attributes,
            contentState: initialState,
            pushType: nil
        )
        print("Live Activity started: \(activity.id)")
    } catch {
        print("Failed to start Live Activity: \(error)")
    }
}

// 업데이트
func updateLiveActivity(activity: Activity<DeliveryAttributes>) {
    Task {
        let newState = DeliveryAttributes.ContentState(
            status: "배달 중",
            estimatedTime: Date().addingTimeInterval(900)
        )
        
        await activity.update(using: newState)
    }
}

// 종료
func endLiveActivity(activity: Activity<DeliveryAttributes>) {
    Task {
        await activity.end(dismissalPolicy: .immediate)
    }
}
```

### 더 보기

[[apple-swiftui-deep-dive]], [[apple-app-lifecycle-and-ui]], [[ios/apple-ios-advanced-capabilities]]
