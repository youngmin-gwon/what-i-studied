---
title: apple-app-tracking-privacy
tags: [apple, privacy, att, tracking, permissions]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## App Tracking & Privacy apple privacy att tracking permissions

App Tracking Transparency 와 프라이버시. 기본은 [[apple-sandbox-and-security]] 참고.

### App Tracking Transparency (ATT)

```swift
import AppTrackingTransparency

func requestTrackingPermission() {
    if #available(iOS 14, *) {
        ATTrackingManager.requestTrackingAuthorization { status in
            switch status {
            case .authorized:
                print("Tracking authorized")
            case .denied:
                print("Tracking denied")
            case .notDetermined:
                print("Not determined")
            case .restricted:
                print("Restricted")
            @unknown default:
                break
            }
        }
    }
}
```

### Info.plist 설정

```xml
<key>NSUserTrackingUsageDescription</key>
<string>맞춤형 광고를 제공하기 위해 추적 권한이 필요합니다</string>
```

### 위치 권한

```swift
import CoreLocation

class LocationManager: NSObject, CLLocationManagerDelegate {
    let manager = CLLocationManager()
    
    func requestPermission() {
        manager.delegate = self
        
        // When In Use
        manager.requestWhenInUseAuthorization()
        
        // Always (백그라운드)
        // manager.requestAlwaysAuthorization()
    }
    
    func locationManagerDidChangeAuthorization(_ manager: CLLocationManager) {
        switch manager.authorizationStatus {
        case .authorizedWhenInUse:
            print("When In Use authorized")
        case .authorizedAlways:
            print("Always authorized")
        case .denied:
            print("Denied")
        case .notDetermined:
            print("Not determined")
        case .restricted:
            print("Restricted")
        @unknown default:
            break
        }
    }
}
```

### 사진 라이브러리 권한

```swift
import Photos

func requestPhotoLibraryPermission() {
    PHPhotoLibrary.requestAuthorization(for: .readWrite) { status in
        switch status {
        case .authorized:
            print("Full access")
        case .limited:
            print("Limited access")
        case .denied:
            print("Denied")
        case .notDetermined:
            print("Not determined")
        case .restricted:
            print("Restricted")
        @unknown default:
            break
        }
    }
}
```

### 더 보기

[[apple-sandbox-and-security]], [[apple-keychain-biometrics]], [[common-security/apple-privacy-and-tcc-details]]
