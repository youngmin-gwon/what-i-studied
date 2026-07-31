# Picture-in-Picture (PiP)

상위 노트: [[android-large-screens]]

```kotlin
// build.gradle.kts
android {
    defaultConfig {
        minSdk = 26 // PiP 는 Android 8.0+
    }
}

class VideoPlayerActivity : AppCompatActivity() {
    
    override fun onUserLeaveHint() {
        super.onUserLeaveHint()
        
        if (isVideoPlaying) {
            enterPictureInPictureMode(createPipParams())
        }
    }
    
    private fun createPipParams(): PictureInPictureParams {
        val aspectRatio = Rational(16, 9)
        
        return PictureInPictureParams.Builder()
            .setAspectRatio(aspectRatio)
            .setActions(createPipActions())
            .build()
    }
    
    private fun createPipActions(): List<RemoteAction> {
        val playPauseIntent = PendingIntent.getBroadcast(
            this,
            0,
            Intent(ACTION_PLAY_PAUSE),
            PendingIntent.FLAG_IMMUTABLE
        )
        
        val playPauseAction = RemoteAction(
            Icon.createWithResource(this, R.drawable.ic_play_pause),
            "Play/Pause",
            "Play or pause video",
            playPauseIntent
        )
        
        return listOf(playPauseAction)
    }
    
    override fun onPictureInPictureModeChanged(
        isInPictureInPictureMode: Boolean,
        newConfig: Configuration
    ) {
        super.onPictureInPictureModeChanged(isInPictureInPictureMode, newConfig)
        
        if (isInPictureInPictureMode) {
            // PiP 모드: 컨트롤 숨기기
            hideControls()
        } else {
            // 전체 화면: 컨트롤 표시
            showControls()
        }
    }
}
```
