---
title: "CameraManager 접근은 가용성 콜백과 캐릭터리스틱 조회로 시작한다"
tags: ["android", "android/system-services"]
---

# CameraManager 접근은 가용성 콜백과 캐릭터리스틱 조회로 시작한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [미디어/오디오/카메라 시스템 서비스 접근 계약](01_inbox/mobile/android/04_system_services/device-capabilities/media-audio-camera-contracts/media-audio-camera-contracts.md)

## 핵심 정의

`CameraManager`(Camera2/CameraX 기반)는 기기의 카메라 목록을 열거하고, 각 카메라의 `CameraCharacteristics`(해상도, 지원 포맷, 렌즈 방향, 하드웨어 지원 수준 등)를 조회한 뒤, `AvailabilityCallback`으로 카메라 사용 가능 여부 변화를 통지받는 구조로 설계돼 있다. 카메라는 시스템에서 한 번에 하나의 클라이언트만 독점적으로 열 수 있는 자원이다.

## 메커니즘

카메라를 열기 전 `getCameraIdList()`로 사용 가능한 카메라 ID 목록을, `getCameraCharacteristics(id)`로 해당 카메라의 능력을 조회한다. `registerAvailabilityCallback()`으로 등록한 콜백은 다른 프로세스가 카메라를 점유하거나 해제할 때 `onCameraAvailable()`/`onCameraUnavailable()`로 통지된다. `openCamera()` 호출 후 이미 다른 앱이나 시스템 컴포넌트가 카메라를 점유 중이면 `onDisconnected()` 또는 `ERROR_CAMERA_IN_USE`로 실패한다.

## 판단 기준

- 카메라를 열기 전 가용성 콜백으로 다른 앱의 점유 여부를 먼저 확인하면, 무작정 `openCamera()`를 호출해 실패를 다루는 것보다 더 나은 사용자 피드백(예: "다른 앱이 카메라를 사용 중입니다")을 줄 수 있다.
- 다중 카메라 기기에서는 렌즈 방향, 초점 거리, 지원 해상도가 카메라 ID마다 다르므로 `CameraCharacteristics`를 조회하지 않고 카메라 ID를 하드코딩하지 않는다.
- 대부분의 앱 개발에는 Camera2를 직접 다루기보다 CameraX가 제공하는 lifecycle-aware 추상화를 우선 검토한다. Camera2 직접 제어가 필요한 경우(수동 노출/포커스 등)만 저수준 API로 내려간다.

## 경계

- 이 노트는 카메라 세션을 열기 전 확인해야 할 시스템 서비스 접근 계약까지 다룬다. 캡처 파이프라인, 이미지 포맷 변환, 인코딩은 `01_system_internals/graphics-and-media`가 다룬다.
- 카메라 permission 승인 이후에도 AppOps가 실행 시점에 거부할 수 있는 계층은 [AppOps는 permission 승인 뒤에도 실행 시점 정책을 추가로 거부할 수 있다](01_inbox/mobile/android/04_system_services/service-lookup/service-lookup-contracts/appops-can-deny-after-permission-is-already-granted.md)와 함께 읽는다.

## 관찰 가능한 신호

`adb shell dumpsys media.camera`로 현재 카메라 서비스의 활성 클라이언트, 점유 상태를 확인할 수 있다. 카메라 열기 실패 시 logcat의 `CameraAccessException` 에러 코드로 원인(권한, 점유 중, 비활성화 등)을 구분한다.

## 공식 문서

- https://developer.android.com/media/camera/camera2
- https://developer.android.com/media/camera/camerax
