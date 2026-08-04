---
title: 사진 촬영, preview, 저장, 업로드까지
tags: ["android", "android/foundations", "worked-example"]
aliases: ["Photo capture, preview, save, and upload"]
date modified: 2026-08-04 02:20:00 +09:00
date created: 2026-08-04 02:20:00 +09:00
---

## 사진 촬영, preview, 저장, 업로드까지

이 예시는 Learning Spine 7·8·9·10장을 하나의 기능으로 잇는다. 카메라라는 기기 기능의 발견과 권한 gate(9·10장), 프리뷰가 화면에 나타나는 렌더링 경로(7장), 촬영된 사진을 로컬에 먼저 저장하고 서버로는 지연된 지속 작업으로 올리는 데이터 계약(8장)을 연결한다.

### 시작 상태

앱에 "사진 촬영" 화면이 있다. `CAMERA` 런타임 권한은 아직 승인되지 않았을 수 있다(dangerous permission, 9장).

### 입력

사용자가 "카메라" 버튼을 탭해 촬영 화면을 열고, 이어서 셔터 버튼을 탭한다.

### 단계별 흐름

1. **권한 gate(9장)**: 화면 진입 시 앱은 `CAMERA` 권한이 이미 grant 상태인지 확인한다. 없으면 시스템 다이얼로그로 요청한다. 승인되더라도 이것이 곧 카메라를 열 수 있다는 뜻은 아니다 — AppOps가 실행 시점에 별도로 거부할 수 있다(9장 5절).
2. **기능 발견(10장)**: 앱은 `CameraManager.getCameraIdList()`로 사용 가능한 카메라를, `getCameraCharacteristics()`로 각 카메라의 해상도·렌즈 방향을 조회한다. `registerAvailabilityCallback()`으로 다른 앱이 카메라를 점유했는지 사전에 확인할 수 있다. 카메라는 한 번에 한 클라이언트만 열 수 있는 독점 자원이다.
3. **Preview 렌더링(7장)**: `openCamera()`가 성공하면 카메라 세션은 `PreviewView`(또는 `SurfaceView`)에 연결된 Surface로 프레임을 직접 전달한다. 이 경로는 앱이 매 프레임을 CPU 배열로 복사하지 않는, 7장에서 다룬 Surface/BufferQueue 계약을 그대로 따른다. 프리뷰 화면에 보이는 실시간 영상은 이 Surface가 SurfaceFlinger의 합성 대상 레이어가 된 결과다.
4. **촬영**: 셔터 탭은 별도의 `ImageReader` output Surface로 정지 이미지를 캡처하도록 요청한다. 캡처된 `Image`는 반드시 acquire 후 명시적으로 닫아야 한다. 열어둔 채로 방치하면 reader의 이미지 큐가 고갈돼 다음 프레임 처리가 막힐 수 있다.
5. **로컬 저장(8장)**: 캡처된 이미지는 갤러리에 공개돼야 하는 공유 미디어이므로 앱 전용 저장소가 아니라 `MediaStore`에 저장한다. `IS_PENDING=1`로 먼저 항목을 만들어 쓰기 중인 파일이 사용자에게 노출되지 않게 하고, 인코딩이 끝나면 `IS_PENDING=0`으로 갱신해 공개 상태로 전환한다. 이 저장은 로컬에서 즉시 끝나는 동작이며, 8장에서 다룬 "로컬 우선 쓰기" 원칙을 따른다.
6. **업로드는 화면 lifetime과 분리한다(6·8장)**: 사진을 서버에도 올려야 한다면, 이 업로드 요청은 화면이 사라져도 이어져야 하는 작업이다. 화면의 `viewModelScope`에 묶지 않고 WorkManager 같은 durable scheduler에 위임한다. 저장된 사진의 URI와 "아직 서버에 반영되지 않음"이라는 대기 상태를 로컬 저장소에 함께 기록한다(8장의 lazy write/outbox 패턴).
7. **네트워크가 돌아오면 업로드 실행**: WorkManager가 네트워크 constraint를 만족하는 시점에 업로드 Worker를 실행한다. 성공하면 대기 상태를 지우고, 실패하면 일시 오류인지 영구 오류인지 구분해 재시도하거나 사용자에게 알린다.

### 성공 결과

화면은 로컬 `MediaStore` 항목을 관찰하는 Flow를 통해 촬영된 사진을 즉시 보여준다. 업로드는 별도로 진행되며, 완료되면 로컬에 기록해둔 "대기 중" 상태가 사라지는 것으로 사용자에게 반영된다.

### 관찰 가능한 신호

- `adb shell dumpsys media.camera`로 카메라 서비스의 현재 활성 클라이언트와 점유 상태를 확인한다.
- 카메라 열기 실패는 logcat의 `CameraAccessException` 에러 코드로 원인(권한 없음, 다른 앱이 점유 중, 비활성화)을 구분한다.
- `WorkInfo.state`와 `adb shell dumpsys jobscheduler`로 업로드 작업이 실제로 예약·실행됐는지 확인한다.
- `dumpsys appops`로 `CAMERA` op의 모드가 permission grant 상태와 별개로 거부돼 있는지 확인한다.

### 실패 분기: 카메라를 열 수 없다

셔터를 누르기 전, `openCamera()` 자체가 실패하는 경우를 생각해 보자. 원인은 최소 세 가지로 갈린다.

1. **권한이 없다.** `CAMERA` 런타임 권한이 거부됐다면 `openCamera()`는 `SecurityException`으로 실패한다.
2. **권한은 있지만 AppOps가 막는다.** 권한은 granted 상태인데도 사용자가 설정에서 이 앱의 카메라 접근을 별도로 차단했다면, 권한 검사만 보고는 원인을 알 수 없다.
3. **다른 앱이 이미 카메라를 점유 중이다.** 이 경우 권한·AppOps와는 무관하게 `ERROR_CAMERA_IN_USE`나 `onDisconnected()`로 실패한다.

세 경우 모두 사용자 화면에는 "카메라를 열 수 없습니다"로 보일 수 있지만, 조사 순서는 다르다. 먼저 권한 grant 상태(9장), 그다음 AppOps 모드(9장), 마지막으로 카메라 서비스의 점유 상태(`dumpsys media.camera`)를 차례로 좁혀야 한다.

### 코드 예시

```kotlin
// 1. 권한 확인
if (ContextCompat.checkSelfPermission(context, Manifest.permission.CAMERA)
    != PackageManager.PERMISSION_GRANTED) {
    requestPermissionLauncher.launch(Manifest.permission.CAMERA)
    return
}

// 5. MediaStore에 pending 상태로 먼저 등록
val values = ContentValues().apply {
    put(MediaStore.Images.Media.DISPLAY_NAME, "IMG_${System.currentTimeMillis()}.jpg")
    put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg")
    put(MediaStore.Images.Media.RELATIVE_PATH, Environment.DIRECTORY_PICTURES)
    put(MediaStore.Images.Media.IS_PENDING, 1)
}
val uri = resolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values)

// 6. 업로드는 화면 lifetime이 아니라 WorkManager로 위임
val uploadRequest = OneTimeWorkRequestBuilder<UploadPhotoWorker>()
    .setInputData(workDataOf("photo_uri" to uri.toString()))
    .setConstraints(Constraints.Builder().setRequiredNetworkType(NetworkType.CONNECTED).build())
    .build()
workManager.enqueueUniqueWork("upload_${uri}", ExistingWorkPolicy.KEEP, uploadRequest)
```

### 관련 원자 노트

- [CameraManager 접근은 가용성 콜백과 캐릭터리스틱 조회로 시작한다](../../04_system_services/device-capabilities/media-audio-camera-contracts/cameramanager-access-starts-with-availability-and-characteristics.md)
- [카메라 출력 Surface는 프리뷰, 분석, 녹화 파이프라인을 정의한다](../../01_system_internals/graphics-and-media/graphics-media-contracts/camera-output-surfaces-define-preview-analysis-and-recording-pipelines.md)
- [Surface 기반 미디어 파이프라인은 앱 수준 픽셀 복사를 줄인다](../../01_system_internals/graphics-and-media/graphics-media-contracts/surface-based-media-pipeline-avoids-app-level-pixel-copy.md)
- [MediaStore: 공유 미디어의 등록과 접근](../../02_app_framework/data/storage/file-access-contracts/mediastore-registers-shared-media.md)
- [Runtime permission은 사용자에게 기능 사용 시점에 요청하는 접근 계약이다](../../05_security_privacy/permissions-and-sandbox/permission-contracts/runtime-permission-is-user-mediated-access-contract.md)
- [AppOps는 permission 승인 뒤에도 실행 시점 정책을 추가로 거부할 수 있다](../../04_system_services/service-lookup/service-lookup-contracts/appops-can-deny-after-permission-is-already-granted.md)
- [WorkManager는 지연 가능한 보장 작업의 기본 선택이다](../../04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)

### 관련 Learning Spine 장

- [7장 입력, 리소스 선택과 화면 프레임](../learning-spine/07-input-resource-selection-and-display-frame.md)
- [8장 데이터, 저장소, 네트워크와 offline recovery](../learning-spine/08-data-storage-network-and-offline-recovery.md)
- [9장 Identity, 권한과 독립적인 security gate](../learning-spine/09-identity-permission-and-independent-security-gates.md)
- [10장 기기 기능 발견과 background execution](../learning-spine/10-device-capability-discovery-and-background-execution.md)

### 공식 근거

- [Camera2 overview](https://developer.android.com/media/camera/camera2)
- [CameraX overview](https://developer.android.com/media/camera/camerax)
- [Camera2 capture sessions and requests](https://developer.android.com/media/camera/camera2/capture-sessions-requests)

검증일: 2026-08-04. 카메라 API의 세부 오류 코드와 MediaStore 열 이름은 API 레벨에 따라 달라질 수 있으므로 실제 구현 시점에 다시 확인한다.
