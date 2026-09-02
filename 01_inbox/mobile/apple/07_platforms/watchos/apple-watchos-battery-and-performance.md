---
title: apple-watchos-battery-and-performance
tags: [apple, apple/platforms, apple/platforms/watchos, performance, watchos]
aliases: ["watchOS Battery", "워치 배터리와 성능"]
date modified: 2026-08-10 18:45:00 +09:00
date created: 2025-12-18 16:21:20 +09:00
---

## watchOS Battery & Performance

애플워치에서 배터리를 최적화하고 성능을 유지하는 기법을 다룹니다. watchOS 는 **극한의 리소스 제약** 환경이며, 모든 설계 결정이 **배터리 수명**과 **반응성**에 영향을 미칩니다. 용어는 [apple-glossary](../../00_foundations/apple-glossary.md).

### 💡 왜 배터리 최적화가 필수인가?

- **하루 배터리 수명 보장**: 모든 watchOS 앱은 하루 사용을 목표. 1%의 최적화 실패도 누적되면 시간 단위로 줄어듭니다.
- **사용자 신뢰**: 배터리가 빨리 닳으면 사용자는 앱을 즉시 삭제합니다.
- **시스템 안정성**: 배터리 압박이 심하면 [Jetsam(강제 종료)](../../00_foundations/apple-glossary.md) 으로 앱이 죽을 수 있습니다.

---

### watchOS 리소스 제약 이해하기

#### 배터리와 전력 모델

Apple Watch Series 8/9 는 약 **300-350mAh** 배터리를 가집니다 (스마트폰의 1/20 이하). 하루를 견디려면 전력 소비를 엄격히 제어해야 합니다.

**전력 소비 순위** (상대값):
1. **Display** (가장 큼) - 화면 켜짐 = 배터리 급속 소모
2. **Cellular/WiFi** - 데이터 전송 (1초 셀룰러 = 60초 대기)
3. **GPS/센서** - 실시간 위치, 심박 센서
4. **CPU 계산** - 복잡한 알고리즘
5. **메모리** - 큰 데이터 보관 (상대적으로 적음)

```swift
import WatchKit
import Foundation

class BatteryOptimizationManager {
    // 1. 화면이 켜져 있는 동안만 집중 업데이트
    func enableScreenWakeUntilDismissed() {
        WKInterfaceDevice.current().enableWaterResistance()
        // 사용자가 손목을 올릴 때까지만 화면 활성화
    }
    
    // 2. 타이머 대신 Background Task 사용
    func scheduleBackgroundTask() {
        // 부정확하지만 배터리 효율적 (초 단위 아님, 분 단위)
        let backgroundTask = WKRefreshBackgroundTask {
            print("백그라운드 새로고침: 경제적")
            $0.setTaskCompletedWithSnapshot(false)
        }
    }
    
    // 3. 데이터 압축 + 배치 전송
    func optimizedNetworkRequest() {
        // 10개 작은 요청 대신 1개 큰 요청
        let compressedData = compress(largePayload: getData())
        sendToiPhone(compressedData) // 한 번에 전송
    }
}
```

#### 화면 스크린 타임

화면이 **몇 초만 켜져 있어도** 배터리가 눈에 띄게 줄어듭니다.

| 화면 상태 | 전력 소비 | 주의사항 |
| :--- | :--- | :--- |
| **화면 OFF (대기)** | 최소 (~10mW) | 가능하면 이 상태 유지 |
| **화면 ON, 정적** | 중간 (~100mW) | 손목 올림 시 순간적으로 증가 |
| **화면 ON, 애니메이션** | 높음 (~150mW+) | 피해야 할 패턴 |
| **Always-On Display** (시계 페이스) | 매우 높음 | 스타일에 따라 다름 |

**최적화 전략**:
- 화면 켜짐을 기반으로 **필수 정보만** 표시
- 복잡한 레이아웃/애니메이션 피하기
- Always-On Display 기능이 필요하면 스타일을 단순하게 (예: 숫자 시계 > 복잡한 그래픽)

---

### CPU와 작업 분배

#### 손목 올림 깨어남 최적화

Watch 는 **손목 올림** 순간에 잠에서 깼다가, **2~3초 후** 자동으로 잠들어 들어갑니다. 이 짧은 창 안에 모든 작업을 완료해야 합니다.

```swift
import SwiftUI
import WatchKit

struct QuickResponseView: View {
    @State var data: String = "..."
    @State var isLoading = false
    
    var body: some View {
        VStack {
            Text(data)
                .font(.headline)
            
            if isLoading {
                ProgressView()
            }
        }
        .onAppear {
            // 손목 올림 순간에 호출됨
            // 2~3초 내에 로컬 데이터 표시
            loadCachedData()
        }
    }
    
    func loadCachedData() {
        // 이전에 캐시해둔 데이터를 즉시 표시
        isLoading = true
        
        // ❌ 나쁜 예: 네트워크 요청 (3초 이상 소요)
        // URLSession.shared.dataTask(with: url).resume()
        
        // ✅ 좋은 예: 로컬 캐시에서 로드 (< 100ms)
        if let cached = loadFromDisk() {
            data = cached
            isLoading = false
            
            // 백그라운드에서 새 데이터를 가져와 업데이트
            DispatchQueue.global().async {
                fetchNewData()
            }
        }
    }
    
    func loadFromDisk() -> String? {
        // UserDefaults 또는 파일 읽기
        UserDefaults.standard.string(forKey: "cachedData")
    }
    
    func fetchNewData() {
        // 네트워크 요청: 결과가 오면 나중에 업데이트
    }
}
```

#### CPU 작업 분할 (Task Slicing)

오래 걸리는 연산을 **짧은 작업 조각(Slice)** 으로 나누고, 사이사이에 **휴식**을 줍니다.

```swift
import WatchKit

class DataProcessor {
    func processLargeDatasetOptimized(_ items: [Int]) {
        // ❌ 나쁜 예: 한 번에 처리 (배터리 급증, 멈춤)
        // let result = items.reduce(0) { $0 + expensiveCalculation($1) }
        
        // ✅ 좋은 예: 배치 단위로 처리
        let batchSize = 50
        var processedCount = 0
        
        DispatchQueue.global().async {
            for i in stride(from: 0, to: items.count, by: batchSize) {
                let batch = Array(items[i..<min(i + batchSize, items.count)])
                
                // 배치 처리
                let batchResult = batch.map { expensiveCalculation($0) }
                processedCount += batch.count
                
                // 10ms 휴식 (배터리 절약)
                usleep(10_000)
            }
        }
    }
    
    func expensiveCalculation(_ value: Int) -> Int {
        // CPU 집약적 작업
        return (value * value) % 1000
    }
}
```

#### 타이머와 폴링 최소화

**반복적인 타이머는 배터리를 심각하게 낭비합니다.** Watch는 2-3초마다 깨어나므로, 타이머는 실제 필요한 경우만 사용하세요.

```swift
import Foundation
import WatchKit

class TimerAlternatives {
    // ❌ 나쁜 예: 1초마다 업데이트 (배터리 낭비)
    var badTimer: Timer?
    
    func startBadTimer() {
        badTimer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { _ in
            print("1초마다 업데이트") // 배터리 낭비!
        }
    }
    
    // ✅ 좋은 예1: Background Refresh (권장)
    func scheduleBackgroundRefresh() {
        WKApplication.shared().scheduleBackgroundRefresh(
            withPreferredDate: Date(timeIntervalSinceNow: 900), // 15분 후
            completion: { error in
                if error == nil {
                    print("백그라운드 새로고침 예약됨")
                }
            }
        )
    }
    
    // ✅ 좋은 예2: Workout 세션 중 (허용됨)
    @State var workoutSession: HKWorkoutSession?
    
    func startWorkoutSession() {
        let config = HKWorkoutConfiguration()
        config.activityType = .running
        
        do {
            let session = try HKWorkoutSession(configuration: config)
            workoutSession = session
            // Workout 세션 중에는 더 자주 업데이트 가능
            print("Workout 중: 업데이트 빈도 증가 허용")
        } catch {
            print("Workout 세션 생성 실패")
        }
    }
}
```

---

### 네트워크 최적화

#### 직접 셀룰러 vs iPhone 프록시

Watch Series 8/9 중 셀룰러 모델은 LTE 를 통해 직접 네트워크 접속이 가능합니다. **하지만 셀룰러 통신은 매우 비싸므로** (배터리 + 데이터), 가능하면 **iPhone을 경유**하세요.

```swift
import WatchConnectivity
import Foundation

class NetworkOptimizer: NSObject, WCSessionDelegate {
    func session(_ session: WCSession, activationDidCompleteWith activationState: WCSessionActivationState, error: Error?) {
        // iPhone 연결 상태 확인
        if session.isReachable {
            print("iPhone 사용 가능: iPhone을 경유하여 요청")
            requestViaIPhone()
        } else {
            print("iPhone 연결 불가: 필요시에만 직접 셀룰러 사용")
            requestViaCellularAsLastResort()
        }
    }
    
    func requestViaIPhone() {
        // WCSession으로 iPhone에 데이터 요청
        WCSession.default.sendMessage(
            ["action": "fetchWeather"],
            replyHandler: { response in
                print("iPhone 응답 수신: \(response)")
            },
            errorHandler: { error in
                print("iPhone 요청 실패: \(error.localizedDescription)")
            }
        )
    }
    
    func requestViaCellularAsLastResort() {
        // URL 요청 (셀룰러)
        var request = URLRequest(url: URL(string: "https://api.example.com/data")!)
        request.timeoutInterval = 5 // 짧은 타임아웃 (배터리 절약)
        
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let data = data {
                print("셀룰러 데이터 수신")
            }
        }.resume()
    }
}

extension NetworkOptimizer {
    func sessionDidBecomeInactive(_ session: WCSession) { }
    func sessionDidDeactivate(_ session: WCSession) { }
}
```

#### 데이터 압축과 배치 처리

여러 개의 작은 요청을 **하나의 큰 요청**으로 합치고, **gzip 압축**을 사용하세요.

```swift
import Foundation
import zlib

class DataCompressionUtility {
    // 여러 데이터를 배치로 합친 후 압축 전송
    func sendBatchedCompressedData(_ items: [String]) {
        let jsonData = try! JSONSerialization.data(
            withJSONObject: ["items": items],
            options: []
        )
        
        // gzip 압축
        let compressed = try! compressData(jsonData)
        
        print("원본: \(jsonData.count) bytes → 압축: \(compressed.count) bytes")
        // 전송: compressed
    }
    
    func compressData(_ data: Data) throws -> Data {
        // 실제 구현은 zlib 또는 스위프트 압축 라이브러리 사용
        return data // 간단한 예시
    }
}
```

#### 재시도 전략과 오프라인 큐

네트워크 실패 시 **즉시 재시도하지 말고**, 지수 백오프(Exponential Backoff)를 사용하세요.

```swift
import Foundation

class RetryPolicy {
    func requestWithRetry(url: URL, maxRetries: Int = 3) {
        var attempt = 0
        
        func attemptRequest() {
            URLSession.shared.dataTask(with: url) { data, response, error in
                if let data = data {
                    print("성공")
                    return
                }
                
                attempt += 1
                if attempt < maxRetries {
                    // 지수 백오프: 1초, 2초, 4초...
                    let delaySeconds = pow(2.0, Double(attempt - 1))
                    print("재시도 대기: \(delaySeconds)초")
                    
                    DispatchQueue.main.asyncAfter(deadline: .now() + delaySeconds) {
                        attemptRequest()
                    }
                } else {
                    print("최대 재시도 횟수 초과. 오프라인 큐에 저장.")
                    saveToOfflineQueue(url: url)
                }
            }.resume()
        }
        
        attemptRequest()
    }
    
    func saveToOfflineQueue(url: URL) {
        // 실패한 요청을 로컬에 저장해 나중에 처리
        var queue = UserDefaults.standard.array(forKey: "failedRequests") as? [String] ?? []
        queue.append(url.absoluteString)
        UserDefaults.standard.set(queue, forKey: "failedRequests")
    }
}
```

---

### 화면과 렌더링 최적화

#### SwiftUI 복잡도 제어

복잡한 레이아웃과 긴 리스트는 Watch 성능을 심각하게 저하시킵니다.

```swift
import SwiftUI

struct WatchScreenOptimization: View {
    var body: some View {
        VStack {
            // ❌ 나쁜 예: 100개 항목 모두 렌더링
            // List(1...100, id: \.self) { i in
            //     Text("Item \(i)")
            // }
            
            // ✅ 좋은 예: 화면에 보이는 항목만 (3~4개)
            List(1...4, id: \.self) { i in
                Text("Item \(i)")
            }
            
            Button("더보기") {
                // 추가 항목 로드
            }
        }
    }
}

// TimelineView로 시계 페이스 업데이트 최적화
struct WatchFaceOptimized: View {
    var body: some View {
        TimelineView(.everyMinute) { context in
            // 매분 업데이트 (초 단위 X)
            Text(context.date.formatted(date: .omitted, time: .shortened))
                .font(.title2)
        }
    }
}
```

#### 이미지 최적화

이미지는 CPU 메모리의 큰 부분을 차지합니다. **작은 해상도**와 **캐싱**을 사용하세요.

```swift
import SwiftUI
import WatchKit

class ImageOptimizer {
    // 디바이스에 맞는 크기로 리사이징
    func optimizeImage(_ image: UIImage) -> UIImage {
        let scale = WKInterfaceDevice.current().screenScale
        let size = CGSize(width: 300 * scale, height: 300 * scale)
        
        UIGraphicsBeginImageContextWithOptions(size, false, scale)
        image.draw(in: CGRect(origin: .zero, size: size))
        let resized = UIGraphicsGetImageFromCurrentImageContext()!
        UIGraphicsEndImageContext()
        
        return resized
    }
    
    // 디스크 캐싱
    func cacheImage(_ image: UIImage, forKey key: String) {
        let cachesDir = FileManager.default.urls(for: .cachesDirectory, in: .userDomainMask)[0]
        let fileURL = cachesDir.appendingPathComponent("\(key).png")
        
        try? image.pngData()?.write(to: fileURL)
    }
    
    func cachedImage(forKey key: String) -> UIImage? {
        let cachesDir = FileManager.default.urls(for: .cachesDirectory, in: .userDomainMask)[0]
        let fileURL = cachesDir.appendingPathComponent("\(key).png")
        
        return UIImage(contentsOfFile: fileURL.path)
    }
}
```

#### 햅틱과 사운드 제어

애플워치는 **Taptic Engine** 으로 진동 피드백을 줍니다. 과다 사용은 배터리를 낭비하고 사용자를 불편하게 합니다.

```swift
import WatchKit

class HapticFeedback {
    func playNotificationFeedback() {
        // 알림 시: 진동 한 번
        WKInterfaceDevice.current().play(.notification)
    }
    
    func playSuccessFeedback() {
        // 성공: 2번 짧은 진동
        WKInterfaceDevice.current().play(.success)
    }
    
    // ❌ 나쁜 예: 과도한 진동
    func avoidExcessiveHaptics() {
        // DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
        //     WKInterfaceDevice.current().play(.notification)
        // } // 반복 금지
    }
}
```

---

### 센서와 위치 서비스

#### GPS 최적화

GPS는 **가장 전력을 많이 소비**하는 센서입니다 (1초 = 배터리의 1%). 꼭 필요한 경우만 사용하세요.

```swift
import CoreLocation
import WatchKit

class LocationManager: NSObject, CLLocationManagerDelegate {
    let locationManager = CLLocationManager()
    
    override init() {
        super.init()
        locationManager.delegate = self
    }
    
    // ❌ 나쁜 예: 백그라운드에서 계속 GPS 추적
    func startContinuousTracking() {
        locationManager.startUpdatingLocation()
        // 배터리 빠르게 소진!
    }
    
    // ✅ 좋은 예: Workout 세션 중에만 GPS 사용
    func startWorkoutWithGPS() {
        // HKWorkoutSession 내에서만 GPS 허용
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
        // Workout 종료 시 자동 정지
    }
    
    // ✅ 더 좋은 예: 샘플링 간격 조절
    func startOptimizedTracking() {
        locationManager.desiredAccuracy = kCLLocationAccuracyHundredMeters // 낮은 정확도
        locationManager.distanceFilter = 50 // 50m 이상 이동할 때만 업데이트
        locationManager.startUpdatingLocation()
    }
}
```

#### HealthKit 샘플링 제어

실시간 심박(HR), 산소 포화도(SpO2) 등을 요청하면 센서가 계속 켜져 배터리를 낭비합니다.

```swift
import HealthKit

class HealthOptimizer {
    let store = HKHealthStore()
    
    // ❌ 나쁜 예: 높은 빈도로 심박 샘플 요청
    func requestHeartRateContiously() {
        // 매초 업데이트? 배터리 낭비
    }
    
    // ✅ 좋은 예: Workout 세션 중에만 요청
    func queryHeartRateDuringWorkout() {
        let heartRateType = HKQuantityType.quantityType(
            forIdentifier: .heartRate
        )!
        
        let predicate = HKQuery.predicateForSamples(
            withStart: Date(timeIntervalSinceNow: -300), // 최근 5분
            end: Date(),
            options: .strictStartDate
        )
        
        let query = HKSampleQuery(
            sampleType: heartRateType,
            predicate: predicate,
            limit: 1, // 최신 1개만
            sortDescriptors: [
                NSSortDescriptor(key: HKSampleSortIdentifierStartDate, ascending: false)
            ]
        ) { query, samples, error in
            if let sample = samples?.first as? HKQuantitySample {
                let heartRate = sample.quantity.doubleValue(for: HKUnit(from: "count/min"))
                print("현재 심박: \(heartRate)")
            }
        }
        
        store.execute(query)
    }
}
```

---

### 메모리 관리

Watch는 **약 512MB~1GB** 메모리만 가집니다. 큰 이미지 배열, 모델, 데이터를 메모리에 보관하면 **Jetsam** 으로 앱이 강제 종료됩니다.

```swift
import WatchKit

class MemoryOptimization {
    // ❌ 나쁜 예: 모든 이미지를 메모리에 로드
    var allImages: [UIImage] = []
    
    // ✅ 좋은 예: 필요한 것만 로드 + 즉시 해제
    func loadImageOptimized(at index: Int) -> UIImage? {
        // 디스크에서 로드
        let cachesDir = FileManager.default.urls(for: .cachesDirectory, in: .userDomainMask)[0]
        let fileURL = cachesDir.appendingPathComponent("image_\(index).png")
        
        let image = UIImage(contentsOfFile: fileURL.path)
        // 사용 후 autorelease pool이 자동으로 해제
        return image
    }
    
    // 메모리 프로파일링
    func monitorMemoryUsage() {
        var info = malloc_statistics_t()
        malloc_zone_statistics(nil, &info)
        let usedMemory = Double(info.size_in_use) / 1024 / 1024 // MB
        print("현재 메모리 사용: \(usedMemory)MB")
        
        // 500MB 초과 시 경고
        if usedMemory > 500 {
            print("⚠️ 메모리 부족 경고! 데이터 정리 필요")
        }
    }
}
```

---

### 테스트와 모니터링

#### Jetsam 로그 읽기

Watch 앱이 의도치 않게 종료되는 주된 원인은 **Jetsam (메모리 부족)** 입니다.

```
// Jetsam 이벤트 로그 위치:
// Xcode → Device & Simulators → Watch Simulator → Logs
// 또는 /var/log/system.log
```

#### 배터리 소모 프로파일링

Xcode의 Energy Impact 도구로 실시간 배터리 영향을 측정하세요.

```swift
import OSLog

class BatteryProfiler {
    let logger = Logger(subsystem: "com.example.watchapp", category: "battery")
    
    func logEnergyIntensiveOperation() {
        logger.log("배터리 집약적 작업 시작")
        
        // 작업 수행
        let startTime = Date()
        performExpensiveCalculation()
        let elapsed = Date().timeIntervalSince(startTime)
        
        logger.log("작업 완료: \(elapsed)초 소요")
    }
    
    func performExpensiveCalculation() {
        // 실제 작업
    }
}
```

---

### 최적화 체크리스트

```
배터리:
- [ ] 앱이 대기 중일 때 배터리가 눈에 띄게 줄어드는가?
- [ ] Background Refresh 빈도를 필요 최소한으로 설정했는가?
- [ ] 타이머 폴링 대신 허용된 모드(Background Task/Push)를 사용하는가?

네트워크:
- [ ] iPhone 연결 여부를 확인하고 우선하는가?
- [ ] 데이터를 압축하고 배치 전송하는가?
- [ ] 재시도 정책이 지수 백오프를 사용하는가?

화면:
- [ ] 리스트 항목이 10개 이하로 유지되는가?
- [ ] 복잡한 애니메이션/이펙트를 피했는가?
- [ ] 이미지를 작은 해상도로 캐싱하는가?

센서:
- [ ] GPS는 Workout 세션 중에만 사용하는가?
- [ ] HealthKit 샘플링 빈도를 필요 최소한으로 설정했는가?

메모리:
- [ ] Jetsam 로그를 확인했는가?
- [ ] 큰 배열/이미지를 메모리에 보관하지 않는가?
- [ ] 사용 후 리소스를 즉시 해제하는가?

사용자 경험:
- [ ] 로딩 중에도 캐시된 데이터를 먼저 표시하는가?
- [ ] 알림/컴플리케이션 업데이트 빈도를 제한하는가?
- [ ] 배터리 부족 시 기능을 축소하거나 안내하는가?
```

---

### 관련 링크

[apple-watchos-system](../apple-watchos-system.md), [apple-watchos-fitness-guide](apple-watchos-fitness-guide.md), [apple-offline-and-resilience](../../03_data_networking/apple-offline-and-resilience.md), [apple-performance-and-debug](../../06_testing_performance/apple-performance-and-debug.md).
