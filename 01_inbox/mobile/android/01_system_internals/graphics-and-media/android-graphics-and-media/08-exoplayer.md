# ExoPlayer

상위 노트: [[android-graphics-and-media]]

```kotlin
val player = ExoPlayer.Builder(context).build()
playerView.player = player

val mediaItem = MediaItem.fromUri(videoUri)
player.setMediaItem(mediaItem)
player.prepare()
player.play()
```

### Adaptive Streaming (DASH/HLS)

```kotlin
val dataSourceFactory = DefaultHttpDataSource.Factory()
val dashMediaSource = DashMediaSource.Factory(dataSourceFactory)
    .createMediaSource(MediaItem.fromUri(dashUri))

player.setMediaSource(dashMediaSource)
```

**자동 품질 조정**:

```
네트워크 속도 감지 → 낮은 비트레이트로 전환
속도 회복 → 높은 비트레이트로 전환
```

---
