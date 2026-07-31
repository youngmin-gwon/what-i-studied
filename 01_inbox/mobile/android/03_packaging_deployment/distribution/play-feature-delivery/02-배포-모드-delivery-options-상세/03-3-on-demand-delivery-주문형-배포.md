# 3 On-demand Delivery (주문형 배포)

| 항목           | 설명                                            |
|--------------|-----------------------------------------------|
| **동작**       | 앱이 런타임에 명시적으로 요청할 때만 다운로드                     |
| **사용 가능 시점** | 다운로드 + 설치 완료 후                                |
| **필요 라이브러리** | Play Core SDK / Play Feature Delivery Library |

```xml

<dist:delivery>
    <dist:on-demand />
</dist:delivery>
```

**런타임 요청 및 상태 모니터링 코드 (Kotlin):**

On-demand 다운로드는 백그라운드에서 오랜 시간 소요되거나 여러 변수가 발생할 수 있으므로, `SplitInstallStateUpdatedListener`를 등록하여 상태
변화를 리스닝하고 사용자에게 시각적인 피드백을 전달해야 합니다.

```kotlin
val splitInstallManager = SplitInstallManagerFactory.create(context)
var mySessionId = 0

// 상태 업데이트 리스너 설정
val listener = SplitInstallStateUpdatedListener { state ->
    if (state.sessionId() == mySessionId) {
        when (state.status()) {
            SplitInstallSessionStatus.DOWNLOADING -> {
                val totalBytes = state.totalBytesToDownload()
                val progress = state.bytesDownloaded()
                // TODO: UI에 다운로드 진행 상태 업데이트 (progress / totalBytes)
            }
            SplitInstallSessionStatus.INSTALLING -> {
                // UI에 설치 중 메시지 표시
            }
            SplitInstallSessionStatus.INSTALLED -> {
                // 다운로드 및 설치 성공 -> 해당 기능 화면 진입 허용
            }
            SplitInstallSessionStatus.FAILED -> {
                val errorCode = state.errorCode()
                // 사용자에게 에러 상황을 명확히 알리고 필요시 재시도 버튼 노출
            }
            SplitInstallSessionStatus.REQUIRES_USER_CONFIRMATION -> {
                // 10MB가 넘는 모듈 등 사용 승인이 필요할 때 Play Store의 확인 대화상자 노출
                splitInstallManager.startConfirmationDialogForResult(state, activity, REQUEST_CODE)
            }
        }
    }
}

// 리스너 등록 (일반적으로 Activity의 onResume 등에서)
splitInstallManager.registerListener(listener)

val request = SplitInstallRequest.newBuilder()
    .addModule("feature_ar")
    .build()

splitInstallManager.startInstall(request)
    .addOnSuccessListener { sessionId ->
        mySessionId = sessionId
    }
    .addOnFailureListener { exception ->
        // 요청 자체 실패 시 처리
    }

// 메모리 누수 방지를 위해 사용 종료 시 해제 (일반적으로 Activity의 onPause 등에서)
// splitInstallManager.unregisterListener(listener)
```

**적합한 상황:**

- **일부 사용자만 사용하는 기능** (예: AR 기능, 고급 편집 도구)
- 용량이 큰 부가 기능 (예: 특수 필터, 이미지 인식 모델)
- 유료/프리미엄 전용 기능
- 특정 이벤트나 시즌에만 필요한 기능

> [!WARNING]
> On-demand 모듈을 요청할 때는 **반드시 다운로드 진행률 UI를 제공**하세요. 특히 10MB를 초과하는 모듈은 사용자 확인 대화상자가 표시됩니다.

---
