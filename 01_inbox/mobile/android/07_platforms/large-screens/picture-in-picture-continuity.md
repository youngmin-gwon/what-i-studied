---
title: picture-in-picture-continuity
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## PiP 는 백그라운드 UI 가 아니라 연속 시청을 위한 멀티윈도우 모드다

상위 문서: [큰 화면 적응 계약](large-screen.md)

Picture-in-Picture 는 앱을 항상 위에 띄우는 임의의 overlay 가 아니다. Android 가 제공하는 특수 multi-window 모드이며 주로 동영상, 영상 통화, 내비게이션처럼 사용자가 다른 작업 중에도 계속 봐야 하는 activity 에 적용한다.

### Manifest 선언 및 `PictureInPictureParams` 구현

```xml
<!-- AndroidManifest.xml -->
<activity
    android:name=".VideoPlayerActivity"
    android:supportsPictureInPicture="true"
    android:configChanges="screenSize|smallestScreenSize|screenLayout|orientation" />
```

```kotlin
fun updatePipParams(activity: Activity, isPlaying: Boolean) {
    val actions = ArrayList<RemoteAction>()
    // Play/Pause RemoteAction 생성 및 추가
    
    val params = PictureInPictureParams.Builder()
        .setAspectRatio(Rational(16, 9))
        .setActions(actions)
        .setAutoEnterEnabled(true)
        .build()

    activity.setPictureInPictureParams(params)
}
```

### 실무 규칙

- PiP 를 지원할 activity 는 manifest 에 명시하고 PiP 전환 중 configuration change 를 처리한다.
- PiP 진입 후에는 재생이나 안내처럼 본질적인 콘텐츠만 남기고 일반 UI chrome 은 숨긴다.
- system alert window 로 PiP 유사 경험을 만들지 않는다.
- PiP action 은 작은 창에서도 의미가 분명한 최소 조작만 제공한다.
- Compose 화면도 activity lifecycle 과 media/session 상태를 기준으로 PiP 전환을 설계한다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 최상위 Activity를 PiP(Pinned Stack)로 강제 이동하여 상태 테스트
adb shell am stack move-top-activity-to-pinned-stack-box 1 0 0 500 500

# 현재 윈도우 스택 및 PiP 모드 상태 dumpsys 관측
adb shell dumpsys window displays | grep -i "pinned"
```

### 관련 문서

- [데스크톱 윈도잉에서는 앱 창이 자유롭게 변한다](desktop-windowing-freeform.md)
- [적응형 앱 준비도는 창, posture, 입력 테스트로 판단한다](adaptive-app-readiness-testing.md)

공식 문서: [Use picture-in-picture](https://developer.android.com/develop/ui/views/picture-in-picture)

