---
title: apple-location-and-maps
tags: [apple, core-location, mapkit, framework, system-service]
aliases: [Location Services, Core Location, MapKit]
date created: 2026-04-09 10:57:00 +09:00
---

## [[apple-system-services]] > Core Location & MapKit

Apple 플랫폼에서 "사용자의 위치를 파악(Core Location)"하고, 그것을 "지도로 시각화(MapKit)"하는 두 기초 프레임워크를 바닥부터 심층적으로 다룹니다.

### 1. 🧭 Core Location: "Where am I?" (데이터와 로직)

**Core Location** 은 장치의 지리적 위치, 고도, 방향 또는 주변 비콘과의 거리를 결정하는 서비스를 제공합니다. 화면에 지도를 보여주는 기능은 없으며, 오직 '좌표'와 '상태' 데이터에 집중합니다.

#### 🛰️ 위치를 파악하는 원리
아이폰은 단순히 GPS만 쓰는 것이 아니라 여러 기술을 하이브리드로 사용합니다.
- **GPS**: 위성 신호 (탁 트인 실외에서 정확, 배터리 소모 높음)
- **Wi-Fi**: 주변 공유기 위치 데이터베이스 (실내에서 유용)
- **Cellular**: 기지국 신호 (정확도는 낮지만 가장 빠름)
- **Bluetooth (iBeacon)**: 아주 가까운 거리(매장 안 등)에서의 정밀 위치

#### 🛠️ 핵심 클래스: `CLLocationManager`
모든 위치 서비스의 컨트롤 타워입니다.
1. **역할**: 위치 업데이트 시작/종료, 권한 요청, 정확도 설정.
2. **Delegate (대리자) 패턴**: 위치가 바뀌면 "바뀌었다!"고 알려주는 함수들을 구현해야 합니다.

#### 🔐 보안 및 권한 (가장 중요)
사용자의 사생활과 직결되므로 iOS에서는 매우 엄격하게 관리합니다.
- **Info.plist**: 반드시 `NSLocationWhenInUseUsageDescription` 또는 `NSLocationAlwaysAndWhenInUseUsageDescription` 키를 추가하여 사용자에게 왜 위치가 필요한지 설명해야 합니다.
- **권한 종류**:
    - **Allow Once**: 이번 한 번만 허용.
    - **While In Use**: 앱을 쓰고 있을 때만.
    - **Always**: 앱이 백그라운드에 있을 때도 (배터리 알림이 뜰 수 있음).

---

### 2. 🗺️ MapKit: "Show me the map" (시각화)

**MapKit**은 앱 내에 눈에 보이는 지도를 넣고, 그 위에 핀을 꽂거나 경로를 그리는 UI 기능을 담당합니다.

#### 🖼️ 핵심 클래스: `MKMapView`
사용자가 보고 상호작용하는 지도 뷰 그 자체입니다.
- **지도 타입**: Standard(일반), Satellite(위성), Hybrid, MutedStandard(강조를 뺀 지도).
- **Region (영역)**: 지도가 어디를 얼마나 넓게 보여줄지 결정합니다 (중심 좌표 + 확대 배율).

#### 📍 핀 꽂기 (Annotations & Overlays)
- **Annotation**: 특정 지점을 표시하는 '핀'이나 '마커'. (예: 식당 위치)
- **Overlay**: 지도 위에 그리는 선이나 도형. (예: 조깅 경로, 구역 표시)

#### 🔍 주요 기능
- **Local Search**: "주변 카페" 같은 키워드로 장소 검색.
- **Directions**: 두 지점 사이의 경로(도보, 가상, 자동차) 계산.
- **Look Around**: 구글의 스트리트 뷰 같은 360도 거리 보기.

---

### 3. 🔗 두 프레임워크의 협업 방식

대부분의 앱은 다음과 같은 흐름으로 작동합니다.

```mermaid
graph LR
    A[Core Location] -- "내 좌표는 37.5, 127.0이야" --> B[App Logic]
    B -- "이 좌표를 중심으로 지도를 그려줘" --> C[MapKit]
    C -- "화면에 지도와 내 위치 표시" --> D[User UI]
```

---

### 🔋 배터리와 성능 최적화 (실무 포인트)

위치 서비스는 배터리를 많이 소모하는 주범입니다. 상황에 맞는 전략이 필요합니다.

1. **정확도 타협 (`desiredAccuracy`)**:
   - 내비게이션 앱: `kCLLocationAccuracyBest` (가장 정밀하지만 배터리 소모 극심)
   - 날씨 앱: `kCLLocationAccuracyThreeKilometers` (대략적인 위치만 필요, 배터리 절약)
2. **Significant Location Change Service**:
   - 기지국이 바뀔 때(약 500m~1km 이동)만 알려주는 모드입니다. 배터리 소모가 거의 없어 백그라운드 위치 추적에 최적입니다.
3. **Geofencing (Region Monitoring)**:
   - "집 반경 100m 안에 들어오면 알려줘"라고 시스템에 등록해두면, 앱을 완전히 꺼두어도 시스템이 감시하다가 조건이 맞을 때 앱을 깨워줍니다.

---

### 4. 🚀 실전 예시: 위경도로 핀 찍기

실제로 위도(latitude)와 경도(longitude) 값을 이용해 지도에 핀을 꽂는 가장 표준적인 코드 흐름입니다.

```swift
import MapKit

// 1. 위경도 좌표 정의 (예: 서울 시청)
let coordinate = CLLocationCoordinate2D(latitude: 37.5665, longitude: 126.9780)

// 2. 핀(Annotation) 객체 생성 및 설정
let annotation = MKPointAnnotation()
annotation.coordinate = coordinate
annotation.title = "서울 시청"
annotation.subtitle = "여기가 서울의 중심입니다"

// 3. 지도에 핀 추가
mapView.addAnnotation(annotation)

// 4. (선택) 핀이 잘 보이도록 지도를 해당 위치로 이동
let region = MKCoordinateRegion(center: coordinate,
                                latitudinalMeters: 500,
                                longitudinalMeters: 500)
mapView.setRegion(region, animated: true)
```

- **MKPointAnnotation**: 지도 위의 한 점을 나타내는 가장 기본적인 객체입니다.
- **setRegion**: 핀만 찍으면 지도가 엉뚱한 곳을 보고 있을 수 있으므로, 핀이 있는 곳을 카메라가 비추도록 범위를 설정해주는 것이 좋습니다.

---

### 📚 연관 문서
- [[apple-system-services]] - 다른 시스템 서비스 개요
- [[apple-privacy-and-tcc-details]] - 위치 권한과 관련된 개인정보 보호 체계
- [[apple-app-lifecycle-and-ui]] - 백그라운드에서의 앱 동작 방식
