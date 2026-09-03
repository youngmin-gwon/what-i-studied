---
title: mapkit-renders-what-core-location-provides
tags: [apple, apple/services, apple/services/location, mapkit, ui]
aliases: ["MapKit 은 그리기만 하고 위치 확보는 Core Location 이 한다", "MKMapView", "Map"]
date modified: 2026-09-03 00:00:00 +09:00
date created: 2026-09-03 00:00:00 +09:00
---

## MapKit 은 그리기만 하고 위치 확보는 Core Location 이 한다

### 개념 (What)

두 프레임워크의 책임이 완전히 분리되어 있다.

| | Core Location | MapKit |
| :--- | :--- | :--- |
| 역할 | **좌표와 상태를 얻는다** | **화면에 그린다** |
| 권한 | 필요 (TCC) | 지도 표시 자체는 불필요 |
| 배터리 | **여기서 결정된다** | 렌더링 비용만 |
| 실패 지점 | 권한·정확도·신호 | 렌더링 성능 |

**"위치가 안 나온다"는 거의 항상 Core Location 문제이고, "지도가 느리다"는 MapKit 문제다.** 이 구분이 진단의 첫 단계다.

### 왜 필요한가 (Why)

지도를 띄우는 것만으로는 권한이 필요 없다. 사용자 위치를 파란 점으로 표시하려는 순간 [Core Location 권한](authorization-and-accuracy-are-independent-axes.md)이 필요해진다.

```swift
// 지도만 — 권한 불필요
Map(position: $cameraPosition)

// 사용자 위치 표시 — 권한 필요
Map(position: $cameraPosition) {
    UserAnnotation()          // 여기서부터 Core Location 권한이 요구된다
}
```

### SwiftUI Map (iOS 17+)

```swift
@State private var camera: MapCameraPosition = .automatic

Map(position: $camera) {
    // 마커
    Marker("서울역", coordinate: stationCoord)

    // 커스텀 뷰
    Annotation("내 장소", coordinate: coord) {
        Image(systemName: "star.fill").padding(6).background(.white, in: .circle)
    }

    // 경로·도형
    MapPolyline(coordinates: routeCoords).stroke(.blue, lineWidth: 4)

    UserAnnotation()
}
.mapControls {
    MapUserLocationButton()
    MapCompass()
}
```

`MapCameraPosition` 이 카메라 상태를 소유하므로, [상태 기반 SwiftUI 모델](../../02_ui_frameworks/swiftui/state-ownership-property-wrappers.md)에 자연스럽게 맞는다.

### 성능 — 어노테이션 수가 지배적이다

수천 개의 핀을 그대로 올리면 지도가 멈춘다.

| 대응 | 방법 |
| :--- | :--- |
| **클러스터링** | 가까운 핀을 묶어 하나로 (`MKMarkerAnnotationView` 의 `clusteringIdentifier`) |
| **가시 영역만 표시** | 현재 `region` 안의 항목만 필터 |
| **뷰 재사용** | UIKit 에서는 `dequeueReusableAnnotationView` — [셀 재사용과 같은 규칙](../../02_ui_frameworks/uikit/cell-reuse-requires-full-state-reset.md) |
| **오버레이 단순화** | 경로 좌표를 다운샘플링 |

```swift
// UIKit: 어노테이션 뷰도 재사용된다 — 이전 상태가 남는다
func mapView(_ mapView: MKMapView, viewFor annotation: MKAnnotation) -> MKAnnotationView? {
    let view = mapView.dequeueReusableAnnotationView(withIdentifier: "pin", for: annotation)
    view.image = nil                       // ★ 이전 상태 초기화
    (view as? MKMarkerAnnotationView)?.clusteringIdentifier = "group"
    return view
}
```

### 검색과 경로

```swift
// 주변 검색
let request = MKLocalSearch.Request()
request.naturalLanguageQuery = "카페"
request.region = currentRegion
let response = try await MKLocalSearch(request: request).start()

// 경로 계산
let dirRequest = MKDirections.Request()
dirRequest.source = MKMapItem(placemark: .init(coordinate: from))
dirRequest.destination = MKMapItem(placemark: .init(coordinate: to))
dirRequest.transportType = .automobile
let route = try await MKDirections(request: dirRequest).calculate()
```

**이 API 들은 네트워크를 쓰고 호출 빈도 제한이 있다.** 스크롤할 때마다 검색을 날리면 제한에 걸린다. 디바운스가 필요하다.

### 지오코딩

```swift
// 좌표 → 주소
let placemarks = try await CLGeocoder().reverseGeocodeLocation(location)

// 주소 → 좌표
let results = try await CLGeocoder().geocodeAddressString("서울시 중구")
```

> [!WARNING] 지오코딩은 서버 호출이며 엄격히 제한된다
> 짧은 시간에 반복 호출하면 실패한다. **결과를 캐시하고, 목록의 각 행마다 호출하지 않는다.** 대량 변환이 필요하면 서버에서 처리한다.

### 관찰 가능한 증거

```swift
// 어노테이션 수와 현재 영역
print(mapView.annotations.count, mapView.region)
```

```bash
xcrun simctl location booted set 37.5665,126.9780
log stream --device --predicate 'process == "locationd"' --info
```

**Instruments의 Time Profiler** 로 `viewFor annotation` 이 두꺼운지 확인한다. 두꺼우면 재사용이 깨졌거나 어노테이션이 너무 많다. **Energy Log** 는 지도 렌더링과 위치 갱신의 소모를 분리해 보여준다.

### 연관 문서

- [위치 권한과 정확도는 서로 독립된 두 축이다](authorization-and-accuracy-are-independent-axes.md)
- [배경 위치 갱신은 모드 선언·플래그·권한 세 가지가 모두 맞아야 한다](background-location-requires-mode-and-indicator.md)
- [셀 재사용은 이전 상태를 그대로 물려주므로 모든 상태를 명시적으로 되돌려야 한다](../../02_ui_frameworks/uikit/cell-reuse-requires-full-state-reset.md)
- [히치는 평균 FPS 가 아니라 사용자가 실제로 본 지연을 잰다](../../01_system_internals/graphics-and-media/hitches-measure-user-visible-jank.md)

공식 문서: [MapKit](https://developer.apple.com/documentation/mapkit) · [MapKit for SwiftUI](https://developer.apple.com/documentation/mapkit/mapkit-for-swiftui)
