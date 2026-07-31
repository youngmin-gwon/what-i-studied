# On-demand와 conditional delivery는 설치 상태와 실패 UX를 설계해야 한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [Play Delivery 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/play-delivery-contracts.md)
관련 정본: [AAB는 Play가 기기별 APK를 생성하는 게시 아티팩트다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/aab-is-publishing-artifact-for-play-generated-apks.md)

## on-demand 요청

Play Feature Delivery Library의 `SplitInstallManager`가 모듈 요청을 담당한다.
요청 성공은 다운로드가 끝났다는 뜻이 아니라 session ID를 받았다는 뜻이다.
상태 listener로 다운로드와 설치 완료를 확인한 뒤 기능 화면을 연다.

```kotlin
val manager = SplitInstallManagerFactory.create(context)
val request = SplitInstallRequest.newBuilder()
    .addModule("photo-editor")
    .build()

manager.startInstall(request)
    .addOnSuccessListener { sessionId ->
        // listener에서 INSTALLED까지 기다린다.
    }
    .addOnFailureListener { error ->
        // 재시도 또는 취소 흐름을 표시한다.
    }
```

`SplitInstallStateUpdatedListener`에서 session ID를 필터링한다.
`DOWNLOADING`, `INSTALLING`, `INSTALLED`, `FAILED`를 사용자 흐름에 연결한다.
큰 다운로드는 Wi-Fi 대기나 사용자 확인 상태가 될 수 있다.
`REQUIRES_USER_CONFIRMATION`이면 Play가 제공하는 확인 UI를 호출한다.

## 지연 설치

당장 필요하지 않은 on-demand 모듈은 `deferredInstall()`로 백그라운드 설치를
요청할 수 있다. 진행률을 추적할 수 없는 best-effort 요청이므로,
다음 사용 시 `installedModules`를 다시 확인하고 필요하면 즉시 요청한다.

## conditional manifest

```xml
<dist:delivery>
    <dist:install-time>
        <dist:conditions>
            <dist:min-sdk dist:value="26" />
            <dist:device-feature dist:name="android.hardware.camera.ar" />
            <dist:user-countries dist:exclude="false">
                <dist:country dist:code="KR" />
            </dist:user-countries>
        </dist:conditions>
    </dist:install-time>
</dist:delivery>
```

지원 조건에는 기기 기능, OpenGL ES, 사용자 국가, API level, 기기 모델,
RAM, system feature, API 31 이상 기기의 SoC가 포함된다.
모든 조건을 만족해야 설치 시 자동 다운로드된다.

조건에 맞지 않은 기기도 앱 안에서 on-demand 요청을 받을 수 있다.
다만 해당 기능이 조건 외 기기에서 실제로 동작하는지 별도로 검증한다.

## 공식 문서

- [Configure on-demand delivery](https://developer.android.com/guide/playcore/feature-delivery/on-demand)
- [Configure conditional delivery](https://developer.android.com/guide/playcore/feature-delivery/conditional)
