# Audio

상위 노트: [android-graphics-and-media](01_inbox/mobile/android/01_system_internals/graphics-and-media/android-graphics-and-media.md)

### AudioTrack (Low-level)

```kotlin
val bufferSize = AudioTrack.getMinBufferSize(
    sampleRate,
    AudioFormat.CHANNEL_OUT_STEREO,
    AudioFormat.ENCODING_PCM_16BIT
)

val audioTrack = AudioTrack(
    AudioAttributes.Builder()
        .setUsage(AudioAttributes.USAGE_MEDIA)
        .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
        .build(),
    AudioFormat.Builder()
        .setSampleRate(sampleRate)
        .setEncoding(AudioFormat.ENCODING_PCM_16BIT)
        .setChannelMask(AudioFormat.CHANNEL_OUT_STEREO)
        .build(),
    bufferSize,
    AudioTrack.MODE_STREAM,
    AudioManager.AUDIO_SESSION_ID_GENERATE
)

audioTrack.play()
audioTrack.write(pcmData, 0, pcmData.size)
```

### Oboe (권장, NDK)

```cpp
#include <oboe/Oboe.h>

oboe::AudioStreamBuilder builder;
builder.setDirection(oboe::Direction::Output)
       ->setPerformanceMode(oboe::PerformanceMode::LowLatency)
       ->setFormat(oboe::AudioFormat::Float)
       ->setSampleRate(48000)
       ->setChannelCount(oboe::ChannelCount::Stereo)
       ->setCallback(this);

oboe::AudioStream *stream;
builder.openStream(&stream);
stream->start();
```

**지연 시간**:

- AAudio/Oboe: ~10ms
- AudioTrack: ~45ms

### AudioFocus

```kotlin
val focusRequest = AudioFocusRequest.Builder(AudioManager.AUDIOFOCUS_GAIN)
    .setOnAudioFocusChangeListener { focusChange ->
        when (focusChange) {
            AudioManager.AUDIOFOCUS_GAIN -> resumePlayback()
            AudioManager.AUDIOFOCUS_LOSS -> stopPlayback()
            AudioManager.AUDIOFOCUS_LOSS_TRANSIENT -> pausePlayback()
        }
    }
    .build()

audioManager.requestAudioFocus(focusRequest)
```

---
