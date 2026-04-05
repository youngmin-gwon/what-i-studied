---
title: apple-background-tasks
tags: [apple, background, battery, ios, multitasking, system]
aliases: []
date modified: 2026-04-05 17:45:08 +09:00
date created: 2025-12-16 16:50:00 +09:00
---

## Background Tasks Deep Dive

iOS 의 앱 생명주기는 데스크톱이나 안드로이드와 다릅니다.

홈 화면으로 나가는 순간 앱은 **얼음(Suspended)**이 됩니다. 이를 깨고 작업을 수행하려면 시스템의 허락(Budget)이 필요합니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **배터리 수명**: 사용자가 가장 민감해하는 부분입니다. 백그라운드에서 CPU 를 계속 쓰면 폰이 뜨거워지고 배터리가 광탈합니다. Apple 이 백그라운드 정책을 엄격하게 잡는 이유입니다.
- **예측 불가성**: "왜 내 앱은 백그라운드 작업이 안 돌죠?" -> 시스템이 판단하기에 사용자가 이 앱을 잘 안 쓰거나, 배터리가 부족하면 실행 기회를 주지 않기 때문입니다.
- **Jetsam**: 메모리가 부족하면 백그라운드 앱부터 죽입니다. 작업을 하다가 갑자기 죽을 수 있음을 방어적으로 코딩해야 합니다.

---

### 🛑 주요 백그라운드 모드 (Limits & Capabilities)

Capability 탭에서 설정하는 전통적인 방식들입니다. 엄격한 심사 대상입니다.

| 모드 | 용도 | 특징 |
|------|------|------|
| **Audio** | 음악 재생, PiP | 계속 실행됩니다. 단, 소리가 멈추면(일시정지) 10 초 뒤 suspend 될 수 있습니다. |
| **Location** | 내비게이션, 트래킹 | 배터리 소모가 큽니다. `allowsBackgroundLocationUpdates` 가 꺼져있으면 백그라운드 진입 시 위치 업데이트가 멈춥니다. |
| **VoIP** | 인터넷 전화 | `PushKit` 사용. 전화가 오면 앱을 깨웁니다. 일반 푸시와 달리 **반드시** CallKit UI 를 띄워야 합니다 (악용 방지). |
| **Remote Notification** | Silent Push | 사용자에게 알리지 않고 데이터를 갱신합니다. 시간당 전송 횟수 제한(Throttling)이 있습니다. |

---

### 🆕 BGTaskScheduler (Modern Background Tasks)

iOS 13+ 부터 권장되는 "예약(Schedule)" 방식입니다.

"지금 당장 실행해줘"가 아니라, "**이따가 충전 중이고 와이파이 연결되면** 실행해줘"라고 시스템에 부탁하는 것입니다.

#### 1. BGAppRefreshTask (짧은 작업)
- **목적**: 사용자가 앱을 켰을 때 최신 정보를 보여주기 위함 (스냅샷 갱신).
- **제약**: 약 30 초의 실행 시간.
- **빈도**: 사용 패턴 머신러닝에 따라 다름. 자주 쓰는 앱일수록 자주 실행됨.

#### 2. BGProcessingTask (긴 작업)
- **목적**: 사진 백업, ML 모델 학습, DB 정리 등.
- **조건**: 주로 배터리 충전 중(Power connected) + 화면 꺼짐(Screen off) 상태일 때 실행됩니다.
- **시간**: 수 분 ~ 수십 분까지 가능하지만, 사용자가 폰을 다시 쓰기 시작하면 중단될 수 있습니다.

#### 구현 패턴 (Best Practices)

1. **Info.plist 등록**: `BGTaskSchedulerPermittedIdentifiers` 에 태스크 ID 를 추가해야 합니다.
2. **등록 (Register)**: `application(_:didFinishLaunchingWithOptions:)` 시점에 **반드시** 등록해야 합니다. 앱이 백그라운드에서 깨어날 때, 이 등록 정보를 보고 핸들러를 찾기 때문입니다.

```swift
// UIKit (AppDelegate) 방식
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    BGTaskScheduler.shared.register(forTaskWithIdentifier: "com.example.db_cleanup", using: nil) { task in
        self.handleProcessingTask(task: task as! BGProcessingTask)
    }
    return true
}
```

>[!TIP] **SwiftUI App Lifecycle 에서의 등록**
>SwiftUI `App` 프로토콜을 사용하는 경우, `init()` 에서 동일하게 등록합니다:
> ```swift
> @main struct MyApp: App {
>     init() {
>         BGTaskScheduler.shared.register(forTaskWithIdentifier: "com.example.db_cleanup", using: nil) { task in ... }
>     }
>     var body: some Scene { WindowGroup { ContentView() } }
> }
> ```

func scheduleProcessing() {

    let request = BGProcessingTaskRequest(identifier: "com.example.db_cleanup")

    request.requiresNetworkConnectivity = false

    request.requiresExternalPower = true // 충전 중에만

    
    do {
        try BGTaskScheduler.shared.submit(request)
    } catch {
        print("스케줄링 실패: \(error)") // 주로 10개 제한 초과 시 발생
    }

}

func handleProcessingTask(task: BGProcessingTask) {

    // 1. 만료 핸들러: 시스템이 "이제 그만 해"라고 할 때 호출됨

    task.expirationHandler = {

        // 하던 저장 작업 취소 및 정리

    }

    
    // 2. 작업 수행
    heavyJob.run { success in
        // 3. 완료 보고
        task.setTaskCompleted(success: success)
    }

}

```

---

### 🧠 Debugging Strategies

시뮬레이터나 실기기나 백그라운드 작업은 "언제 실행될지 모른다"는 게 문제입니다. 디버그를 위해 강제로 실행해야 합니다.

1. 앱 실행 후 홈 화면으로 이동(백그라운드 진입).
2. Xcode 디버거 일시 정지(Pause).
3. 콘솔에 명령어 입력:
   `e -l objc -- (void)[[BGTaskScheduler sharedScheduler] _simulateLaunchForTaskWithIdentifier:@"com.example.db_cleanup"]`
4. 디버거 재개(Resume) -> 즉시 태스크 실행됨.

### 더 보기
- [apple-uikit-lifecycle](../02_ui_frameworks/apple-uikit-lifecycle.md) - 앱이 백그라운드로 가는 시점
- [apple-networking-and-cloud](../03_data_networking/apple-networking-and-cloud.md) - Background URLSession 과의 차이 (파일 다운로드는 URLSession 이 더 유리함)
