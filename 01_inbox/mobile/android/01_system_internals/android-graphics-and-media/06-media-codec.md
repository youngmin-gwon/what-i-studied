# Media Codec

상위 노트: [[android-graphics-and-media]]

### 비디오 인코딩

```kotlin
val codec = MediaCodec.createEncoderByType(MediaFormat.MIMETYPE_VIDEO_AVC)
val format = MediaFormat.createVideoFormat(MIMETYPE_VIDEO_AVC, width, height)
format.setInteger(MediaFormat.KEY_BIT_RATE, bitRate)
format.setInteger(MediaFormat.KEY_FRAME_RATE, frameRate)
format.setInteger(MediaFormat.KEY_I_FRAME_INTERVAL, 1)

codec.configure(format, null, null, MediaCodec.CONFIGURE_FLAG_ENCODE)
codec.start()

// 입력
val inputBufferId = codec.dequeueInputBuffer(timeout)
val inputBuffer = codec.getInputBuffer(inputBufferId)
inputBuffer.put(rawData)
codec.queueInputBuffer(inputBufferId, 0, size, presentationTimeUs, 0)

// 출력
val bufferInfo = MediaCodec.BufferInfo()
val outputBufferId = codec.dequeueOutputBuffer(bufferInfo, timeout)
val outputBuffer = codec.getOutputBuffer(outputBufferId)
// encoded data 사용
codec.releaseOutputBuffer(outputBufferId, false)
```

### 하드웨어 가속

```kotlin
// Surface 입력 모드 (Camera → Encoder 직접 연결)
codec.configure(format, null, null, MediaCodec.CONFIGURE_FLAG_ENCODE)
val inputSurface = codec.createInputSurface()

// Camera를 inputSurface로
camera.setPreviewTexture(SurfaceTexture(inputSurface))
```

**이점**: CPU/메모리 복사 없음 (Zero-copy)

---
