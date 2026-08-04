---
title: 02-photo-capture-preview-save-upload
tags: ["android", "android/foundations", "worked-example"]
aliases: ["Photo capture, preview, save, and upload", "사진 촬영, preview, 저장, 업로드까지"]
date modified: 2026-08-04 16:00:00 +09:00
date created: 2026-08-04 02:20:00 +09:00
---

## 사진 촬영, preview, 저장, 업로드까지 (Photo Capture, Preview, Save, and Upload)

이 예시는 Learning Spine 7·8·9·10 장을 하나의 카메라 비즈니스 유스케이스로 연결한다. 카메라라는 기기 하드웨어 독점 자원의 발견과 독립적 권한 게이트(9·10 장), 프레임을 앱 메인 메모리 복사 없이 화면에 바인딩하는 Surface 렌더링 경로(7 장), 캡처된 사진의 MediaStore 로컬 우선 저장(Outbox 패턴)과 WorkManager 기반 지연 업로드 보장 계약(8 장)을 다층 레이어 서사로 풀어낸다.

---

### 시작 상태

앱에 "카메라 촬영" 화면이 열려 있다. `CAMERA` 런타임 권한(Dangerous Permission)과 시스템 프라이버시 토글(AppOps)의 승인 상태를 확인해야 하며, 캡처된 미디어를 갤러리에 추가하기 위한 준비가 필요하다.

---

### 입력

사용자가 카메라 프리뷰 화면 진입 후, 셔터 버튼을 탭하여 사진 촬영을 요청한다.

---

### 다층 계층별 실행 흐름 (Multi-Layer Narrative)

```
[UI Layer] PreviewView (SurfaceView) Display & Shutter Button Tap
       │
       ▼
[App Framework Layer] CameraX / Camera2 (ProcessCameraProvider)
       │               -> AppOpsManager & Permission Verification
       │               -> CameraDevice.createCaptureSession()
       │               -> ImageReader acquires hardware frame buffer
       ▼
[System Server / IPC Layer] Binder IPC to CameraService (cameraserver)
       │                      -> AppOpsService Privacy Switch Check
       │                      -> MediaProvider IPC for MediaStore insertion
       │                      -> WorkManager JobScheduler persistence
       ▼
[Kernel / Hardware Layer] Camera Service communicates via AIDL to Camera HAL3
       │                    -> Hardware ISP (Image Signal Processor) capturing
       │                    -> Gralloc / HardwareBuffer DMA-BUF zero-copy allocation
       │                    -> NVMe / UFS Storage write (f2fs/ext4)
       ▼
[Network / Background Work] WorkManager -> Baseband Modem Driver -> Cloud Server
```

1. **UI / 입력 레이어**:
   - 사용자가 셔터 버튼을 탭하면 클릭 이벤트가 Main Thread Looper 를 거쳐 카메라 capture handler 로 전달된다.
   - 라이브 비디오 프리뷰는 `PreviewView` 내부의 `SurfaceView` Surface 로 흐르고 있으며, GPU 합성기(`SurfaceFlinger`)가 디스플레이 렌더링을 담당한다.

2. **App Framework 레이어**:
   - 앱은 `CameraManager` 또는 `CameraX`(`ProcessCameraProvider`)를 통해 하드웨어 파이프라인을 구성한다.
   - `checkSelfPermission`으로 `CAMERA` 권한을 확인하고, `AppOpsManager`로 시스템 수준의 카메라 차단 유무를 점검한다.
   - `CameraDevice.createCaptureSession()`을 통해 `Preview` Surface 와 `ImageCapture`용 `ImageReader` Surface 를 한 번에 구성한다.
   - 셔터 탭 시 `ImageReader`의 `onImageAvailable()` 콜백이 트리거되어 `Image` 객체(YUV/JPEG)를 획득한다.

3. **System Server 및 IPC 레이어**:
   - `CameraDevice` 호출은 Binder IPC 를 통해 OS 의 `cameraserver` 프로세스로 전달된다.
   - `AppOpsService`는 앱이 카메라에 접근할 수 있는 최신 런타임 상태인지 검증한다.
   - 사진 저장 시 `MediaProvider` 프로세스와 IPC 통신을 수행하여 `MediaStore` DB 에 튜플을 생성한다.
   - 업로드 작업 요청 시 `WorkManager`는 `JobSchedulerService`와 통신하여 SQLite DB 에 지속 가능 작업(Durable Job)을 등록한다.

4. **Kernel 및 Hardware Layer**:
   - `cameraserver`는 AIDL/HIDL 로 `Camera HAL3` 모듈에 명령을 전달하고, 하드웨어 센서 및 ISP(Image Signal Processor)가 렌더링 프레임 데이터를 생성한다.
   - 프레임 버퍼는 `Gralloc`을 통해 `HardwareBuffer`(DMA-BUF) 메모리로 할당되어 CPU 공간으로의 불필요한 픽셀 복사(Zero-Copy) 없이 GPU 및 인코더로 직행한다.
   - 캡처 파일은 저장소 드라이버(UFS/f2fs)를 통해 저장되고, 네트워크 상태가 만족되면 샐룰러/Wi-Fi 모뎀 드라이버를 통해 서버로 전송된다.

---

### Android 14 / 15 / 16 platform specific behaviors

1. **Android 12+ Quick Settings Camera Privacy Toggle (AppOps)**:
   - Android 12 이상에서는 퀵 설정 창에 글로벌 "카메라 차단" 토글이 존재한다. `Manifest.permission.CAMERA`가 `GRANTED` 상태라 하더라도, 사용자가 퀵 설정을 통해 카메라를 차단하면 `AppOpsManager`가 `MODE_IGNORED`를 반환하며, 카메라 세션은 검은색 프레임만 반환하거나 `SecurityException`을 던진다.

2. **Foreground Service Types Requirement (Android 14 / 15 / 16)**:
   - Android 14 이상에서 앱이 백그라운드 상태이거나 화면이 꺼진 동안 카메라 센서를 계속 캡처해야 하는 경우, 매니페스트에 `<service android:foregroundServiceType="camera">`를 선언해야 한다.
   - 촬영된 대용량 이미지/비디오 인코딩 및 처리 작업을 수행할 때는 Android 14+ 에 도입된 `foregroundServiceType="mediaProcessing"`을 사용하여 OS 스케줄러의 강제 종료를 방지한다.

3. **Scoped Storage & MediaStore Atomic Publishing (`IS_PENDING`)**:
   - Android 10 이상 Scoped Storage 환경에서는 앱이 외부 저장소 전체 쓰기 권한(`WRITE_EXTERNAL_STORAGE`) 없이도 `MediaStore`에 사진을 작성할 수 있다. `IS_PENDING=1` 상태로 파일을 생성해 쓰기를 진행한 후, 인코딩이 완료되는 시점에 `IS_PENDING=0`으로 업데이트하여 atomic 하게 갤러리에 노출시킨다.

---

### 성공 경로 vs 실패 분기 비교

| 항목 | 성공 경로 (Success Path) | 실패 분기 (Failure Branch 1: Camera Monopolized) | 실패 분기 (Failure Branch 2: ImageReader Buffer Leak) |
| :--- | :--- | :--- | :--- |
| **진행 현상** | 프리뷰 정상 작동, 셔터 클릭 즉시 MediaStore 에 사진 저장 후 배경 업로드 등록 | 촬영 화면 진입 시 "카메라를 열 수 없습니다" 에러 표시 또는 화면 검게 멈춤 | 1~2 회 촬영 후 더 이상 셔터가 반응하지 않고 프리뷰가 멈춤 |
| **원인 메커니즘** | 하드웨어 점유 성공, Zero-Copy Surface 바인딩, `IS_PENDING` 관리 및 WorkManager 성공 | 다른 앱(예: 영상 통화)이 카메라 단일 점유 자원을 소유하고 있어 오픈 실패 | `ImageReader.acquireNextImage()` 호출 후 `image.close()`를 누락하여 Reader 버퍼 큐 고갈 |
| **관측 가능 신호** | `dumpsys media.camera` 내 클라이언트 바인딩 활성화, MediaStore `IS_PENDING=0` | `CameraAccessException: CAMERA_IN_USE (1)`, logcat 에 `onDisconnected()` 수신 | logcat: `ImageReader_JNI: Discarding image.. buffer queue is full`, `ImageReader` 멈춤 |

---

### CLI 진단 명령어 및 관찰 도구

1. **카메라 서비스 점유 및 활성 스트림 확인**:
   ```bash
   adb shell dumpsys media.camera
   # 출력 내용 중 Active Camera Clients 및 Package Name, Surface format/dimensions 점검
   ```

2. **AppOps 프라이버시 차단 상태 조회**:
   ```bash
   adb shell dumpsys appops com.example.app | grep -i CAMERA
   # OP_CAMERA: mode=0 (Granted) 또는 mode=1 (Ignored - 퀵 설정 차단)
   ```

3. **Camera2 / CameraX 전용 Logcat 추적**:
   ```bash
   adb logcat -v time -s Camera2Client:V Camera3-Device:V CameraX:D
   ```

4. **WorkManager 업로드 작업 예약 상태 진단**:
   ```bash
   adb shell dumpsys jobscheduler | grep com.example.app
   # 또는 WorkManager DB 확인
   adb shell dumpsys activity service com.example.app/androidx.work.impl.background.systemjob.SystemJobService
   ```

---

### 실전 코드 예시 (Production Code Examples)

```kotlin
// CameraCaptureManager.kt
package com.example.app

import android.content.ContentValues
import android.content.Context
import android.net.Uri
import android.os.Environment
import android.provider.MediaStore
import androidx.camera.core.ImageCapture
import androidx.camera.core.ImageCaptureException
import androidx.core.content.ContextCompat
import androidx.work.*
import java.util.concurrent.Executor

class CameraCaptureManager(private val context: Context) {

    // 1. MediaStore 에 Pending 상태로 파일 인서트 후 비동기 쓰기
    fun captureAndEnqueueUpload(imageCapture: ImageCapture, executor: Executor) {
        val resolver = context.contentResolver
        val contentValues = ContentValues().apply {
            put(MediaStore.Images.Media.DISPLAY_NAME, "IMG_${System.currentTimeMillis()}.jpg")
            put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg")
            put(MediaStore.Images.Media.RELATIVE_PATH, Environment.DIRECTORY_PICTURES)
            // Android 10+ Scoped Storage: 작성 중에는 사용자 갤러리에 비노출
            put(MediaStore.Images.Media.IS_PENDING, 1)
        }

        val uri = resolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, contentValues)
            ?: return

        val outputOptions = ImageCapture.OutputFileOptions.Builder(resolver, uri, contentValues).build()

        imageCapture.takePicture(
            outputOptions,
            executor,
            object : ImageCapture.OnImageSavedCallback {
                override fun onImageSaved(outputFileResults: ImageCapture.OutputFileResults) {
                    // 쓰기 완료 -> IS_PENDING = 0 변환 (Atomic Publishing)
                    contentValues.clear()
                    contentValues.put(MediaStore.Images.Media.IS_PENDING, 0)
                    resolver.update(uri, contentValues, null, null)

                    // 2. 업로드 작업은 화면 Scope 가 아닌 WorkManager 로 위임
                    scheduleBackgroundUpload(uri)
                }

                override fun onError(exception: ImageCaptureException) {
                    // 저장 실패 시 pending row 정리
                    resolver.delete(uri, null, null)
                }
            }
        )
    }

    private fun scheduleBackgroundUpload(photoUri: Uri) {
        val constraints = Constraints.Builder()
            .setRequiredNetworkType(NetworkType.CONNECTED)
            .build()

        val uploadWorkRequest = OneTimeWorkRequestBuilder<PhotoUploadWorker>()
            .setInputData(workDataOf("KEY_PHOTO_URI" to photoUri.toString()))
            .setConstraints(constraints)
            .setBackoffCriteria(BackoffPolicy.EXPONENTIAL, WorkRequest.MIN_BACKOFF_MILLIS, java.util.concurrent.TimeUnit.MILLISECONDS)
            .build()

        WorkManager.getInstance(context).enqueueUniqueWork(
            "upload_photo_${photoUri.lastPathSegment}",
            ExistingWorkPolicy.KEEP,
            uploadWorkRequest
        )
    }
}
```

---

### 관련 원자 노트

- [CameraManager 접근은 가용성 콜백과 캐릭터리스틱 조회로 시작한다](../../04_system_services/device-capabilities/media-audio-camera-contracts/cameramanager-access-starts-with-availability-and-characteristics.md)
- [카메라 출력 Surface는 프리뷰, 분석, 녹화 파이프라인을 정의한다](../../01_system_internals/graphics-and-media/graphics-media-contracts/camera-output-surfaces-define-preview-analysis-and-recording-pipelines.md)
- [Surface 기반 미디어 파이프라인은 앱 수준 픽셀 복사를 줄인다](../../01_system_internals/graphics-and-media/graphics-media-contracts/surface-based-media-pipeline-avoids-app-level-pixel-copy.md)
- [MediaStore: 공유 미디어의 등록과 접근](../../02_app_framework/data/storage/file-access-contracts/mediastore-registers-shared-media.md)
- [Runtime permission은 사용자에게 기능 사용 시점에 요청하는 접근 계약이다](../../05_security_privacy/permissions-and-sandbox/permission-contracts/runtime-permission-is-user-mediated-access-contract.md)
- [AppOps는 permission 승인 뒤에도 실행 시점 정책을 추가로 거부할 수 있다](../../04_system_services/service-lookup/service-lookup-contracts/appops-can-deny-after-permission-is-already-granted.md)
- [WorkManager는 지연 가능한 보장 작업의 기본 선택이다](../../04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)

---

### 관련 Learning Spine 장

- [7장 입력, 리소스 선택과 화면 프레임](../learning-spine/07-input-resource-selection-and-display-frame.md)
- [8장 데이터, 저장소, 네트워크와 offline recovery](../learning-spine/08-data-storage-network-and-offline-recovery.md)
- [9장 Identity, 권한과 독립적인 security gate](../learning-spine/09-identity-permission-and-independent-security-gates.md)
- [10장 기기 기능 발견과 background execution](../learning-spine/10-device-capability-discovery-and-background-execution.md)

---

### 관련 Diagnostic Runbook

- [04-permission-denial.md](../diagnostic-runbooks/04-permission-denial.md)
- [05-background-work-delayed-or-not-running.md](../diagnostic-runbooks/05-background-work-delayed-or-not-running.md)

---

### 공식 근거

- [Camera2 overview](https://developer.android.com/media/camera/camera2)
- [CameraX architecture](https://developer.android.com/media/camera/camerax/architecture)
- [Access media files from shared storage](https://developer.android.com/training/data-storage/shared/media)
- [Foreground service types](https://developer.android.com/about/versions/14/changes/fgs-types-required)

검증일: 2026-08-04. CameraX 1.3+ UseCase 규칙, Scoped Storage `IS_PENDING` 플래그, AppOps 카메라 차단 토글 동작을 공식 문서를 기준으로 검증함.
