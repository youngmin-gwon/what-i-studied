---
title: media-session-controllers
tags: ["android", "android/system-services"]
aliases: ["MediaSession은 재생 상태를 시스템 UI와 외부 컨트롤러에 노출하는 계약이다"]
date modified: 2026-08-06 14:59:18 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## MediaSession은 재생 상태를 시스템 UI와 외부 컨트롤러에 노출하는 계약이다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [미디어/오디오/카메라 시스템 서비스 접근 계약](./media-audio-camera.md)
배경 지식: [IPC 메커니즘](../../../../../operating-systems/ipc-mechanisms.md)

### 핵심 정의

`MediaSession`(미디어 앱의 재생 상태와 조작 명령을 시스템 UI 및 외부 기기와 매개하는 IPC 통신 계약 객체)은 앱의 재생 엔진 내부 상태(재생 중/일시정지, 현재 트랙, 위치)를 잠금화면, 시스템 알림, 블루투스 리모컨, Wear OS, Assistant 같은 외부 컨트롤러가 공통 규약으로 읽고 제어할 수 있게 노출하는 시스템 연동 계층이다.

### 메커니즘

앱은 재생 상태가 바뀔 때마다 `PlaybackState`(현재 재생 상태, 재생 위치, 속도, 가능 제어 액션 목록을 나타내는 메타데이터 객체)를 갱신해 세션에 반영한다. 외부 컨트롤러(잠금화면 미디어 위젯, 블루투스 헤드셋의 재생/일시정지 버튼 등)는 세션에 등록된 `MediaController`(외부 프로세스나 UI가 MediaSession에 제어 명령을 보내기 위한 클라이언트 측 인터페이스)를 통해 명령(재생, 일시정지, 다음 곡)을 세션으로 보내고, 세션은 이를 콜백으로 앱에 전달한다. 앱이 `PlaybackState`를 정확히 갱신하지 않으면 외부 UI가 실제 재생 상태와 다르게 표시된다(예: 실제로는 멈췄는데 재생 중으로 보임).

미디어 알림(Notification)의 재생 컨트롤 스타일도 이 세션의 토큰을 참조해 시스템이 자동으로 잠금화면과 동기화한다.

### Media3 세션 소유 흐름

```kotlin
class PlaybackService : MediaSessionService() {
    private lateinit var player: ExoPlayer
    private lateinit var session: MediaSession

    override fun onCreate() {
        super.onCreate()
        player = ExoPlayer.Builder(this).build()
        session = MediaSession.Builder(this, player).build()
    }

    override fun onGetSession(info: MediaSession.ControllerInfo) = session

    override fun onDestroy() {
        session.release()
        player.release()
        super.onDestroy()
    }
}
```

Media3에서는 player의 상태·timeline이 session에 연결된다. 외부 controller를 무조건 신뢰하지 말고 `MediaSession.Callback.onConnect()`에서 controller identity와 허용 command를 결정한다. background playback은 session을 Activity가 아니라 `MediaSessionService`가 소유해 화면 재생성과 분리한다.

### 판단 기준

- 백그라운드 오디오 재생 앱은 반드시 `MediaSession`을 등록하고 `PlaybackState`를 실시간으로 갱신해야, 사용자가 화면을 보지 않아도 잠금화면/블루투스로 제어할 수 있다.
- 오디오 포커스 상실 콜백과 `PlaybackState` 갱신을 함께 처리한다. 포커스를 잃고 재생을 멈췄다면 세션의 상태도 즉시 "일시정지"로 갱신해야 외부 UI가 어긋나지 않는다.
- 여러 미디어 항목을 다루는 앱은 `MediaSession`과 함께 `MediaBrowserService`(또는 Media3의 대응 API)로 탐색 가능한 미디어 트리를 노출하면 차량, Wear OS 같은 외부 표면에서 콘텐츠를 탐색할 수 있다.

### 경계

- 이 노트는 재생 상태를 외부에 노출하는 계약까지 다룬다. 여러 앱 간 오디오 재생 자체의 조정은 [AudioManager는 포커스 요청으로 여러 앱의 동시 재생을 조정한다](audio-manager-focus-arbitration.md)가 다룬다.
- 알림 자체의 표시 규칙과 채널 정책은 `04_system_services/background-and-notifications/notification-messaging-contracts`가 다룬다.

### 관찰 가능한 신호

`adb shell dumpsys media_session`으로 현재 활성 미디어 세션 목록과 각 세션의 `PlaybackState`를 확인할 수 있다. 잠금화면 미디어 위젯이 실제 재생 상태와 다르게 보이면 이 덤프에서 세션 상태 갱신 누락을 먼저 확인한다.

### 공식 문서

- https://developer.android.com/media/media3/session/control-playback
- https://developer.android.com/guide/topics/media-apps/working-with-a-media-session

검증일: 2026-08-06. Media3의 service-owned session, controller command 승인, player/session release 흐름을 보강했다.
